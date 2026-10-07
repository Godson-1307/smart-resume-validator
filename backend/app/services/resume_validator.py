import re


def detect_contact_information(text: str) -> dict:
    """
    Detect basic contact information in the resume text.
    """

    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

    phone_pattern = r"\b(?:\+91[\s-]?)?[6-9]\d{9}\b"

    email_found = re.search(email_pattern, text)
    phone_found = re.search(phone_pattern, text)

    return {
        "email_found": bool(email_found),
        "phone_found": bool(phone_found)
    }


def detect_resume_sections(text: str) -> list:
    """
    Detect common resume sections in the extracted text.
    """

    section_keywords = {
        "education": [
            "education",
            "academic background",
            "educational qualification"
        ],
        "skills": [
            "skills",
            "technical skills",
            "technical knowledge"
        ],
        "experience": [
            "experience",
            "work experience",
            "professional experience"
        ],
        "projects": [
            "projects",
            "academic projects",
            "personal projects"
        ],
        "certifications": [
            "certifications",
            "certificates"
        ],
        "summary": [
            "summary",
            "professional summary",
            "profile summary"
        ],
        "objective": [
            "objective",
            "career objective"
        ],
        "achievements": [
            "achievements",
            "accomplishments"
        ]
    }

    text_lower = text.lower()

    detected_sections = []

    for section, keywords in section_keywords.items():
        for keyword in keywords:
            if keyword in text_lower:
                detected_sections.append(section)
                break

    return detected_sections


def calculate_validation_confidence(
    contact_info: dict,
    sections: list,
    content: dict
) -> int:
    """
    Calculate validation confidence using
    contact, section and content signals.
    """

    points = 0

    # Contact information
    if contact_info["email_found"]:
        points += 1

    if contact_info["phone_found"]:
        points += 1

    # Resume sections
    points += len(sections)

    # Stronger content evidence
    if content["education_content_found"]:
        points += 2

    if content["skills_content_found"]:
        points += 2

    if content["experience_content_found"]:
        points += 2

    if content["projects_content_found"]:
        points += 2

    # Convert points into a percentage
    confidence = min(points * 5, 100)

    return confidence


def detect_resume_content(text: str) -> dict:
    """
    Detect common content patterns found in resumes.
    """

    text_lower = text.lower()

    education_keywords = [
        "b.e.",
        "b.tech",
        "bachelor",
        "degree",
        "university",
        "college",
        "engineering",
        "education"
    ]

    skill_keywords = [
        "python",
        "java",
        "sql",
        "javascript",
        "html",
        "css",
        "machine learning",
        "deep learning",
        "c++",
        "c#"
    ]

    experience_keywords = [
        "intern",
        "internship",
        "developer",
        "engineer",
        "company",
        "worked",
        "professional experience"
    ]

    project_keywords = [
        "project",
        "developed",
        "built",
        "created",
        "implemented"
    ]

    education_found = any(
        keyword in text_lower
        for keyword in education_keywords
    )

    skills_found = any(
        keyword in text_lower
        for keyword in skill_keywords
    )

    experience_found = any(
        keyword in text_lower
        for keyword in experience_keywords
    )

    projects_found = any(
        keyword in text_lower
        for keyword in project_keywords
    )

    return {
        "education_content_found": education_found,
        "skills_content_found": skills_found,
        "experience_content_found": experience_found,
        "projects_content_found": projects_found
    }


def validate_resume(text: str) -> dict:
    """
    Check whether the extracted document text
    looks like a resume.
    """

    if not text:
        return {
            "is_resume": False,
            "confidence": 0,
            "reasons": ["No text was available for validation."]
        }

    contact_info = detect_contact_information(text)

    sections = detect_resume_sections(text)

    content = detect_resume_content(text)

    confidence = calculate_validation_confidence(
        contact_info,
        sections,
        content
    )

    reasons = []

    if contact_info["email_found"]:
        reasons.append("Email address detected.")

    if contact_info["phone_found"]:
        reasons.append("Phone number detected.")

    for section in sections:
        reasons.append(
            f"{section.capitalize()} section detected."
        )

    if content["education_content_found"]:
        reasons.append("Education-related content detected.")

    if content["skills_content_found"]:
        reasons.append("Skills-related content detected.")

    if content["experience_content_found"]:
        reasons.append("Experience-related content detected.")

    if content["projects_content_found"]:
        reasons.append("Project-related content detected.")

    is_resume = confidence >= 50

    if is_resume:
        message = "The document appears to be a resume."
    else:
        message = "The document does not appear to be a resume."

    return {
        "is_resume": is_resume,
        "confidence": confidence,
        "reasons": reasons,
        "message": message
    }