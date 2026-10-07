import torch

from transformers import (
    Qwen2VLForConditionalGeneration,
    AutoProcessor
)


MODEL_NAME = "Qwen/Qwen2-VL-2B-Instruct"


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
You are a resume information extraction assistant.

Analyze the resume below and extract the information
into JSON.

Return ONLY valid JSON.
Do not use markdown.
Do not add explanations before or after the JSON.

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

Resume:

{resume_text}
"""


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


# ---------------------------------------------------------
# PREPARE INPUT
# ---------------------------------------------------------

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
# GENERATE
# ---------------------------------------------------------

print("Analyzing resume...")

with torch.no_grad():

    generated_ids = model.generate(
        **inputs,
        max_new_tokens=400,
        do_sample=False
    )


# ---------------------------------------------------------
# REMOVE INPUT TOKENS
# ---------------------------------------------------------

generated_ids_trimmed = [
    output_ids[len(input_ids):]
    for input_ids, output_ids
    in zip(inputs.input_ids, generated_ids)
]


# ---------------------------------------------------------
# DECODE RESPONSE
# ---------------------------------------------------------

output = processor.batch_decode(
    generated_ids_trimmed,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)


print("\n" + "=" * 60)
print("QWEN RESUME ANALYSIS")
print("=" * 60)

print(output[0])

print("=" * 60)