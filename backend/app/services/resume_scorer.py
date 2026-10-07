import re

from app.services.resume_validator import detect_contact_information


# Common resume headings
SECTION_HEADINGS = [
    "summary",
    "professional summary",
    "profile summary",
    "objective",
    "career objective",
    "education",
    "academic background",
    "educational qualification",
    "skills",
    "technical skills",
    "technical knowledge",
    "experience",
    "work experience",
    "professional experience",
    "projects",
    "academic projects",
    "personal projects",
    "certifications",
    "certificates",
    "achievements",
    "accomplishments"
]


# Common technical and professional skills
SKILL_KEYWORDS = [
    "python",
    "java",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "html",
    "css",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "git",
    "github",
    "docker",
    "linux",
    "fastapi",
    "flask",
    "django",
    "react",
    "node.js",
    "express",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "natural language processing",
    "nlp",
    "computer vision",
    "pytorch",
    "tensorflow",
    "scikit-learn",
    "pandas",
    "numpy",
    "data analysis",
    "data science",
    "power bi",
    "excel",
    "cloud",
    "aws",
    "azure",
    "communication",
    "leadership",
    "problem solving",
    "teamwork"
]


def clean_lines(text: str) -> list:
    """
    Return non-empty cleaned lines from resume text.
    """

    return [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]


def is_heading(line: str) -> bool:
    """
    Check whether a line looks like a resume heading.
    """

    cleaned = re.sub(r"[^a-zA-Z ]", " ", line).strip().lower()
    cleaned = re.sub(r"\s+", " ", cleaned)

    for heading in SECTION_HEADINGS:
        if cleaned == heading:
            return True

    return False


def extract_section(text: str, keywords: list) -> str:
    """
    Extract the text belonging to a resume section.
    """

    lines = clean_lines(text)

    for index, line in enumerate(lines):

        cleaned = re.sub(r"[^a-zA-Z ]", " ", line).strip().lower()
        cleaned = re.sub(r"\s+", " ", cleaned)

        found = False

        for keyword in keywords:
            if cleaned == keyword:
                found = True
                break

        if not found:
            continue

        section_lines = []

        for next_index in range(index + 1, len(lines)):

            if is_heading(lines[next_index]):
                break

            section_lines.append(lines[next_index])

        return " ".join(section_lines).strip()

    return ""


def score_contact_header(text: str) -> dict:
    """
    Score contact information and resume header.

    Maximum score: 10
    """

    score = 0
    improvements = []

    contact_info = detect_contact_information(text)

    # Email = 4 points
    if contact_info["email_found"]:
        score += 4
    else:
        improvements.append(
            "Add a professional email address."
        )

    # Phone = 4 points
    if contact_info["phone_found"]:
        score += 4
    else:
        improvements.append(
            "Add a contact phone number."
        )

    # Name = 2 points
    lines = clean_lines(text)

    if lines:

        first_line = lines[0]

        name_pattern = r"^[A-Za-z]+(?:\s+[A-Za-z]+){1,3}$"

        if re.match(name_pattern, first_line):
            score += 2
        else:
            improvements.append(
                "Add your full name clearly at the top of the resume."
            )

    else:
        improvements.append(
            "Add a clear header with your name."
        )

    return {
        "score": score,
        "max_score": 10,
        "improvements": improvements
    }


def score_summary(text: str) -> dict:
    """
    Score summary or objective section.

    Maximum score: 10
    """

    keywords = [
        "summary",
        "professional summary",
        "profile summary",
        "objective",
        "career objective"
    ]

    summary_text = extract_section(text, keywords)

    score = 0
    improvements = []

    if summary_text:
        score += 5
    else:
        improvements.append(
            "Add a professional summary or career objective."
        )

    word_count = len(summary_text.split())

    if word_count >= 25:
        score += 5
    elif word_count >= 10:
        score += 2
        improvements.append(
            "Expand your summary with more meaningful details."
        )
    elif summary_text:
        improvements.append(
            "Expand your summary with more meaningful details."
        )

    return {
        "score": score,
        "max_score": 10,
        "improvements": improvements
    }


def score_education(text: str) -> dict:
    """
    Score education section.

    Maximum score: 10
    """

    keywords = [
        "education",
        "academic background",
        "educational qualification"
    ]

    education_text = extract_section(text, keywords)

    score = 0
    improvements = []

    if education_text:

        # Section exists
        score += 4

        education_lower = education_text.lower()

        degree_keywords = [
            "b.e",
            "b.tech",
            "bachelor",
            "b.sc",
            "bca",
            "mca",
            "m.e",
            "m.tech",
            "master",
            "degree",
            "diploma",
            "engineering"
        ]

        institution_keywords = [
            "university",
            "college",
            "institute",
            "school"
        ]

        year_pattern = r"\b(?:19|20)\d{2}\b"

        if any(
            keyword in education_lower
            for keyword in degree_keywords
        ):
            score += 2
        else:
            improvements.append(
                "Mention your degree or academic qualification clearly."
            )

        if any(
            keyword in education_lower
            for keyword in institution_keywords
        ):
            score += 2
        else:
            improvements.append(
                "Include your college, university, or institution name."
            )

        if re.search(year_pattern, education_text):
            score += 2
        else:
            improvements.append(
                "Consider adding relevant education years or graduation dates."
            )

    else:
        improvements.append(
            "Add an education section with your academic qualifications."
        )

    return {
        "score": score,
        "max_score": 10,
        "improvements": improvements
    }


def score_skills(text: str) -> dict:
    """
    Score skills section.

    Maximum score: 15
    """

    keywords = [
        "skills",
        "technical skills",
        "technical knowledge"
    ]

    skills_text = extract_section(text, keywords)

    score = 0
    improvements = []

    if not skills_text:
        improvements.append(
            "Add a dedicated skills section."
        )

        return {
            "score": 0,
            "max_score": 15,
            "improvements": improvements
        }

    # Section exists
    score += 5

    skills_lower = skills_text.lower()

    detected_skills = []

    for skill in SKILL_KEYWORDS:
        if skill in skills_lower:
            detected_skills.append(skill)

    skill_count = len(set(detected_skills))

    if skill_count >= 6:
        score += 10
    elif skill_count >= 4:
        score += 7
        improvements.append(
            "Consider adding more relevant technical or professional skills."
        )
    elif skill_count >= 2:
        score += 4
        improvements.append(
            "Add more relevant skills that match your target roles."
        )
    else:
        improvements.append(
            "Add more specific and relevant skills."
        )

    return {
        "score": score,
        "max_score": 15,
        "skills_detected": sorted(set(detected_skills)),
        "improvements": improvements
    }


def score_experience(text: str) -> dict:
    """
    Score experience section.

    Maximum score: 15
    """

    keywords = [
        "experience",
        "work experience",
        "professional experience"
    ]

    experience_text = extract_section(text, keywords)

    score = 0
    improvements = []

    if not experience_text:
        improvements.append(
            "Add work experience, internships, or relevant professional experience."
        )

        return {
            "score": 0,
            "max_score": 15,
            "improvements": improvements
        }

    # Section exists
    score += 5

    experience_lower = experience_text.lower()

    role_keywords = [
        "intern",
        "internship",
        "developer",
        "engineer",
        "analyst",
        "designer",
        "manager",
        "company",
        "worked",
        "responsible",
        "professional"
    ]

    action_keywords = [
        "developed",
        "built",
        "created",
        "implemented",
        "designed",
        "managed",
        "improved",
        "analyzed",
        "maintained",
        "led"
    ]

    year_pattern = r"\b(?:19|20)\d{2}\b"

    if any(
        keyword in experience_lower
        for keyword in role_keywords
    ):
        score += 3
    else:
        improvements.append(
            "Clearly mention your job role, internship, or professional position."
        )

    if any(
        keyword in experience_lower
        for keyword in action_keywords
    ):
        score += 3
    else:
        improvements.append(
            "Use action-oriented descriptions for your experience."
        )

    if re.search(year_pattern, experience_text):
        score += 2
    else:
        improvements.append(
            "Include dates or duration for your experience."
        )

    if len(experience_text.split()) >= 40:
        score += 2
    else:
        improvements.append(
            "Add more detail about your responsibilities and contributions."
        )

    return {
        "score": score,
        "max_score": 15,
        "improvements": improvements
    }


def score_projects(text: str) -> dict:
    """
    Score projects section.

    Maximum score: 15
    """

    keywords = [
        "projects",
        "academic projects",
        "personal projects"
    ]

    project_text = extract_section(text, keywords)

    score = 0
    improvements = []

    if not project_text:
        improvements.append(
            "Add a projects section with relevant projects."
        )

        return {
            "score": 0,
            "max_score": 15,
            "improvements": improvements
        }

    # Section exists
    score += 5

    project_lower = project_text.lower()

    action_keywords = [
        "developed",
        "built",
        "created",
        "implemented",
        "designed",
        "developing",
        "built a",
        "created a"
    ]

    technology_keywords = [
        "python",
        "java",
        "sql",
        "html",
        "css",
        "javascript",
        "react",
        "fastapi",
        "flask",
        "django",
        "machine learning",
        "deep learning",
        "pytorch",
        "tensorflow",
        "mongodb",
        "mysql"
    ]

    if any(
        keyword in project_lower
        for keyword in action_keywords
    ):
        score += 3
    else:
        improvements.append(
            "Describe what you developed, implemented, or achieved in each project."
        )

    if any(
        keyword in project_lower
        for keyword in technology_keywords
    ):
        score += 3
    else:
        improvements.append(
            "Mention the technologies or tools used in your projects."
        )

    if len(project_text.split()) >= 40:
        score += 2
    else:
        improvements.append(
            "Add more technical details and outcomes for your projects."
        )

    if project_text.count("\n") >= 1 or len(project_text.split(".")) >= 2:
        score += 2

    return {
        "score": score,
        "max_score": 15,
        "improvements": improvements
    }


def score_certifications_achievements(text: str) -> dict:
    """
    Score certifications and achievements.

    Maximum score: 10
    """

    certification_keywords = [
        "certifications",
        "certificates"
    ]

    achievement_keywords = [
        "achievements",
        "accomplishments"
    ]

    certification_text = extract_section(
        text,
        certification_keywords
    )

    achievement_text = extract_section(
        text,
        achievement_keywords
    )

    combined_text = (
        certification_text + " " + achievement_text
    ).strip()

    score = 0
    improvements = []

    if certification_text:
        score += 5

    if achievement_text:
        score += 5

    if not certification_text and not achievement_text:
        improvements.append(
            "Add certifications or relevant achievements when available."
        )

    elif len(combined_text.split()) < 10:
        improvements.append(
            "Provide more detail about your certifications or achievements."
        )

    return {
        "score": score,
        "max_score": 10,
        "improvements": improvements
    }


def score_structure_readability(text: str) -> dict:
    """
    Score overall resume structure and readability.

    Maximum score: 15
    """

    score = 0
    improvements = []

    lines = clean_lines(text)
    word_count = len(text.split())

    # Number of detected resume sections
    section_count = 0

    for line in lines:
        if is_heading(line):
            section_count += 1

    # Section organization = 5 points
    if section_count >= 5:
        score += 5
    elif section_count >= 3:
        score += 3
        improvements.append(
            "Consider adding more clearly separated resume sections."
        )
    elif section_count >= 1:
        score += 1
        improvements.append(
            "Organize your resume using clear section headings."
        )
    else:
        improvements.append(
            "Use clear headings to organize your resume."
        )

    # Appropriate content length = 5 points
    if word_count >= 400:
        score += 5
    elif word_count >= 250:
        score += 4
    elif word_count >= 150:
        score += 2
        improvements.append(
            "Add more relevant details to strengthen your resume."
        )
    else:
        improvements.append(
            "Your resume appears too short. Add more relevant information."
        )

    # Basic formatting/list structure = 5 points
    bullet_pattern = r"(?m)^\s*(?:[-•*▪◦])\s+"

    bullet_count = len(
        re.findall(bullet_pattern, text)
    )

    long_lines = sum(
        1 for line in lines
        if len(line) > 250
    )

    if bullet_count >= 3:
        score += 3
    elif bullet_count >= 1:
        score += 2
    else:
        improvements.append(
            "Use bullet points to make responsibilities and achievements easier to read."
        )

    if long_lines == 0:
        score += 2
    else:
        improvements.append(
            "Break very long lines or paragraphs into shorter readable points."
        )

    return {
        "score": min(score, 15),
        "max_score": 15,
        "improvements": improvements
    }


def remove_duplicate_items(items: list) -> list:
    """
    Remove duplicate improvement messages while preserving order.
    """

    unique_items = []

    for item in items:
        if item not in unique_items:
            unique_items.append(item)

    return unique_items


def calculate_resume_score(text: str) -> dict:
    """
    Calculate the complete rule-based resume score.

    Maximum score: 100
    """

    if not text or not text.strip():
        return {
            "score": 0,
            "breakdown": {},
            "improvements": [
                "No readable resume text was available for scoring."
            ]
        }

    contact_header = score_contact_header(text)
    summary = score_summary(text)
    education = score_education(text)
    skills = score_skills(text)
    experience = score_experience(text)
    projects = score_projects(text)
    certifications_achievements = score_certifications_achievements(
        text
    )
    structure = score_structure_readability(text)

    total_score = (
        contact_header["score"]
        + summary["score"]
        + education["score"]
        + skills["score"]
        + experience["score"]
        + projects["score"]
        + certifications_achievements["score"]
        + structure["score"]
    )

    all_improvements = (
        contact_header["improvements"]
        + summary["improvements"]
        + education["improvements"]
        + skills["improvements"]
        + experience["improvements"]
        + projects["improvements"]
        + certifications_achievements["improvements"]
        + structure["improvements"]
    )

    all_improvements = remove_duplicate_items(
        all_improvements
    )

    return {
        "score": min(total_score, 100),

        "breakdown": {
            "contact_header": {
                "score": contact_header["score"],
                "max_score": 10
            },
            "summary": {
                "score": summary["score"],
                "max_score": 10
            },
            "education": {
                "score": education["score"],
                "max_score": 10
            },
            "skills": {
                "score": skills["score"],
                "max_score": 15,
                "skills_detected": skills.get(
                    "skills_detected", []
                )
            },
            "experience": {
                "score": experience["score"],
                "max_score": 15
            },
            "projects": {
                "score": projects["score"],
                "max_score": 15
            },
            "certifications_achievements": {
                "score": certifications_achievements["score"],
                "max_score": 10
            },
            "structure_readability": {
                "score": structure["score"],
                "max_score": 15
            }
        },

        "improvements": all_improvements
    }