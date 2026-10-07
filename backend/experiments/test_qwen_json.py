import json
import re
import torch

from transformers import (
    Qwen2VLForConditionalGeneration,
    AutoProcessor
)


MODEL_NAME = "Qwen/Qwen2-VL-2B-Instruct"


# ---------------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------------

print("Loading Qwen model...")

model = Qwen2VLForConditionalGeneration.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",
    device_map="auto"
)

processor = AutoProcessor.from_pretrained(
    MODEL_NAME
)

print("Model loaded successfully.")
print("GPU:", torch.cuda.get_device_name(0))


# ---------------------------------------------------------
# SAMPLE RESUME
# ---------------------------------------------------------

resume_text = """
Godson Nadar
Email: godson.nadar@gmail.com
Phone: 9876543210

SUMMARY
Third-year Artificial Intelligence and Machine Learning
engineering student interested in machine learning,
natural language processing and software development.

EDUCATION
Bachelor of Engineering in Artificial Intelligence and
Machine Learning, St. Francis Institute of Technology,
2024 - 2028

SKILLS
Python, SQL, Machine Learning, Deep Learning, NLP,
FastAPI, HTML, CSS, JavaScript, Git, PyTorch

EXPERIENCE
AI/ML Intern at ABC Technologies.
Worked on machine learning models and data preprocessing.
Developed Python-based solutions for internal projects.

PROJECTS
Smart Resume Validator
Developed a resume analysis system using Python and FastAPI.

OCR Extraction System
Built an OCR document extraction project using Qwen2-VL.

CERTIFICATIONS
Python Programming Certification
Machine Learning Fundamentals Certification
"""


# ---------------------------------------------------------
# PROMPT
# ---------------------------------------------------------

prompt = f"""
Extract information from the following resume.

Return ONLY a valid JSON object.

Do NOT use markdown.
Do NOT use ```json.
Do NOT add explanations.

Use exactly these keys:

{{
    "name": "",
    "email": "",
    "phone": "",
    "skills": [],
    "education": [],
    "experience": [],
    "projects": [],
    "certifications": []
}}

Rules:
- Keep missing string values as empty strings.
- Keep missing list values as empty lists.
- Do not invent information.
- Put each separate skill into the skills list.
- Keep education, experience, projects and certifications as separate items.

Resume:

{resume_text}
"""


# ---------------------------------------------------------
# PREPARE INPUT
# ---------------------------------------------------------

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": prompt
            }
        ]
    }
]


text = processor.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

inputs = processor(
    text=[text],
    padding=True,
    return_tensors="pt"
)

inputs = inputs.to(model.device)


# ---------------------------------------------------------
# GENERATE RESPONSE
# ---------------------------------------------------------

print("Generating structured response...")

with torch.no_grad():

    generated_ids = model.generate(
        **inputs,
        max_new_tokens=500,
        do_sample=False
    )


# ---------------------------------------------------------
# REMOVE PROMPT TOKENS
# ---------------------------------------------------------

generated_ids_trimmed = [
    output_ids[len(input_ids):]
    for input_ids, output_ids
    in zip(inputs.input_ids, generated_ids)
]


# ---------------------------------------------------------
# DECODE
# ---------------------------------------------------------

output = processor.batch_decode(
    generated_ids_trimmed,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)

raw_output = output[0].strip()


print("\n" + "=" * 60)
print("RAW QWEN OUTPUT")
print("=" * 60)
print(raw_output)


# ---------------------------------------------------------
# EXTRACT JSON
# ---------------------------------------------------------

def extract_json(text: str):
    """
    Extract a JSON object from Qwen output.

    Handles both pure JSON and JSON wrapped
    inside markdown/code fences.
    """

    # Remove markdown code fences if present
    cleaned = re.sub(
        r"```json\s*",
        "",
        text,
        flags=re.IGNORECASE
    )

    cleaned = re.sub(
        r"```\s*",
        "",
        cleaned
    ).strip()

    # Try the complete response first
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # Find the first JSON object
    start = cleaned.find("{")
    end = cleaned.rfind("}")

    if start == -1 or end == -1:
        return None

    json_text = cleaned[start:end + 1]

    try:
        return json.loads(json_text)
    except json.JSONDecodeError:
        return None


# ---------------------------------------------------------
# VALIDATE JSON STRUCTURE
# ---------------------------------------------------------

def validate_json_structure(data) -> bool:
    """
    Check that the Qwen response contains
    the fields expected by our application.
    """

    required_keys = {
        "name",
        "email",
        "phone",
        "skills",
        "education",
        "experience",
        "projects",
        "certifications"
    }

    if not isinstance(data, dict):
        return False

    if set(data.keys()) != required_keys:
        return False

    if not isinstance(data["name"], str):
        return False

    if not isinstance(data["email"], str):
        return False

    if not isinstance(data["phone"], str):
        return False

    list_fields = [
        "skills",
        "education",
        "experience",
        "projects",
        "certifications"
    ]

    for field in list_fields:

        if not isinstance(data[field], list):
            return False

    return True


# ---------------------------------------------------------
# PARSE RESPONSE
# ---------------------------------------------------------

parsed_data = extract_json(raw_output)


print("\n" + "=" * 60)
print("JSON VALIDATION")
print("=" * 60)


if parsed_data is None:

    print("JSON parsing failed.")

else:

    print("JSON parsing successful.")

    if validate_json_structure(parsed_data):

        print("JSON structure is valid.")

        print("\nSTRUCTURED RESUME DATA:")
        print(
            json.dumps(
                parsed_data,
                indent=4,
                ensure_ascii=False
            )
        )

    else:

        print("JSON structure is invalid.")
        print(
            "Received keys:",
            list(parsed_data.keys())
        )