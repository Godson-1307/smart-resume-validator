import re

import torch

from transformers import (
    Qwen2VLForConditionalGeneration,
    AutoProcessor
)


MODEL_NAME = "Qwen/Qwen2-VL-2B-Instruct"


# =========================================================
# MODEL CACHE
# =========================================================

_model = None
_processor = None


def get_qwen_model():
    """
    Load Qwen once and reuse it.
    """

    global _model
    global _processor

    if _model is None or _processor is None:

        print("Loading Qwen model...")

        _model = Qwen2VLForConditionalGeneration.from_pretrained(
            MODEL_NAME,
            torch_dtype="auto",
            device_map="auto"
        )

        _processor = AutoProcessor.from_pretrained(
            MODEL_NAME
        )

        print("Qwen model loaded successfully.")

    return _model, _processor


# =========================================================
# TEXT UTILITIES
# =========================================================

def normalize_text(text: str) -> str:
    """
    Normalize text for comparison.
    """

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def clean_line(line: str) -> str:
    """
    Clean a single extracted line.
    """

    line = line.strip()

    line = re.sub(
        r"^[•●▪◦*-]\s*",
        "",
        line
    )

    return line.strip()


# =========================================================
# SOURCE CONTACT EXTRACTION
# =========================================================

def extract_email_from_source(text: str) -> str:
    """
    Extract email directly from the original resume text.
    """

    pattern = (
        r"\b[A-Za-z0-9._%+-]+"
        r"@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    )

    match = re.search(
        pattern,
        text
    )

    if match:
        return match.group(0)

    return ""


def extract_phone_from_source(text: str) -> str:
    """
    Extract a likely Indian phone number.
    """

    patterns = [
        r"\+91[\s-]?[6-9]\d{9}",
        r"\b[6-9]\d{9}\b"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text
        )

        if match:
            return match.group(0)

    return ""


def extract_name_from_source(text: str) -> str:
    """
    Extract a likely candidate name from the first
    suitable lines of the resume.
    """

    ignored = {
        "resume",
        "curriculum vitae",
        "cv",
        "professional summary",
        "summary",
        "technical skills",
        "skills",
        "projects",
        "education",
        "certifications",
        "experience"
    }

    for line in text.splitlines():

        line = clean_line(line)

        if not line:
            continue

        if "@" in line:
            continue

        if re.search(
            r"\d{7,}",
            line
        ):
            continue

        normalized = normalize_text(line)

        if normalized in ignored:
            continue

        # Avoid obvious section descriptions
        if len(line.split()) > 5:
            continue

        # Reasonable name pattern
        if re.match(
            r"^[A-Za-z]+(?:[\s'-]+[A-Za-z]+){1,4}$",
            line
        ):
            return line

    return ""


# =========================================================
# SECTION DETECTION
# =========================================================

SECTION_ALIASES = {
    "summary": [
        "professional summary",
        "profile summary",
        "summary",
        "objective",
        "career objective"
    ],

    "skills": [
        "technical skills",
        "skills",
        "technical knowledge"
    ],

    "projects": [
        "projects",
        "academic projects",
        "personal projects"
    ],

    "education": [
        "education",
        "academic background",
        "educational qualification"
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience"
    ],

    "certifications": [
        "certifications",
        "certificates",
        "certification"
    ]
}


def normalize_heading(line: str) -> str:
    """
    Normalize a line for heading comparison.
    """

    line = line.strip().lower()

    line = re.sub(
        r"[:\-|]+$",
        "",
        line
    )

    line = re.sub(
        r"\s+",
        " ",
        line
    )

    return line.strip()


def get_section_name(line: str):
    """
    Return the logical section name if the line
    looks like a known resume heading.
    """

    normalized = normalize_heading(line)

    for section, aliases in SECTION_ALIASES.items():

        for alias in aliases:

            if normalized == alias:
                return section

    return None


def extract_sections(text: str) -> dict:
    """
    Split resume text into logical sections.
    """

    sections = {}

    current_section = None

    for raw_line in text.splitlines():

        line = clean_line(raw_line)

        if not line:
            continue

        detected_section = get_section_name(line)

        if detected_section:

            current_section = detected_section

            if current_section not in sections:
                sections[current_section] = []

            continue

        if current_section:

            sections[current_section].append(line)

    result = {}

    for section, lines in sections.items():

        result[section] = "\n".join(lines).strip()

    return result


# =========================================================
# SKILL EXTRACTION
# =========================================================

SKILL_PATTERNS = {
    "Python": [
        "python"
    ],

    "C++": [
        "c++"
    ],

    "Java": [
        "java"
    ],

    "SQL": [
        "sql"
    ],

    "Machine Learning": [
        "machine learning",
        "machine-learning"
    ],

    "Deep Learning": [
        "deep learning",
        "deep-learning"
    ],

    "Generative AI": [
        "generative ai",
        "generational ai"
    ],

    "Large Language Models": [
        "large language models",
        "large language model",
        "llms",
        "llm"
    ],

    "Prompt Engineering": [
        "prompt engineering"
    ],

    "Natural Language Processing": [
        "natural language processing",
        "nlp",
        "npl"
    ],

    "LangChain": [
        "langchain"
    ],

    "Pandas": [
        "pandas"
    ],

    "NumPy": [
        "numpy"
    ],

    "Scikit-learn": [
        "scikit-learn",
        "scikit learn",
        "scikitlearn"
    ],

    "Matplotlib": [
        "matplotlib"
    ],

    "GitHub": [
        "github"
    ],

    "GitHub Actions": [
        "github actions"
    ],

    "Git": [
        "git"
    ],

    "VS Code": [
        "vs code",
        "visual studio code"
    ],

    "Jupyter Notebook": [
        "jupyter notebook",
        "jupyter"
    ],

    "Cloud Computing": [
        "cloud computing"
    ],

    "Version Control": [
        "version control"
    ],

    "CLI": [
        "cli"
    ],

    "Windows": [
        "windows"
    ],

    "MySQL": [
        "mysql"
    ],

    "HTML": [
        "html"
    ],

    "CSS": [
        "css"
    ],

    "JavaScript": [
        "javascript"
    ],

    "Computer Vision": [
        "computer vision"
    ],

    "Analytical Thinking": [
        "analytical thinking",
        "analytic thinking"
    ],

    "Problem Solving": [
        "problem solving"
    ],

    "Attention to Detail": [
        "attention to detail",
        "attention-to-detail"
    ],

    "Research Skills": [
        "research skills"
    ],

    "Written Communication": [
        "written communication"
    ],

    "Team Collaboration": [
        "team collaboration"
    ],

    "Adaptability": [
        "adaptability",
        "continuous learning"
    ]
}


def contains_skill(
    text: str,
    pattern: str
) -> bool:
    """
    Check whether a skill is present.
    """

    text_lower = text.lower()
    pattern_lower = pattern.lower()

    regex = (
        r"(?<![a-z0-9])"
        + re.escape(pattern_lower)
        + r"(?![a-z0-9])"
    )

    return re.search(
        regex,
        text_lower
    ) is not None


def extract_skills_from_source(
    text: str
) -> list:
    """
    Extract skills from the original resume text.
    """

    skills = []

    for skill, patterns in SKILL_PATTERNS.items():

        for pattern in patterns:

            if contains_skill(
                text,
                pattern
            ):

                if skill not in skills:
                    skills.append(skill)

                break

    return skills


# =========================================================
# LIST EXTRACTION FROM SECTIONS
# =========================================================

def extract_section_items(
    section_text: str,
    max_items: int
) -> list:
    """
    Convert section text into a list of readable items.
    """

    if not section_text:
        return []

    lines = section_text.splitlines()

    items = []

    for line in lines:

        line = clean_line(line)

        if not line:
            continue

        # Skip very short fragments
        if len(line) < 3:
            continue

        if line not in items:
            items.append(line)

        if len(items) >= max_items:
            break

    return items


def extract_projects_from_source(
    section_text: str
) -> list:
    """
    Extract project names from the project section.
    """

    if not section_text:
        return []

    lines = section_text.splitlines()

    projects = []

    skip_words = {
        "semester",
        "developed",
        "built",
        "created",
        "implemented",
        "used",
        "performed",
        "applied",
        "code source"
    }

    for line in lines:

        line = clean_line(line)

        if not line:
            continue

        normalized = normalize_text(line)

        if normalized.startswith(
            "semester"
        ):
            continue

        if normalized.startswith(
            "january"
        ):
            continue

        if normalized.startswith(
            "february"
        ):
            continue

        if normalized.startswith(
            "march"
        ):
            continue

        if normalized.startswith(
            "april"
        ):
            continue

        if normalized.startswith(
            "may"
        ):
            continue

        if normalized.startswith(
            "june"
        ):
            continue

        if normalized.startswith(
            "july"
        ):
            continue

        if normalized.startswith(
            "august"
        ):
            continue

        if normalized.startswith(
            "september"
        ):
            continue

        if normalized.startswith(
            "october"
        ):
            continue

        if normalized.startswith(
            "november"
        ):
            continue

        if normalized.startswith(
            "december"
        ):
            continue

        if any(
            normalized.startswith(word)
            for word in skip_words
        ):
            continue

        # Ignore very long description lines
        if len(line.split()) > 12:
            continue

        if line not in projects:
            projects.append(line)

        if len(projects) >= 5:
            break

    return projects


# =========================================================
# QWEN GENERATION
# =========================================================

def generate_qwen_response(
    model,
    processor,
    prompt: str,
    max_new_tokens: int = 300
) -> str:
    """
    Generate a Qwen response.
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

    inputs = processor.apply_chat_template(
        messages,
        tokenize=True,
        return_dict=True,
        return_tensors="pt"
    )

    inputs = inputs.to(model.device)

    with torch.no_grad():

        generated_ids = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.01,
            top_p=0.001,
            top_k=1,
            repetition_penalty=1.0,
            no_repeat_ngram_size=4,
            use_cache=True
        )

    input_length = inputs[
        "input_ids"
    ].shape[1]

    generated_ids = generated_ids[
        :,
        input_length:
    ]

    output = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False
    )

    if output:
        return output[0].strip()

    return ""


# =========================================================
# QWEN TAG PARSER
# =========================================================

def extract_tag(
    text: str,
    tag: str
) -> str:
    """
    Extract content from a tag.
    """

    pattern = rf"<{tag}>(.*?)</{tag}>"

    match = re.search(
        pattern,
        text,
        flags=re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return ""


def extract_list_tag(
    text: str,
    tag: str
) -> list:
    """
    Extract pipe-separated values from a tag.
    """

    value = extract_tag(
        text,
        tag
    )

    if not value:
        return []

    items = []

    for item in value.split("|"):

        item = clean_line(item)

        if item and item not in items:
            items.append(item)

    return items


def parse_qwen_tags(
    response: str
) -> dict:
    """
    Parse Qwen's tagged output.
    """

    return {
        "name": extract_tag(
            response,
            "NAME"
        ),

        "email": extract_tag(
            response,
            "EMAIL"
        ),

        "phone": extract_tag(
            response,
            "PHONE"
        ),

        "skills": extract_list_tag(
            response,
            "SKILLS"
        ),

        "education": extract_list_tag(
            response,
            "EDUCATION"
        ),

        "experience": extract_list_tag(
            response,
            "EXPERIENCE"
        ),

        "projects": extract_list_tag(
            response,
            "PROJECTS"
        ),

        "certifications": extract_list_tag(
            response,
            "CERTIFICATIONS"
        )
    }


# =========================================================
# BUILD SOURCE-BASED RESULT
# =========================================================

def build_source_result(
    resume_text: str
) -> dict:
    """
    Build reliable structured information directly
    from the extracted resume text.

    This is the fallback whenever Qwen does not
    follow the requested format.
    """

    sections = extract_sections(
        resume_text
    )

    name = extract_name_from_source(
        resume_text
    )

    email = extract_email_from_source(
        resume_text
    )

    phone = extract_phone_from_source(
        resume_text
    )

    skills = extract_skills_from_source(
        resume_text
    )

    education = extract_section_items(
        sections.get(
            "education",
            ""
        ),
        5
    )

    experience = extract_section_items(
        sections.get(
            "experience",
            ""
        ),
        5
    )

    projects = extract_projects_from_source(
        sections.get(
            "projects",
            ""
        )
    )

    certifications = extract_section_items(
        sections.get(
            "certifications",
            ""
        ),
        5
    )

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,
        "education": education,
        "experience": experience,
        "projects": projects,
        "certifications": certifications
    }


# =========================================================
# MERGE QWEN + SOURCE
# =========================================================

def merge_qwen_with_source(
    qwen_data: dict,
    source_data: dict,
    source_text: str
) -> dict:
    """
    Merge Qwen output with source-verified information.

    Source information wins whenever Qwen is empty
    or produces information that is not present
    in the original resume.
    """

    result = {}

    # -----------------------------------------------------
    # Identity
    # -----------------------------------------------------

    result["name"] = qwen_data.get(
        "name",
        ""
    ).strip()

    if (
        not result["name"]
        or normalize_text(result["name"])
        not in normalize_text(source_text)
    ):
        result["name"] = source_data["name"]

    result["email"] = qwen_data.get(
        "email",
        ""
    ).strip()

    if (
        not result["email"]
        or result["email"].lower()
        not in source_text.lower()
    ):
        result["email"] = source_data["email"]

    result["phone"] = qwen_data.get(
        "phone",
        ""
    ).strip()

    source_digits = re.sub(
        r"\D",
        "",
        source_data["phone"]
    )

    qwen_digits = re.sub(
        r"\D",
        "",
        result["phone"]
    )

    if (
        not qwen_digits
        or qwen_digits != source_digits
    ):
        result["phone"] = source_data["phone"]

    # -----------------------------------------------------
    # Skills
    # -----------------------------------------------------

    qwen_skills = qwen_data.get(
        "skills",
        []
    )

    verified_qwen_skills = []

    for skill in qwen_skills:

        if not isinstance(
            skill,
            str
        ):
            continue

        if contains_skill(
            source_text,
            skill
        ):

            if skill not in verified_qwen_skills:
                verified_qwen_skills.append(skill)

    # Use source detection when Qwen fails
    if verified_qwen_skills:

        result["skills"] = verified_qwen_skills

    else:

        result["skills"] = source_data["skills"]

    # -----------------------------------------------------
    # Other sections
    # -----------------------------------------------------

    for field in [
        "education",
        "experience",
        "projects",
        "certifications"
    ]:

        qwen_items = qwen_data.get(
            field,
            []
        )

        valid_items = []

        for item in qwen_items:

            if not isinstance(
                item,
                str
            ):
                continue

            if not item.strip():
                continue

            if normalize_text(item) in normalize_text(
                source_text
            ):

                if item not in valid_items:
                    valid_items.append(item)

        if valid_items:

            result[field] = valid_items

        else:

            result[field] = source_data[field]

    return result


# =========================================================
# FINAL STRUCTURE VALIDATION
# =========================================================

def validate_resume_data(
    data: dict
) -> bool:
    """
    Validate the final application structure.
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

    if not isinstance(
        data,
        dict
    ):
        return False

    if set(data.keys()) != required_keys:
        return False

    for field in [
        "name",
        "email",
        "phone"
    ]:

        if not isinstance(
            data[field],
            str
        ):
            return False

    for field in [
        "skills",
        "education",
        "experience",
        "projects",
        "certifications"
    ]:

        if not isinstance(
            data[field],
            list
        ):
            return False

    return True


# =========================================================
# MAIN FUNCTION
# =========================================================

def extract_resume_information(
    text: str
) -> dict:
    """
    Extract structured resume information.

    Qwen is attempted first.
    If Qwen does not follow the requested format,
    source-based extraction is used as a safe fallback.
    """

    if not text or not text.strip():

        raise ValueError(
            "No resume text was provided."
        )

    model, processor = get_qwen_model()

    resume_text = re.sub(
        r"\n\s*\n+",
        "\n\n",
        text
    ).strip()

    # -----------------------------------------------------
    # SOURCE-BASED BASELINE
    # -----------------------------------------------------

    source_data = build_source_result(
        resume_text
    )

    # -----------------------------------------------------
    # QWEN PROMPT
    # -----------------------------------------------------

    prompt = f"""
Extract information from this resume.

Return ONLY these eight lines:

<NAME>name</NAME>
<EMAIL>email</EMAIL>
<PHONE>phone</PHONE>
<SKILLS>skill1 | skill2 | skill3</SKILLS>
<EDUCATION>education1 | education2</EDUCATION>
<EXPERIENCE>experience1 | experience2</EXPERIENCE>
<PROJECTS>project1 | project2</PROJECTS>
<CERTIFICATIONS>certification1 | certification2</CERTIFICATIONS>

Important:
- Do not repeat the resume.
- Do not explain anything.
- Do not use JSON.
- Do not use markdown.
- Do not create other tags.
- Do not invent information.
- Keep missing fields empty.
- Stop immediately after the certifications tag.

Resume:

{resume_text}
"""

    print(
        "Running Qwen resume extraction..."
    )

    try:

        raw_output = generate_qwen_response(
            model,
            processor,
            prompt,
            max_new_tokens=300
        )

    except Exception as error:

        print(
            "Qwen generation failed:",
            error
        )

        raw_output = ""

    print("\n" + "=" * 60)
    print("QWEN RAW OUTPUT")
    print("=" * 60)
    print(raw_output)
    print("=" * 60)

    # -----------------------------------------------------
    # PARSE QWEN
    # -----------------------------------------------------

    qwen_data = parse_qwen_tags(
        raw_output
    )

    qwen_has_structure = (
        bool(qwen_data["name"])
        or bool(qwen_data["email"])
        or bool(qwen_data["phone"])
        or bool(qwen_data["skills"])
        or bool(qwen_data["education"])
        or bool(qwen_data["experience"])
        or bool(qwen_data["projects"])
        or bool(qwen_data["certifications"])
    )

    # -----------------------------------------------------
    # MERGE
    # -----------------------------------------------------

    if qwen_has_structure:

        final_data = merge_qwen_with_source(
            qwen_data,
            source_data,
            resume_text
        )

        print(
            "Qwen extraction used with source verification."
        )

    else:

        final_data = source_data

        print(
            "Qwen did not follow the extraction format."
        )

        print(
            "Using source-based extraction fallback."
        )

    # -----------------------------------------------------
    # FINAL VALIDATION
    # -----------------------------------------------------

    if not validate_resume_data(
        final_data
    ):

        raise ValueError(
            "Resume extraction produced an invalid data structure."
        )

    return final_data