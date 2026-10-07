import re


# =========================================================
# SKILL CATALOG
# =========================================================

SKILL_PATTERNS = {
    "Python": ["python"],
    "C++": ["c++"],
    "Java": ["java"],
    "C#": ["c#"],
    "JavaScript": ["javascript"],
    "TypeScript": ["typescript"],
    "HTML": ["html"],
    "CSS": ["css"],
    "SQL": ["sql"],
    "MySQL": ["mysql"],
    "PostgreSQL": ["postgresql"],
    "MongoDB": ["mongodb"],

    "Machine Learning": [
        "machine learning",
        "machine-learning"
    ],

    "Deep Learning": [
        "deep learning",
        "deep-learning"
    ],

    "Artificial Intelligence": [
        "artificial intelligence",
        "ai"
    ],

    "Generative AI": [
        "generative ai"
    ],

    "Large Language Models": [
        "large language models",
        "large language model",
        "llms",
        "llm"
    ],

    "Natural Language Processing": [
        "natural language processing",
        "nlp"
    ],

    "Computer Vision": [
        "computer vision"
    ],

    "PyTorch": [
        "pytorch"
    ],

    "TensorFlow": [
        "tensorflow"
    ],

    "Scikit-learn": [
        "scikit-learn",
        "scikit learn"
    ],

    "Pandas": [
        "pandas"
    ],

    "NumPy": [
        "numpy"
    ],

    "Matplotlib": [
        "matplotlib"
    ],

    "OpenCV": [
        "opencv"
    ],

    "LangChain": [
        "langchain"
    ],

    "Prompt Engineering": [
        "prompt engineering"
    ],

    "Transformers": [
        "transformers"
    ],

    "Statistics": [
        "statistics",
        "statistical analysis"
    ],

    "Data Analysis": [
        "data analysis",
        "data analytics"
    ],

    "Data Visualization": [
        "data visualization"
    ],

    "Power BI": [
        "power bi"
    ],

    "Excel": [
        "excel",
        "microsoft excel"
    ],

    "FastAPI": [
        "fastapi"
    ],

    "Flask": [
        "flask"
    ],

    "Django": [
        "django"
    ],

    "React": [
        "react"
    ],

    "Node.js": [
        "node.js",
        "nodejs"
    ],

    "Git": [
        "git"
    ],

    "GitHub": [
        "github"
    ],

    "GitHub Actions": [
        "github actions"
    ],

    "Docker": [
        "docker"
    ],

    "Kubernetes": [
        "kubernetes"
    ],

    "AWS": [
        "aws",
        "amazon web services"
    ],

    "Azure": [
        "azure",
        "microsoft azure"
    ],

    "GCP": [
        "gcp",
        "google cloud"
    ],

    "Cloud Computing": [
        "cloud computing"
    ],

    "Linux": [
        "linux"
    ],

    "Data Structures": [
        "data structures",
        "data structure"
    ],

    "Algorithms": [
        "algorithms",
        "algorithm"
    ],

    "REST API": [
        "rest api",
        "restful api",
        "rest services"
    ],

    "Problem Solving": [
        "problem solving"
    ],

    "Communication": [
        "communication",
        "written communication",
        "verbal communication"
    ],

    "Leadership": [
        "leadership"
    ],

    "Teamwork": [
        "teamwork",
        "team collaboration"
    ]
}


# =========================================================
# IMPORTANT JOB-DESCRIPTION TERMS
# =========================================================

IMPORTANT_TERMS = [
    "internship",
    "intern",
    "experience",
    "freshers",
    "fresher",
    "bachelor",
    "master",
    "degree",
    "engineering",
    "agile",
    "scrum",
    "deployment",
    "testing",
    "debugging",
    "optimization",
    "deployment",
    "production",
    "research",
    "analytics",
    "documentation",
    "communication",
    "leadership",
    "collaboration",
    "problem solving"
]


# =========================================================
# TEXT NORMALIZATION
# =========================================================

def normalize_text(text: str) -> str:
    """
    Normalize text for matching.
    """

    text = text.lower()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def contains_term(
    text: str,
    term: str
) -> bool:
    """
    Check whether a term appears in text.
    """

    normalized = normalize_text(text)

    pattern = (
        r"(?<![a-z0-9])"
        + re.escape(term.lower())
        + r"(?![a-z0-9])"
    )

    return re.search(
        pattern,
        normalized
    ) is not None


# =========================================================
# SKILL EXTRACTION
# =========================================================

def extract_skills(
    text: str
) -> list:
    """
    Extract recognized skills from text.
    """

    skills = []

    for skill, patterns in SKILL_PATTERNS.items():

        for pattern in patterns:

            if contains_term(
                text,
                pattern
            ):

                if skill not in skills:
                    skills.append(skill)

                break

    return sorted(skills)


# =========================================================
# IMPORTANT TERM EXTRACTION
# =========================================================

def extract_important_terms(
    job_description: str
) -> list:
    """
    Extract additional job-description terms.
    """

    terms = []

    for term in IMPORTANT_TERMS:

        if contains_term(
            job_description,
            term
        ):

            terms.append(term)

    return sorted(terms)


# =========================================================
# JOB REQUIREMENT SENTENCES
# =========================================================

def extract_requirement_sentences(
    job_description: str
) -> list:
    """
    Extract sentences that look like requirements.
    """

    sentences = re.split(
        r"(?<=[.!?])\s+",
        job_description
    )

    requirement_words = [
        "required",
        "requirement",
        "must",
        "should have",
        "experience with",
        "knowledge of",
        "proficient",
        "skills",
        "responsibilities"
    ]

    results = []

    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        sentence_lower = sentence.lower()

        if any(
            word in sentence_lower
            for word in requirement_words
        ):

            results.append(
                sentence
            )

    return results[:15]


# =========================================================
# JD MATCH ANALYSIS
# =========================================================

def match_resume_to_job(
    resume_text: str,
    job_description: str,
    job_title: str | None = None,
    company: str | None = None
) -> dict:
    """
    Compare resume content against a job description.
    """

    if not resume_text or not resume_text.strip():

        raise ValueError(
            "Resume text is empty."
        )

    if not job_description or not job_description.strip():

        raise ValueError(
            "Job description is empty."
        )

    # -----------------------------------------------------
    # Extract skills
    # -----------------------------------------------------

    resume_skills = extract_skills(
        resume_text
    )

    jd_skills = extract_skills(
        job_description
    )

    resume_skill_set = {
        skill.lower()
        for skill in resume_skills
    }

    matching_skills = [
        skill
        for skill in jd_skills
        if skill.lower() in resume_skill_set
    ]

    missing_skills = [
        skill
        for skill in jd_skills
        if skill.lower() not in resume_skill_set
    ]

    # -----------------------------------------------------
    # Skill match percentage
    # -----------------------------------------------------

    if jd_skills:

        skill_match_percentage = round(
            (
                len(matching_skills)
                / len(jd_skills)
            ) * 100
        )

    else:

        skill_match_percentage = 0

    # -----------------------------------------------------
    # Important terms
    # -----------------------------------------------------

    jd_terms = extract_important_terms(
        job_description
    )

    normalized_resume = normalize_text(
        resume_text
    )

    matching_terms = [
        term
        for term in jd_terms
        if contains_term(
            normalized_resume,
            term
        )
    ]

    missing_terms = [
        term
        for term in jd_terms
        if term not in matching_terms
    ]

    if jd_terms:

        keyword_match_percentage = round(
            (
                len(matching_terms)
                / len(jd_terms)
            ) * 100
        )

    else:

        keyword_match_percentage = 0

    # -----------------------------------------------------
    # Overall match
    # -----------------------------------------------------

    if jd_skills and jd_terms:

        overall_match_percentage = round(
            (
                skill_match_percentage * 0.70
                +
                keyword_match_percentage * 0.30
            )
        )

    elif jd_skills:

        overall_match_percentage = (
            skill_match_percentage
        )

    elif jd_terms:

        overall_match_percentage = (
            keyword_match_percentage
        )

    else:

        overall_match_percentage = 0

    # -----------------------------------------------------
    # Resume strengths for this JD
    # -----------------------------------------------------

    strengths = []

    if matching_skills:

        strengths.append(
            "Your resume contains skills that directly overlap with the job description."
        )

    if skill_match_percentage >= 70:

        strengths.append(
            "Your detected technical skill coverage is relatively strong for this job description."
        )

    if keyword_match_percentage >= 60:

        strengths.append(
            "Your resume contains several terms that align with the job description."
        )

    if not strengths:

        strengths.append(
            "The resume contains some potentially relevant information, but the detected overlap is limited."
        )

    # -----------------------------------------------------
    # Tailoring suggestions
    # -----------------------------------------------------

    suggestions = []

    for skill in missing_skills[:6]:

        suggestions.append(
            f"If you have this skill, make {skill} more visible in your resume; otherwise consider developing it."
        )

    if missing_terms:

        suggestions.append(
            "Consider reflecting relevant job-description terminology in your resume when it accurately describes your experience."
        )

    if "experience" in missing_terms:

        suggestions.append(
            "Make internships, practical training, simulations, freelance work, or relevant experience clearly visible."
        )

    if "communication" in missing_terms:

        suggestions.append(
            "Highlight communication or collaboration evidence where it is genuinely supported by your experience."
        )

    if "testing" in missing_terms:

        suggestions.append(
            "Mention testing, debugging, or validation work when you have actually performed it."
        )

    if "deployment" in missing_terms:

        suggestions.append(
            "Highlight deployment or production-related work when applicable."
        )

    if not suggestions:

        suggestions.append(
            "Tailor the summary and strongest project or experience bullets to the specific responsibilities in this job description."
        )

    # -----------------------------------------------------
    # Requirements
    # -----------------------------------------------------

    requirements = extract_requirement_sentences(
        job_description
    )

    # -----------------------------------------------------
    # Resume skills not mentioned in JD
    # -----------------------------------------------------

    jd_skill_set = {
        skill.lower()
        for skill in jd_skills
    }

    additional_resume_skills = [
        skill
        for skill in resume_skills
        if skill.lower() not in jd_skill_set
    ]

    return {
        "job_title": job_title,
        "company": company,

        "resume_skills": resume_skills,

        "job_description_skills": jd_skills,

        "matching_skills": matching_skills,

        "missing_skills": missing_skills,

        "additional_resume_skills": (
            additional_resume_skills
        ),

        "skill_match_percentage": (
            skill_match_percentage
        ),

        "job_description_terms": jd_terms,

        "matching_terms": matching_terms,

        "missing_terms": missing_terms,

        "keyword_match_percentage": (
            keyword_match_percentage
        ),

        "overall_match_percentage": (
            overall_match_percentage
        ),

        "key_requirements": requirements,

        "strengths": strengths,

        "tailoring_suggestions": suggestions,

        "note": (
            "The match percentage represents detected overlap "
            "between the resume and this job description. "
            "It is not a hiring probability or eligibility score."
        )
    }