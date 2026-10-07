from app.services.career_service import (
    ROLE_REQUIREMENTS,
    ROLE_ALIASES,
    extract_skills,
    find_matching_role
)

from app.services.job_match_service import (
    match_resume_to_job
)


# =========================================================
# PROJECT RECOMMENDATIONS BY ROLE
# =========================================================

PROJECT_RECOMMENDATIONS = {
    "Machine Learning Engineer": [
        "Build an end-to-end machine learning project with model training, evaluation, and deployment.",
        "Build a prediction system using Python, Pandas, NumPy, and Scikit-learn with a documented API.",
        "Create a model deployment project using PyTorch or TensorFlow with Docker."
    ],

    "Data Scientist": [
        "Build a complete data science project covering preprocessing, exploratory analysis, modeling, and evaluation.",
        "Create a predictive analytics project with clear statistical reasoning and visualizations.",
        "Build a real-world dataset project and document insights, model performance, and limitations."
    ],

    "Data Analyst": [
        "Create a dashboard project using SQL, Excel, Power BI, or another visualization tool.",
        "Build an exploratory data analysis project with business-oriented insights.",
        "Create a data cleaning and reporting pipeline using Python and SQL."
    ],

    "AI Engineer": [
        "Build an AI application using a language model and a Python backend.",
        "Create an AI system that combines a model with an API and persistent data storage.",
        "Build a practical generative AI application with evaluation and documented results."
    ],

    "NLP Engineer": [
        "Build an NLP project covering text preprocessing, modeling, evaluation, and deployment.",
        "Create a document or text analysis application using Transformers or an NLP framework.",
        "Build a question-answering or information-extraction system and evaluate its output."
    ],

    "Computer Vision Engineer": [
        "Build an image classification or object-detection application using PyTorch or TensorFlow.",
        "Create a computer vision pipeline covering preprocessing, inference, and evaluation.",
        "Build a document/image analysis application using a vision model."
    ],

    "Software Developer": [
        "Build a complete backend application with authentication, database operations, APIs, and testing.",
        "Create a data-structure-focused application demonstrating algorithms and problem solving.",
        "Build and document a production-style software project using Git and version control."
    ],

    "Web Developer": [
        "Build a responsive full-stack application with a frontend, backend API, and database.",
        "Create a portfolio project with authentication, CRUD operations, and deployment.",
        "Build a real-world web application with clear API documentation."
    ],

    "Backend Developer": [
        "Build a REST API with authentication, validation, database integration, and testing.",
        "Create a backend service using FastAPI, Flask, or Django with PostgreSQL or MongoDB.",
        "Build a containerized backend application and document its API."
    ],

    "Frontend Developer": [
        "Build a responsive React application consuming a real backend API.",
        "Create a dashboard with reusable components, form validation, and API integration.",
        "Build a polished web application with accessible and responsive UI design."
    ]
}


# =========================================================
# SUPPORTING SKILLS
# =========================================================

SUPPORTING_SKILLS = {
    "Machine Learning Engineer": [
        "docker",
        "rest api",
        "data analysis"
    ],

    "Data Scientist": [
        "data visualization",
        "statistics",
        "git"
    ],

    "Data Analyst": [
        "data visualization",
        "statistics",
        "sql"
    ],

    "AI Engineer": [
        "docker",
        "rest api",
        "transformers"
    ],

    "NLP Engineer": [
        "transformers",
        "docker",
        "git"
    ],

    "Computer Vision Engineer": [
        "opencv",
        "docker",
        "git"
    ],

    "Software Developer": [
        "git",
        "github",
        "rest api"
    ],

    "Web Developer": [
        "javascript",
        "git",
        "github"
    ],

    "Backend Developer": [
        "rest api",
        "docker",
        "git"
    ],

    "Frontend Developer": [
        "javascript",
        "react",
        "git"
    ]
}


# =========================================================
# NORMALIZATION
# =========================================================

def normalize_skill(skill: str) -> str:
    """
    Normalize a skill name.
    """

    return skill.strip().lower()


# =========================================================
# ALTERNATIVE ROLE ANALYSIS
# =========================================================

def calculate_role_overlap(
    current_skills: list,
    required_skills: list
) -> int:
    """
    Calculate overlap between candidate skills
    and a role's configured skills.
    """

    current_set = {
        normalize_skill(skill)
        for skill in current_skills
    }

    required_set = {
        normalize_skill(skill)
        for skill in required_skills
    }

    if not required_set:
        return 0

    matching = (
        current_set.intersection(
            required_set
        )
    )

    return round(
        len(matching)
        / len(required_set)
        * 100
    )


def recommend_related_roles(
    current_skills: list,
    target_role: str | None
) -> list:
    """
    Identify related roles based on configured
    skill overlap.

    These are compatibility suggestions, not
    hiring predictions.
    """

    results = []

    for role, requirements in ROLE_REQUIREMENTS.items():

        if role == target_role:
            continue

        overlap = calculate_role_overlap(
            current_skills,
            requirements
        )

        results.append(
            {
                "role": role,
                "skill_overlap_percentage": overlap
            }
        )

    results.sort(
        key=lambda item: item[
            "skill_overlap_percentage"
        ],
        reverse=True
    )

    return results[:3]


# =========================================================
# LEARNING PLAN
# =========================================================

def build_learning_priorities(
    target_role: str,
    missing_skills: list
) -> list:
    """
    Convert missing skills into an ordered learning plan.
    """

    priorities = []

    supporting = {
        normalize_skill(skill)
        for skill in SUPPORTING_SKILLS.get(
            target_role,
            []
        )
    }

    for skill in missing_skills:

        normalized = normalize_skill(
            skill
        )

        if normalized in supporting:

            priority = "Medium"

        else:

            priority = "High"

        priorities.append(
            {
                "skill": skill,
                "priority": priority,
                "reason": (
                    f"{skill} is part of the configured "
                    f"skill profile for {target_role}."
                )
            }
        )

    high = [
        item
        for item in priorities
        if item["priority"] == "High"
    ]

    medium = [
        item
        for item in priorities
        if item["priority"] == "Medium"
    ]

    return (
        high + medium
    )[:8]


# =========================================================
# PROFILE ACTIONS
# =========================================================

def generate_profile_actions(
    resume_text: str,
    target_role: str,
    matching_skills: list,
    missing_skills: list,
    job_match: dict | None
) -> list:
    """
    Generate practical actions for improving the profile.
    """

    actions = []

    normalized_resume = resume_text.lower()

    # -----------------------------------------------------
    # Target role
    # -----------------------------------------------------

    actions.append(
        f"Tailor the resume summary and strongest projects toward {target_role}."
    )

    # -----------------------------------------------------
    # Skill evidence
    # -----------------------------------------------------

    if matching_skills:

        actions.append(
            "Make the strongest matching skills visible in project and experience descriptions."
        )

    # -----------------------------------------------------
    # Missing skill evidence
    # -----------------------------------------------------

    if missing_skills:

        actions.append(
            "Add newly developed target-role skills only after gaining genuine practical experience with them."
        )

    # -----------------------------------------------------
    # Experience
    # -----------------------------------------------------

    experience_terms = [
        "intern",
        "internship",
        "job simulation",
        "virtual experience",
        "work experience"
    ]

    if not any(
        term in normalized_resume
        for term in experience_terms
    ):

        actions.append(
            "Build practical experience through internships, simulations, freelance work, or substantial projects when available."
        )

    # -----------------------------------------------------
    # GitHub
    # -----------------------------------------------------

    if "github" not in normalized_resume:

        actions.append(
            "Add relevant GitHub repositories for projects you want employers to review."
        )

    # -----------------------------------------------------
    # Job-specific
    # -----------------------------------------------------

    if job_match:

        match_percentage = job_match.get(
            "overall_match_percentage",
            0
        )

        if match_percentage < 70:

            actions.append(
                "Tailor the resume more closely to the actual job description by emphasizing relevant skills and responsibilities that are genuinely supported by your experience."
            )

        else:

            actions.append(
                "Preserve the strong overlap while tailoring the summary and project descriptions to the specific job description."
            )

    return actions[:7]


# =========================================================
# GOAL SUMMARY
# =========================================================

def build_goal_summary(
    target_role: str,
    expected_package: str | None,
    industry: str | None,
    experience_level: str | None
) -> dict:
    """
    Store and summarize the user's stated career goal.
    """

    return {
        "target_role": target_role,
        "expected_package": expected_package,
        "industry": industry,
        "experience_level": experience_level,
        "package_note": (
            "The package is treated as the user's stated goal. "
            "This system does not infer salary eligibility from it."
        )
    }


# =========================================================
# MAIN CAREER RECOMMENDATION ENGINE
# =========================================================

def generate_advanced_career_recommendations(
    resume_text: str,
    target_role: str,
    expected_package: str | None = None,
    industry: str | None = None,
    experience_level: str | None = None,
    job_description: str | None = None
) -> dict:
    """
    Generate advanced career recommendations from
    resume skills, target role and optional JD.
    """

    if not resume_text or not resume_text.strip():

        raise ValueError(
            "Resume text is empty."
        )

    if not target_role or not target_role.strip():

        raise ValueError(
            "Target role is required."
        )

    # -----------------------------------------------------
    # Current skills
    # -----------------------------------------------------

    current_skills = extract_skills(
        resume_text
    )

    # -----------------------------------------------------
    # Match target role
    # -----------------------------------------------------

    matched_role = find_matching_role(
        target_role
    )

    # -----------------------------------------------------
    # Unknown target role
    # -----------------------------------------------------

    if matched_role is None:

        return {
            "goal": build_goal_summary(
                target_role,
                expected_package,
                industry,
                experience_level
            ),

            "matched_role": None,

            "current_skills": current_skills,

            "required_skills": [],

            "matching_skills": [],

            "missing_skills": [],

            "skill_coverage_percentage": 0,

            "learning_priorities": [],

            "recommended_projects": [],

            "profile_actions": [
                (
                    "The target role is not currently "
                    "present in the configured role catalog."
                ),
                (
                    "Add a role-specific skill mapping "
                    "before using automated gap analysis."
                )
            ],

            "related_roles": recommend_related_roles(
                current_skills,
                None
            ),

            "job_match": None,

            "message": (
                "Career recommendations were generated, "
                "but detailed role-gap analysis is unavailable "
                "for this target role."
            )
        }

    # -----------------------------------------------------
    # Role requirements
    # -----------------------------------------------------

    required_skills = ROLE_REQUIREMENTS[
        matched_role
    ]

    current_skill_set = {
        normalize_skill(skill)
        for skill in current_skills
    }

    matching_skills = [
        skill
        for skill in required_skills
        if normalize_skill(skill)
        in current_skill_set
    ]

    missing_skills = [
        skill
        for skill in required_skills
        if normalize_skill(skill)
        not in current_skill_set
    ]

    if required_skills:

        skill_coverage = round(
            len(matching_skills)
            / len(required_skills)
            * 100
        )

    else:

        skill_coverage = 0

    # -----------------------------------------------------
    # Learning priorities
    # -----------------------------------------------------

    learning_priorities = build_learning_priorities(
        matched_role,
        missing_skills
    )

    # -----------------------------------------------------
    # Project recommendations
    # -----------------------------------------------------

    recommended_projects = (
        PROJECT_RECOMMENDATIONS.get(
            matched_role,
            []
        )[:3]
    )

    # -----------------------------------------------------
    # Optional job description match
    # -----------------------------------------------------

    job_match = None

    if job_description:

        job_match = match_resume_to_job(
            resume_text=resume_text,
            job_description=job_description,
            job_title=matched_role
        )

    # -----------------------------------------------------
    # Profile actions
    # -----------------------------------------------------

    profile_actions = generate_profile_actions(
        resume_text=resume_text,
        target_role=matched_role,
        matching_skills=matching_skills,
        missing_skills=missing_skills,
        job_match=job_match
    )

    # -----------------------------------------------------
    # Related roles
    # -----------------------------------------------------

    related_roles = recommend_related_roles(
        current_skills,
        matched_role
    )

    # -----------------------------------------------------
    # Role summary
    # -----------------------------------------------------

    if skill_coverage < 40:

        coverage_message = (
            "The resume currently has limited overlap "
            "with the configured baseline skills for this role."
        )

    elif skill_coverage < 70:

        coverage_message = (
            "The resume shows partial overlap with the "
            "configured baseline skills for this role."
        )

    else:

        coverage_message = (
            "The resume shows substantial overlap with "
            "the configured baseline skills for this role."
        )

    return {
        "goal": build_goal_summary(
            target_role,
            expected_package,
            industry,
            experience_level
        ),

        "matched_role": matched_role,

        "current_skills": current_skills,

        "required_skills": required_skills,

        "matching_skills": matching_skills,

        "missing_skills": missing_skills,

        "skill_coverage_percentage": skill_coverage,

        "coverage_message": coverage_message,

        "learning_priorities": learning_priorities,

        "recommended_projects": recommended_projects,

        "profile_actions": profile_actions,

        "related_roles": related_roles,

        "job_match": job_match,

        "message": (
            "Advanced career recommendations generated "
            "from the configured role and skill profiles."
        )
    }