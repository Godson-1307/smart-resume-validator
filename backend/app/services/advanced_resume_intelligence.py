import re


# =========================================================
# COMMON PATTERNS
# =========================================================

ACTION_VERBS = [
    "developed",
    "built",
    "created",
    "implemented",
    "designed",
    "deployed",
    "managed",
    "analyzed",
    "improved",
    "optimized",
    "automated",
    "integrated",
    "configured",
    "led",
    "performed",
    "applied",
    "processed",
    "generated",
    "tested",
    "maintained",
    "researched",
    "trained",
    "evaluated",
    "engineered"
]


METRIC_PATTERNS = [
    r"\b\d+(?:\.\d+)?\s*%",
    r"\b\d+(?:\.\d+)?\s*(?:x|times)\b",
    r"\b\d+\+?\s*(?:users|clients|projects|models|records|datasets)\b",
    r"\b(?:increased|improved|reduced|achieved)\b[^.\n]{0,80}",
    r"\b(?:accuracy|precision|recall|f1|score)\b[^.\n]{0,50}"
]


EXPERIENCE_PATTERNS = [
    "intern",
    "internship",
    "work experience",
    "professional experience",
    "employment",
    "freelance",
    "job simulation",
    "virtual job simulation",
    "virtual experience",
    "work simulation",
    "apprenticeship",
    "trainee",
    "research assistant",
    "research intern",
    "volunteer experience"
]


SECTION_NAMES = {
    "summary": [
        "summary",
        "professional summary",
        "profile summary",
        "objective",
        "career objective"
    ],

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
        "certificates",
        "certification"
    ],

    "achievements": [
        "achievements",
        "accomplishments",
        "awards"
    ],

    "interests": [
        "areas of interest",
        "interests"
    ]
}


# =========================================================
# SKILL CATEGORIES
# =========================================================

SKILL_CATEGORIES = {
    "programming": [
        "python",
        "java",
        "c++",
        "c#",
        "javascript",
        "typescript",
        "sql"
    ],

    "ai_machine_learning": [
        "machine learning",
        "deep learning",
        "generative ai",
        "artificial intelligence",
        "natural language processing",
        "nlp",
        "large language models",
        "llm",
        "computer vision",
        "pytorch",
        "tensorflow",
        "scikit-learn",
        "langchain",
        "prompt engineering"
    ],

    "data": [
        "pandas",
        "numpy",
        "matplotlib",
        "mysql",
        "postgresql",
        "mongodb",
        "data analysis",
        "data visualization",
        "statistics"
    ],

    "web": [
        "html",
        "css",
        "javascript",
        "react",
        "node.js",
        "fastapi",
        "flask",
        "django"
    ],

    "cloud_devops": [
        "cloud computing",
        "aws",
        "azure",
        "docker",
        "github actions",
        "github",
        "git",
        "version control",
        "cli"
    ],

    "tools": [
        "vs code",
        "visual studio code",
        "jupyter",
        "jupyter notebook",
        "windows"
    ],

    "soft_skills": [
        "analytical thinking",
        "analytic thinking",
        "problem solving",
        "attention to detail",
        "research skills",
        "written communication",
        "team collaboration",
        "adaptability",
        "leadership"
    ]
}


# =========================================================
# NORMALIZATION
# =========================================================

def normalize_text(text: str) -> str:
    """
    Normalize text for comparisons.
    """

    text = text.lower()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def normalize_heading(line: str) -> str:
    """
    Normalize a possible section heading.
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


def clean_line(line: str) -> str:
    """
    Clean bullet symbols from a line.
    """

    line = line.strip()

    line = re.sub(
        r"^[•●▪◦*-]\s*",
        "",
        line
    )

    return line.strip()


# =========================================================
# SECTION DETECTION
# =========================================================

def detect_sections(text: str) -> dict:
    """
    Detect resume sections and their content.
    """

    sections = {}

    current_section = None

    for raw_line in text.splitlines():

        line = clean_line(raw_line)

        if not line:
            continue

        heading = normalize_heading(line)

        detected_section = None

        for section, aliases in SECTION_NAMES.items():

            if heading in aliases:
                detected_section = section
                break

        if detected_section:

            current_section = detected_section

            if current_section not in sections:
                sections[current_section] = []

            continue

        if current_section:

            sections[current_section].append(line)

    return {
        section: "\n".join(lines).strip()
        for section, lines in sections.items()
    }


# =========================================================
# CONTACT / LINKS
# =========================================================

def analyze_contact_links(text: str) -> dict:
    """
    Detect email, phone, GitHub, LinkedIn and portfolio links.
    """

    email_pattern = (
        r"\b[A-Za-z0-9._%+-]+"
        r"@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    )

    phone_pattern = (
        r"(?:\+91[\s-]?)?[6-9]\d{9}"
    )

    github_pattern = r"(?:github\.com|github)"

    linkedin_pattern = r"(?:linkedin\.com|linkedin)"

    portfolio_pattern = (
        r"(?:portfolio|personal website|"
        r"behance\.net|dribbble\.com)"
    )

    return {
        "email_found": bool(
            re.search(
                email_pattern,
                text,
                flags=re.IGNORECASE
            )
        ),

        "phone_found": bool(
            re.search(
                phone_pattern,
                text
            )
        ),

        "github_found": bool(
            re.search(
                github_pattern,
                text,
                flags=re.IGNORECASE
            )
        ),

        "linkedin_found": bool(
            re.search(
                linkedin_pattern,
                text,
                flags=re.IGNORECASE
            )
        ),

        "portfolio_found": bool(
            re.search(
                portfolio_pattern,
                text,
                flags=re.IGNORECASE
            )
        )
    }


# =========================================================
# EXPERIENCE INTELLIGENCE
# =========================================================

def analyze_experience(text: str) -> dict:
    """
    Detect formal and non-traditional experience evidence.

    This includes internships, job simulations,
    virtual experiences and freelance work.
    """

    lines = [
        clean_line(line)
        for line in text.splitlines()
        if clean_line(line)
    ]

    formal_heading_found = False
    experience_entries = []

    for raw_line in text.splitlines():

        line = clean_line(raw_line)

        if not line:
            continue

        heading = normalize_heading(line)

        if heading in SECTION_NAMES["experience"]:
            formal_heading_found = True

    for line in lines:

        normalized = normalize_text(line)

        for pattern in EXPERIENCE_PATTERNS:

            if pattern in normalized:

                if line not in experience_entries:
                    experience_entries.append(line)

                break

    experience_types = []

    normalized_text = normalize_text(text)

    if (
        "intern" in normalized_text
        or "internship" in normalized_text
    ):
        experience_types.append(
            "internship"
        )

    if (
        "job simulation" in normalized_text
        or "virtual job simulation" in normalized_text
        or "work simulation" in normalized_text
    ):
        experience_types.append(
            "job_simulation"
        )

    if (
        "virtual experience" in normalized_text
        or "virtual internship" in normalized_text
    ):
        experience_types.append(
            "virtual_experience"
        )

    if "freelance" in normalized_text:
        experience_types.append(
            "freelance"
        )

    if "volunteer" in normalized_text:
        experience_types.append(
            "volunteer"
        )

    has_experience_evidence = (
        formal_heading_found
        or bool(experience_entries)
    )

    return {
        "formal_experience_section": formal_heading_found,
        "experience_evidence_found": has_experience_evidence,
        "experience_like_entries": experience_entries[:10],
        "experience_types": sorted(
            set(experience_types)
        )
    }


# =========================================================
# ACHIEVEMENT INTELLIGENCE
# =========================================================

def analyze_achievements(text: str) -> dict:
    """
    Detect action-oriented and measurable achievements.
    """

    lines = [
        clean_line(line)
        for line in text.splitlines()
        if clean_line(line)
    ]

    action_lines = []
    metric_lines = []

    for line in lines:

        normalized = normalize_text(line)

        if any(
            re.search(
                rf"\b{re.escape(verb)}\b",
                normalized
            )
            for verb in ACTION_VERBS
        ):

            action_lines.append(line)

        if any(
            re.search(
                pattern,
                normalized
            )
            for pattern in METRIC_PATTERNS
        ):

            metric_lines.append(line)

    achievement_heading_found = False

    for line in lines:

        if normalize_heading(line) in (
            SECTION_NAMES["achievements"]
        ):

            achievement_heading_found = True

    return {
        "achievement_section_found": (
            achievement_heading_found
        ),

        "action_oriented_lines": action_lines[:10],

        "action_verb_count": len(
            action_lines
        ),

        "quantified_lines": metric_lines[:10],

        "quantified_achievement_count": len(
            metric_lines
        )
    }


# =========================================================
# SKILL INTELLIGENCE
# =========================================================

def analyze_skills(text: str) -> dict:
    """
    Categorize skills found in the resume.
    """

    normalized = normalize_text(
        text
    )

    categories = {}

    all_detected = []

    for category, skills in SKILL_CATEGORIES.items():

        detected = []

        for skill in skills:

            pattern = (
                r"(?<![a-z0-9])"
                + re.escape(
                    skill.lower()
                )
                + r"(?![a-z0-9])"
            )

            if re.search(
                pattern,
                normalized
            ):

                if skill not in detected:
                    detected.append(skill)

                if skill not in all_detected:
                    all_detected.append(skill)

        categories[category] = detected

    technical_count = sum(
        len(
            skills
        )
        for category, skills in categories.items()
        if category != "soft_skills"
    )

    soft_skill_count = len(
        categories.get(
            "soft_skills",
            []
        )
    )

    return {
        "categories": categories,

        "all_detected_skills": sorted(
            set(all_detected)
        ),

        "technical_skill_count": technical_count,

        "soft_skill_count": soft_skill_count,

        "skill_category_count": sum(
            1
            for skills in categories.values()
            if skills
        )
    }


# =========================================================
# EDUCATION INTELLIGENCE
# =========================================================

def analyze_education(
    text: str,
    sections: dict
) -> dict:
    """
    Analyze education details.
    """

    education_text = sections.get(
        "education",
        ""
    )

    normalized = normalize_text(
        education_text
    )

    degree_terms = [
        "b.e",
        "b.tech",
        "bachelor",
        "b.sc",
        "bca",
        "m.e",
        "m.tech",
        "master",
        "degree",
        "diploma",
        "engineering"
    ]

    institution_terms = [
        "university",
        "college",
        "institute",
        "school"
    ]

    year_matches = re.findall(
        r"\b(?:19|20)\d{2}\b",
        education_text
    )

    return {
        "section_found": bool(
            education_text
        ),

        "degree_detected": any(
            term in normalized
            for term in degree_terms
        ),

        "institution_detected": any(
            term in normalized
            for term in institution_terms
        ),

        "years_detected": sorted(
            set(year_matches)
        ),

        "education_entries": [
            clean_line(line)
            for line in education_text.splitlines()
            if clean_line(line)
        ][:10]
    }


# =========================================================
# PROJECT INTELLIGENCE
# =========================================================

def analyze_projects(
    text: str,
    sections: dict
) -> dict:
    """
    Analyze project depth and technical evidence.
    """

    project_text = sections.get(
        "projects",
        ""
    )

    normalized = normalize_text(
        project_text
    )

    technologies = []

    technology_terms = [
        "python",
        "c++",
        "java",
        "sql",
        "machine learning",
        "deep learning",
        "generative ai",
        "pytorch",
        "tensorflow",
        "pandas",
        "numpy",
        "scikit-learn",
        "langchain",
        "fastapi",
        "html",
        "css",
        "javascript",
        "mysql",
        "mongodb",
        "github",
        "github actions",
        "cloud computing"
    ]

    for technology in technology_terms:

        if technology in normalized:
            technologies.append(
                technology
            )

    action_count = 0

    for verb in ACTION_VERBS:

        matches = re.findall(
            rf"\b{re.escape(verb)}\b",
            normalized
        )

        action_count += len(
            matches
        )

    metric_count = sum(
        len(
            re.findall(
                pattern,
                normalized
            )
        )
        for pattern in METRIC_PATTERNS
    )

    return {
        "section_found": bool(
            project_text
        ),

        "technologies_detected": sorted(
            set(technologies)
        ),

        "technology_count": len(
            set(technologies)
        ),

        "action_verb_count": action_count,

        "metric_count": metric_count,

        "project_word_count": len(
            project_text.split()
        )
    }


# =========================================================
# STRUCTURE INTELLIGENCE
# =========================================================

def analyze_structure(
    text: str,
    sections: dict
) -> dict:
    """
    Analyze resume organization and readability.
    """

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    word_count = len(
        text.split()
    )

    bullet_count = len(
        re.findall(
            r"(?m)^\s*[•●▪◦*-]\s+",
            text
        )
    )

    long_lines = [
        line
        for line in lines
        if len(line) > 250
    ]

    expected_core_sections = [
        "summary",
        "education",
        "skills",
        "projects"
    ]

    present_core_sections = [
        section
        for section in expected_core_sections
        if section in sections
        and sections[section].strip()
    ]

    missing_core_sections = [
        section
        for section in expected_core_sections
        if section not in present_core_sections
    ]

    return {
        "word_count": word_count,

        "line_count": len(lines),

        "bullet_count": bullet_count,

        "detected_section_count": len(
            sections
        ),

        "present_core_sections": (
            present_core_sections
        ),

        "missing_core_sections": (
            missing_core_sections
        ),

        "long_line_count": len(
            long_lines
        )
    }


# =========================================================
# QUALITY FLAGS
# =========================================================

def generate_quality_flags(
    text: str,
    contact: dict,
    experience: dict,
    achievements: dict,
    skills: dict,
    projects: dict,
    structure: dict
) -> list:
    """
    Generate important quality flags.
    """

    flags = []

    # Contact
    if not contact["email_found"]:
        flags.append(
            "Missing email address."
        )

    if not contact["phone_found"]:
        flags.append(
            "Missing phone number."
        )

    # Online presence
    if not contact["linkedin_found"]:
        flags.append(
            "LinkedIn profile was not detected."
        )

    if not contact["github_found"]:
        flags.append(
            "GitHub profile was not detected."
        )

    # Experience
    if not experience[
        "experience_evidence_found"
    ]:

        flags.append(
            "No clear professional or experience-like evidence was detected."
        )

    elif (
        not experience["formal_experience_section"]
        and experience["experience_evidence_found"]
    ):

        flags.append(
            "Experience-like evidence exists but is not organized under a clear experience section."
        )

    # Achievements
    if achievements[
        "quantified_achievement_count"
    ] == 0:

        flags.append(
            "Few or no quantified results were detected."
        )

    # Skills
    if skills[
        "technical_skill_count"
    ] < 4:

        flags.append(
            "Limited number of recognizable technical skills detected."
        )

    if skills[
        "skill_category_count"
    ] < 2:

        flags.append(
            "Skills could be organized into clearer categories."
        )

    # Projects
    if projects[
        "section_found"
    ] and projects[
        "technology_count"
    ] == 0:

        flags.append(
            "Projects do not clearly mention technologies used."
        )

    # Structure
    if structure[
        "bullet_count"
    ] == 0:

        flags.append(
            "No bullet points were detected."
        )

    if structure[
        "long_line_count"
    ] > 0:

        flags.append(
            "Some lines are unusually long and may reduce readability."
        )

    return flags


# =========================================================
# STRENGTHS
# =========================================================

def generate_strengths(
    contact: dict,
    experience: dict,
    achievements: dict,
    skills: dict,
    projects: dict,
    structure: dict
) -> list:
    """
    Generate evidence-based resume strengths.
    """

    strengths = []

    if contact["email_found"]:
        strengths.append(
            "Contact information includes an email address."
        )

    if contact["phone_found"]:
        strengths.append(
            "Contact information includes a phone number."
        )

    if skills[
        "technical_skill_count"
    ] >= 8:

        strengths.append(
            "The resume demonstrates a broad technical skill set."
        )

    if skills[
        "skill_category_count"
    ] >= 3:

        strengths.append(
            "Skills span multiple technical areas."
        )

    if projects[
        "technology_count"
    ] >= 4:

        strengths.append(
            "Projects demonstrate practical use of multiple technologies."
        )

    if achievements[
        "quantified_achievement_count"
    ] > 0:

        strengths.append(
            "The resume includes measurable results or performance indicators."
        )

    if experience[
        "experience_types"
    ]:

        strengths.append(
            "The resume contains practical experience-like evidence."
        )

    if structure[
        "detected_section_count"
    ] >= 5:

        strengths.append(
            "The resume is organized into multiple recognizable sections."
        )

    return strengths[:6]


# =========================================================
# ADVANCED IMPROVEMENTS
# =========================================================

def generate_advanced_improvements(
    contact: dict,
    experience: dict,
    achievements: dict,
    skills: dict,
    projects: dict,
    structure: dict
) -> list:
    """
    Generate advanced and actionable improvements.
    """

    improvements = []

    if not contact["linkedin_found"]:
        improvements.append(
            "Add a LinkedIn profile link to strengthen your professional presence."
        )

    if not contact["github_found"]:
        improvements.append(
            "Add a GitHub profile or relevant project repository links when applicable."
        )

    if (
        experience["experience_evidence_found"]
        and not experience["formal_experience_section"]
    ):

        improvements.append(
            "Move job simulations, internships, or virtual experiences into a clearly labeled Experience section."
        )

    if (
        achievements["quantified_achievement_count"]
        == 0
    ):

        improvements.append(
            "Add measurable outcomes to projects or experience, such as accuracy, scale, time saved, or users affected."
        )

    if (
        achievements["action_verb_count"]
        < 3
    ):

        improvements.append(
            "Use stronger action verbs such as developed, implemented, optimized, automated, and analyzed."
        )

    if (
        skills["skill_category_count"]
        < 3
    ):

        improvements.append(
            "Group skills into categories such as Programming, AI/ML, Data, Cloud, and Tools."
        )

    if (
        projects["section_found"]
        and projects["technology_count"] < 3
    ):

        improvements.append(
            "Mention the key technologies used in each project."
        )

    if (
        projects["section_found"]
        and projects["action_verb_count"] < 2
    ):

        improvements.append(
            "Describe your personal contribution to each project using action-oriented bullet points."
        )

    if (
        structure["bullet_count"] < 3
    ):

        improvements.append(
            "Use concise bullet points for project, experience, and achievement descriptions."
        )

    return improvements[:8]


# =========================================================
# MAIN ANALYSIS
# =========================================================

def analyze_advanced_resume_intelligence(
    text: str
) -> dict:
    """
    Run the complete advanced resume intelligence analysis.
    """

    if not text or not text.strip():

        raise ValueError(
            "No resume text was provided."
        )

    sections = detect_sections(
        text
    )

    contact = analyze_contact_links(
        text
    )

    experience = analyze_experience(
        text
    )

    achievements = analyze_achievements(
        text
    )

    skills = analyze_skills(
        text
    )

    education = analyze_education(
        text,
        sections
    )

    projects = analyze_projects(
        text,
        sections
    )

    structure = analyze_structure(
        text,
        sections
    )

    quality_flags = generate_quality_flags(
        text=text,
        contact=contact,
        experience=experience,
        achievements=achievements,
        skills=skills,
        projects=projects,
        structure=structure
    )

    strengths = generate_strengths(
        contact=contact,
        experience=experience,
        achievements=achievements,
        skills=skills,
        projects=projects,
        structure=structure
    )

    improvements = generate_advanced_improvements(
        contact=contact,
        experience=experience,
        achievements=achievements,
        skills=skills,
        projects=projects,
        structure=structure
    )

    return {
        "contact_analysis": contact,

        "experience_analysis": experience,

        "achievement_analysis": achievements,

        "skill_analysis": skills,

        "education_analysis": education,

        "project_analysis": projects,

        "structure_analysis": structure,

        "quality_flags": quality_flags,

        "strengths": strengths,

        "advanced_improvements": improvements
    }