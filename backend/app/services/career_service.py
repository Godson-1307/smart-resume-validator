import re

from app.services.resume_scorer import SKILL_KEYWORDS


# ---------------------------------------------------------
# ROLE CATALOG
# ---------------------------------------------------------
# These are baseline skill requirements used by our system.
# They can be expanded later as the project grows.
# ---------------------------------------------------------

ROLE_REQUIREMENTS = {
    "Machine Learning Engineer": [
        "python",
        "machine learning",
        "pytorch",
        "tensorflow",
        "scikit-learn",
        "sql",
        "pandas",
        "numpy",
        "git",
        "docker"
    ],

    "Data Scientist": [
        "python",
        "sql",
        "pandas",
        "numpy",
        "machine learning",
        "scikit-learn",
        "statistics",
        "data analysis",
        "data visualization",
        "git"
    ],

    "Data Analyst": [
        "sql",
        "excel",
        "python",
        "pandas",
        "numpy",
        "data analysis",
        "statistics",
        "power bi",
        "data visualization"
    ],

    "AI Engineer": [
        "python",
        "machine learning",
        "deep learning",
        "pytorch",
        "tensorflow",
        "artificial intelligence",
        "transformers",
        "git",
        "docker"
    ],

    "NLP Engineer": [
        "python",
        "machine learning",
        "deep learning",
        "natural language processing",
        "pytorch",
        "tensorflow",
        "transformers",
        "git",
        "docker"
    ],

    "Computer Vision Engineer": [
        "python",
        "machine learning",
        "deep learning",
        "computer vision",
        "opencv",
        "pytorch",
        "tensorflow",
        "numpy",
        "git",
        "docker"
    ],

    "Software Developer": [
        "python",
        "java",
        "c++",
        "sql",
        "git",
        "github",
        "data structures",
        "algorithms",
        "problem solving"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "sql",
        "git",
        "github"
    ],

    "Backend Developer": [
        "python",
        "fastapi",
        "flask",
        "django",
        "sql",
        "postgresql",
        "mongodb",
        "git",
        "docker",
        "rest api"
    ],

    "Frontend Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "git",
        "github"
    ]
}


# ---------------------------------------------------------
# ROLE ALIASES
# ---------------------------------------------------------

ROLE_ALIASES = {
    "Machine Learning Engineer": [
        "machine learning engineer",
        "ml engineer",
        "machine learning developer"
    ],

    "Data Scientist": [
        "data scientist",
        "data science"
    ],

    "Data Analyst": [
        "data analyst",
        "data analytics"
    ],

    "AI Engineer": [
        "ai engineer",
        "artificial intelligence engineer"
    ],

    "NLP Engineer": [
        "nlp engineer",
        "natural language processing engineer"
    ],

    "Computer Vision Engineer": [
        "computer vision engineer",
        "computer vision developer"
    ],

    "Software Developer": [
        "software developer",
        "software engineer",
        "software development"
    ],

    "Web Developer": [
        "web developer",
        "web development"
    ],

    "Backend Developer": [
        "backend developer",
        "back end developer",
        "backend engineer"
    ],

    "Frontend Developer": [
        "frontend developer",
        "front end developer",
        "frontend engineer"
    ]
}


# ---------------------------------------------------------
# EXTENDED SKILL LIST
# ---------------------------------------------------------

EXTRA_SKILLS = [
    "statistics",
    "data visualization",
    "data structures",
    "algorithms",
    "transformers",
    "rest api",
    "opencv"
]


# Create a skill-pattern dictionary.
SKILL_PATTERNS = {
    skill: [skill]
    for skill in SKILL_KEYWORDS
}

for skill in EXTRA_SKILLS:
    SKILL_PATTERNS[skill] = [skill]


# Add common abbreviations / alternatives.
SKILL_PATTERNS["machine learning"] = [
    "machine learning",
    "ml"
]

SKILL_PATTERNS["artificial intelligence"] = [
    "artificial intelligence",
    "ai"
]

SKILL_PATTERNS["natural language processing"] = [
    "natural language processing",
    "nlp"
]

SKILL_PATTERNS["computer vision"] = [
    "computer vision"
]

SKILL_PATTERNS["javascript"] = [
    "javascript",
    "js"
]

SKILL_PATTERNS["typescript"] = [
    "typescript",
    "ts"
]

SKILL_PATTERNS["node.js"] = [
    "node.js",
    "nodejs"
]


def contains_skill(text: str, pattern: str) -> bool:
    """
    Check whether a skill appears as a separate term
    inside the resume text.
    """

    text_lower = text.lower()
    pattern_lower = pattern.lower()

    regex = (
        r"(?<![a-z0-9])"
        + re.escape(pattern_lower)
        + r"(?![a-z0-9])"
    )

    return re.search(regex, text_lower) is not None


def extract_skills(text: str) -> list:
    """
    Extract known skills from resume text.
    """

    detected_skills = []

    for skill, patterns in SKILL_PATTERNS.items():

        for pattern in patterns:

            if contains_skill(text, pattern):
                detected_skills.append(skill)
                break

    return sorted(set(detected_skills))


def find_matching_role(target_role: str) -> str | None:
    """
    Match the user's target role against the built-in
    role catalog.
    """

    if not target_role:
        return None

    target_lower = target_role.lower().strip()

    for canonical_role, aliases in ROLE_ALIASES.items():

        for alias in aliases:

            if alias in target_lower:
                return canonical_role

    return None


def analyze_career_goal(
    text: str,
    target_role: str,
    expected_package: str | None = None,
    industry: str | None = None,
    experience_level: str | None = None
) -> dict:
    """
    Compare resume skills with the requirements of
    the user's target role.
    """

    current_skills = extract_skills(text)

    matched_role = find_matching_role(target_role)

    # -----------------------------------------------------
    # Unknown role
    # -----------------------------------------------------

    if matched_role is None:

        recommendations = [
            "The selected target role is not currently in the built-in role catalog.",
            "Add a role-specific skill mapping before relying on automated skill-gap analysis."
        ]

        if industry:
            recommendations.append(
                f"Tailor your resume toward the {industry} industry."
            )

        return {
            "target_role": target_role,
            "matched_role": None,
            "expected_package": expected_package,
            "industry": industry,
            "experience_level": experience_level,
            "current_skills": current_skills,
            "required_skills": [],
            "matching_skills": [],
            "missing_skills": [],
            "coverage_percentage": 0,
            "recommendations": recommendations,
            "note": (
                "Career-gap analysis is currently available only "
                "for roles in the built-in catalog."
            )
        }

    # -----------------------------------------------------
    # Known role
    # -----------------------------------------------------

    required_skills = ROLE_REQUIREMENTS[matched_role]

    current_skill_set = set(current_skills)

    matching_skills = [
        skill
        for skill in required_skills
        if skill in current_skill_set
    ]

    missing_skills = [
        skill
        for skill in required_skills
        if skill not in current_skill_set
    ]

    if required_skills:
        coverage_percentage = round(
            (
                len(matching_skills)
                / len(required_skills)
            ) * 100
        )
    else:
        coverage_percentage = 0

    recommendations = []

    # -----------------------------------------------------
    # Missing skills
    # -----------------------------------------------------

    if missing_skills:

        for skill in missing_skills[:5]:

            recommendations.append(
                f"Consider developing {skill} for the {matched_role} role."
            )

    # -----------------------------------------------------
    # Resume evidence
    # -----------------------------------------------------

    if matching_skills:

        recommendations.append(
            "Make sure your matching skills are supported by "
            "projects, internships, coursework, or experience in the resume."
        )

    else:

        recommendations.append(
            "Build or demonstrate role-relevant skills through "
            "projects, internships, coursework, or practical experience."
        )

    # -----------------------------------------------------
    # Coverage-based recommendation
    # -----------------------------------------------------

    if coverage_percentage < 40:

        recommendations.append(
            "Your resume currently shows limited coverage of the "
            "baseline skills configured for this target role."
        )

    elif coverage_percentage < 70:

        recommendations.append(
            "Focus first on the missing role-specific skills and "
            "demonstrate them through practical projects."
        )

    elif coverage_percentage < 100:

        recommendations.append(
            "Your resume covers many of the configured role skills. "
            "Work on the remaining gaps and strengthen evidence for your skills."
        )

    else:

        recommendations.append(
            "Your extracted skills cover all baseline skills in our "
            "role catalog. Continue tailoring the resume to each job description."
        )

    # -----------------------------------------------------
    # Industry
    # -----------------------------------------------------

    if industry:

        recommendations.append(
            f"Tailor your projects, terminology, and resume content "
            f"toward the {industry} industry."
        )

    # -----------------------------------------------------
    # Experience level
    # -----------------------------------------------------

    if experience_level:

        recommendations.append(
            f"Present your resume evidence clearly for your "
            f"{experience_level} experience level."
        )

    # -----------------------------------------------------
    # Package goal
    # -----------------------------------------------------

    if expected_package:

        recommendations.append(
            f"Your stated package goal is {expected_package}. "
            "This version records the goal but does not use salary-market "
            "data to judge whether the target is realistic."
        )

    return {
        "target_role": target_role,
        "matched_role": matched_role,
        "expected_package": expected_package,
        "industry": industry,
        "experience_level": experience_level,
        "current_skills": current_skills,
        "required_skills": required_skills,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "coverage_percentage": coverage_percentage,
        "recommendations": recommendations,
        "note": (
            "Coverage represents overlap with this project's configured "
            "baseline skills; it is not a measure of job eligibility or hiring probability."
        )
    }