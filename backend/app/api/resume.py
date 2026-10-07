from pathlib import Path
import uuid

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

from app.models.career_goal import CareerGoal

from app.services.document_service import (
    extract_text,
    clean_text,
    check_text_quality
)

from app.services.resume_validator import (
    validate_resume
)

from app.services.resume_scorer import (
    calculate_resume_score
)

from app.services.recommendation_service import (
    generate_recommendations
)

from app.services.career_service import (
    analyze_career_goal
)

from app.services.qwen_service import (
    extract_resume_information
)

from app.services.qwen_analysis_service import (
    analyze_resume_semantically
)

from app.db.resume_repository import (
    create_resume_record,
    save_extracted_text,
    save_validation_result,
    save_score_result,
    save_ai_analysis,
    save_career_analysis,
    save_career_recommendations,
    save_job_match,
    get_resume,
    get_all_resumes
)

from app.services.advanced_resume_intelligence import (
    analyze_advanced_resume_intelligence
)

from app.models.job_description import (
    JobDescriptionRequest
)

from app.services.job_match_service import (
    match_resume_to_job
)

from app.db.resume_repository import (
    save_job_match
)

from app.models.career_recommendation import (
    CareerRecommendationRequest
)

from app.services.advanced_career_service import (
    generate_advanced_career_recommendations
)
# =========================================================
# ROUTER
# =========================================================

router = APIRouter(
    prefix="/api/resume",
    tags=["Resume"]
)


# =========================================================
# DIRECTORIES
# =========================================================

BASE_DIR = Path(__file__).resolve().parents[3]

UPLOAD_DIR = BASE_DIR / "uploads"

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# =========================================================
# FILE RULES
# =========================================================

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".doc",
    ".docx"
}

MAX_FILE_SIZE = 10 * 1024 * 1024


# =========================================================
# UPLOAD
# =========================================================

@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...)
):

    if not file.filename:

        raise HTTPException(
            status_code=400,
            detail="No file was provided."
        )

    extension = Path(
        file.filename
    ).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:

        raise HTTPException(
            status_code=400,
            detail=(
                "Only PDF, DOC, and DOCX "
                "files are allowed."
            )
        )

    file_content = await file.read()

    if len(file_content) > MAX_FILE_SIZE:

        raise HTTPException(
            status_code=413,
            detail=(
                "File size must be "
                "10 MB or less."
            )
        )

    resume_id = (
        f"res_{uuid.uuid4().hex[:8]}"
    )

    saved_filename = (
        f"{resume_id}{extension}"
    )

    file_path = (
        UPLOAD_DIR / saved_filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(
            file_content
        )

    # Save initial database record
    create_resume_record(
        resume_id=resume_id,
        original_filename=file.filename,
        saved_filename=saved_filename,
        file_type=extension.replace(
            ".",
            ""
        ),
        file_path=str(file_path)
    )

    return {
        "success": True,
        "resume_id": resume_id,
        "original_filename": file.filename,
        "saved_filename": saved_filename,
        "file_type": extension.replace(
            ".",
            ""
        ),
        "message": (
            "Resume uploaded successfully."
        )
    }


# =========================================================
# TEXT EXTRACTION
# =========================================================

@router.get("/{resume_id}/extract")
def extract_resume_text(
    resume_id: str
):

    matching_files = list(
        UPLOAD_DIR.glob(
            f"{resume_id}.*"
        )
    )

    if not matching_files:

        raise HTTPException(
            status_code=404,
            detail="Resume file not found."
        )

    file_path = matching_files[0]

    try:

        extracted_text = extract_text(
            file_path
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail=(
                "Unable to extract text "
                "from the document."
            )
        )

    cleaned_text = clean_text(
        extracted_text
    )

    save_extracted_text(
        resume_id,
        cleaned_text
    )

    return {
        "success": True,
        "resume_id": resume_id,
        "text": cleaned_text
    }


# =========================================================
# TEXT QUALITY
# =========================================================

@router.get("/{resume_id}/quality")
def check_resume_quality(
    resume_id: str
):

    matching_files = list(
        UPLOAD_DIR.glob(
            f"{resume_id}.*"
        )
    )

    if not matching_files:

        raise HTTPException(
            status_code=404,
            detail="Resume file not found."
        )

    file_path = matching_files[0]

    try:

        extracted_text = extract_text(
            file_path
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail=(
                "Unable to extract text "
                "from the document."
            )
        )

    cleaned_text = clean_text(
        extracted_text
    )

    save_extracted_text(
        resume_id,
        cleaned_text
    )

    quality = check_text_quality(
        cleaned_text
    )

    return {
        "success": True,
        "resume_id": resume_id,
        "quality": quality
    }


# =========================================================
# VALIDATION
# =========================================================

@router.get("/{resume_id}/validate")
def validate_uploaded_resume(
    resume_id: str
):

    matching_files = list(
        UPLOAD_DIR.glob(
            f"{resume_id}.*"
        )
    )

    if not matching_files:

        raise HTTPException(
            status_code=404,
            detail="Resume file not found."
        )

    file_path = matching_files[0]

    try:

        extracted_text = extract_text(
            file_path
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail=(
                "Unable to extract text "
                "from the document."
            )
        )

    cleaned_text = clean_text(
        extracted_text
    )

    save_extracted_text(
        resume_id,
        cleaned_text
    )

    if not cleaned_text:

        validation = {
            "is_resume": False,
            "confidence": 0,
            "reasons": [
                "No readable text was found."
            ],
            "message": (
                "Please upload a proper resume."
            )
        }

    else:

        validation = validate_resume(
            cleaned_text
        )

    save_validation_result(
        resume_id,
        validation
    )

    return {
        "success": True,
        "resume_id": resume_id,
        **validation
    }


# =========================================================
# SCORE
# =========================================================

@router.get("/{resume_id}/score")
def score_uploaded_resume(
    resume_id: str
):

    matching_files = list(
        UPLOAD_DIR.glob(
            f"{resume_id}.*"
        )
    )

    if not matching_files:

        raise HTTPException(
            status_code=404,
            detail="Resume file not found."
        )

    file_path = matching_files[0]

    try:

        extracted_text = extract_text(
            file_path
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail=(
                "Unable to extract text "
                "from the document."
            )
        )

    cleaned_text = clean_text(
        extracted_text
    )

    save_extracted_text(
        resume_id,
        cleaned_text
    )

    validation = validate_resume(
        cleaned_text
    )

    save_validation_result(
        resume_id,
        validation
    )

    if not validation["is_resume"]:

        return {
            "success": True,
            "resume_id": resume_id,
            "is_resume": False,
            "score": None,
            "message": (
                "Please upload a proper resume."
            ),
            "reason": (
                "The uploaded document does not "
                "appear to be a resume."
            )
        }

    score_result = calculate_resume_score(
        cleaned_text
    )

    recommendations = generate_recommendations(
        score_result
    )

    save_score_result(
        resume_id,
        score_result,
        recommendations
    )

    return {
        "success": True,
        "resume_id": resume_id,
        "is_resume": True,
        "score": score_result["score"],
        "breakdown": score_result["breakdown"],
        "improvements": score_result["improvements"],
        "recommendations": recommendations,
        "message": (
            "Resume scored successfully."
        )
    }


# =========================================================
# QWEN EXTRACTION
# =========================================================

@router.get("/{resume_id}/ai-analysis")
def ai_analyze_uploaded_resume(
    resume_id: str
):

    matching_files = list(
        UPLOAD_DIR.glob(
            f"{resume_id}.*"
        )
    )

    if not matching_files:

        raise HTTPException(
            status_code=404,
            detail="Resume file not found."
        )

    file_path = matching_files[0]

    try:

        extracted_text = extract_text(
            file_path
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail=(
                "Unable to extract text "
                "from the document."
            )
        )

    cleaned_text = clean_text(
        extracted_text
    )

    save_extracted_text(
        resume_id,
        cleaned_text
    )

    validation = validate_resume(
        cleaned_text
    )

    save_validation_result(
        resume_id,
        validation
    )

    if not validation["is_resume"]:

        return {
            "success": True,
            "resume_id": resume_id,
            "is_resume": False,
            "message": (
                "Please upload a proper resume."
            )
        }

    try:

        extracted_information = (
            extract_resume_information(
                cleaned_text
            )
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )

    save_ai_analysis(
        resume_id,
        extracted_information
    )

    return {
        "success": True,
        "resume_id": resume_id,
        "is_resume": True,
        "ai_analysis": extracted_information,
        "message": (
            "Resume analyzed successfully "
            "using Qwen."
        )
    }


# =========================================================
# CAREER ANALYSIS
# =========================================================

@router.post("/{resume_id}/career-analysis")
def career_analysis(
    resume_id: str,
    career_goal: CareerGoal
):
    """
    Compare the uploaded resume against the user's
    target career goal and persist the result.
    """

    matching_files = list(
        UPLOAD_DIR.glob(f"{resume_id}.*")
    )

    if not matching_files:
        raise HTTPException(
            status_code=404,
            detail="Resume file not found."
        )

    file_path = matching_files[0]

    try:
        extracted_text = extract_text(file_path)

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to extract text from the document."
        )

    cleaned_text = clean_text(extracted_text)

    save_extracted_text(
        resume_id,
        cleaned_text
    )

    validation = validate_resume(cleaned_text)

    save_validation_result(
        resume_id,
        validation
    )

    if not validation["is_resume"]:
        return {
            "success": True,
            "resume_id": resume_id,
            "is_resume": False,
            "message": "Please upload a proper resume."
        }

    analysis = analyze_career_goal(
        text=cleaned_text,
        target_role=career_goal.target_role,
        expected_package=(
            str(career_goal.expected_package)
            if career_goal.expected_package is not None
            else None
        ),
        industry=career_goal.industry,
        experience_level=career_goal.experience_level
    )

    # Keep frontend goal information in the stored result.
    analysis["country"] = career_goal.country
    analysis["city"] = career_goal.city
    analysis["work_type"] = career_goal.work_type

    save_career_analysis(
        resume_id,
        analysis
    )

    return {
        "success": True,
        "resume_id": resume_id,
        "is_resume": True,
        "career_analysis": analysis
    }


# =========================================================
# FULL ANALYSIS
# =========================================================

@router.get(
    "/{resume_id}/full-analysis"
)
def full_resume_analysis(
    resume_id: str
):

    matching_files = list(
        UPLOAD_DIR.glob(
            f"{resume_id}.*"
        )
    )

    if not matching_files:

        raise HTTPException(
            status_code=404,
            detail="Resume file not found."
        )

    file_path = matching_files[0]

    try:

        extracted_text = extract_text(
            file_path
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail=(
                "Unable to extract text "
                "from the document."
            )
        )

    cleaned_text = clean_text(
        extracted_text
    )

    save_extracted_text(
        resume_id,
        cleaned_text
    )

    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    validation = validate_resume(
        cleaned_text
    )

    save_validation_result(
        resume_id,
        validation
    )

    if not validation["is_resume"]:

        return {
            "success": True,
            "resume_id": resume_id,
            "is_resume": False,
            "score": None,
            "message": (
                "Please upload a proper resume."
            )
        }

    # -----------------------------------------------------
    # SCORE
    # -----------------------------------------------------

    score_result = calculate_resume_score(
        cleaned_text
    )

    recommendations = generate_recommendations(
        score_result
    )

        # -----------------------------------------------------
    # ADVANCED RESUME INTELLIGENCE
    # -----------------------------------------------------

    try:

        advanced_intelligence = (
            analyze_advanced_resume_intelligence(
                cleaned_text
            )
        )

    except Exception as error:

        advanced_intelligence = {
            "success": False,
            "error": str(error)
        }

    save_score_result(
        resume_id,
        score_result,
        recommendations
    )

    # -----------------------------------------------------
    # QWEN EXTRACTION
    # -----------------------------------------------------

    try:

        ai_extraction = (
            extract_resume_information(
                cleaned_text
            )
        )

        save_ai_analysis(
            resume_id,
            ai_extraction
        )

    except Exception as error:

        ai_extraction = {
            "success": False,
            "error": str(error)
        }

    # -----------------------------------------------------
    # QWEN SEMANTIC ANALYSIS
    # -----------------------------------------------------

    try:

        semantic_analysis = (
            analyze_resume_semantically(
                cleaned_text
            )
        )

    except Exception as error:

        semantic_analysis = {
            "success": False,
            "message": (
                "Semantic analysis failed."
            ),
            "error": str(error)
        }

    # Save both AI outputs together
    save_ai_analysis(
        resume_id,
        {
            "extraction": ai_extraction,
            "semantic_analysis": semantic_analysis
        }
    )

    return {
        "success": True,
        "resume_id": resume_id,
        "is_resume": True,
        "score": score_result["score"],
        "breakdown": score_result["breakdown"],
        "rule_based_improvements": (
            score_result["improvements"]
        ),
        "recommendations": recommendations,
        "advanced_intelligence": advanced_intelligence,
        "ai_extraction": ai_extraction,
        "ai_semantic_analysis": semantic_analysis,
        "message": (
            "Complete resume analysis "
            "performed successfully."
        )
    }


# =========================================================
# SINGLE RESUME HISTORY
# =========================================================

@router.get(
    "/{resume_id}/history"
)
def get_resume_history(
    resume_id: str
):

    resume = get_resume(
        resume_id
    )

    if resume is None:

        raise HTTPException(
            status_code=404,
            detail="Resume record not found."
        )

    return {
        "success": True,
        "resume": resume
    }


# =========================================================
# ALL RESUME HISTORY
# =========================================================

@router.get(
    "/history/all"
)
def get_all_resume_history():

    resumes = get_all_resumes()

    return {
        "success": True,
        "count": len(resumes),
        "resumes": resumes
    }

@router.get(
    "/{resume_id}/advanced-intelligence"
)
def advanced_resume_intelligence(
    resume_id: str
):
    """
    Run advanced resume intelligence analysis.
    """

    matching_files = list(
        UPLOAD_DIR.glob(
            f"{resume_id}.*"
        )
    )

    if not matching_files:

        raise HTTPException(
            status_code=404,
            detail="Resume file not found."
        )

    file_path = matching_files[0]

    try:

        extracted_text = extract_text(
            file_path
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail=(
                "Unable to extract text "
                "from the document."
            )
        )

    cleaned_text = clean_text(
        extracted_text
    )

    validation = validate_resume(
        cleaned_text
    )

    if not validation["is_resume"]:

        return {
            "success": True,
            "resume_id": resume_id,
            "is_resume": False,
            "message": (
                "Please upload a proper resume."
            )
        }

    try:

        intelligence = (
            analyze_advanced_resume_intelligence(
                cleaned_text
            )
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail=(
                "Advanced resume intelligence "
                "analysis failed."
            )
        )

    return {
        "success": True,
        "resume_id": resume_id,
        "is_resume": True,
        "advanced_intelligence": intelligence,
        "message": (
            "Advanced resume intelligence "
            "generated successfully."
        )
    }

@router.post(
    "/{resume_id}/job-match"
)
def job_description_match(
    resume_id: str,
    request: JobDescriptionRequest
):
    """
    Compare an uploaded resume against a job description.
    """

    matching_files = list(
        UPLOAD_DIR.glob(
            f"{resume_id}.*"
        )
    )

    if not matching_files:

        raise HTTPException(
            status_code=404,
            detail="Resume file not found."
        )

    file_path = matching_files[0]

    # -----------------------------------------------------
    # Extract resume
    # -----------------------------------------------------

    try:

        extracted_text = extract_text(
            file_path
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail=(
                "Unable to extract text "
                "from the resume."
            )
        )

    cleaned_text = clean_text(
        extracted_text
    )

    save_extracted_text(
        resume_id,
        cleaned_text
    )

    # -----------------------------------------------------
    # Validate
    # -----------------------------------------------------

    validation = validate_resume(
        cleaned_text
    )

    save_validation_result(
        resume_id,
        validation
    )

    if not validation["is_resume"]:

        return {
            "success": True,
            "resume_id": resume_id,
            "is_resume": False,
            "message": (
                "Please upload a proper resume."
            )
        }

    # -----------------------------------------------------
    # Match
    # -----------------------------------------------------

    try:

        match_result = match_resume_to_job(
            resume_text=cleaned_text,
            job_description=request.job_description,
            job_title=request.job_title,
            company=request.company
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    # -----------------------------------------------------
    # Save
    # -----------------------------------------------------

    save_job_match(
        resume_id=resume_id,
        job_description=request.job_description,
        job_match_analysis=match_result
    )

    return {
        "success": True,
        "resume_id": resume_id,
        "is_resume": True,
        "job_match": match_result,
        "message": (
            "Resume matched against the "
            "job description successfully."
        )
    }

@router.post(
    "/{resume_id}/career-recommendations"
)
def advanced_career_recommendations(
    resume_id: str,
    request: CareerRecommendationRequest
):
    """
    Generate advanced career recommendations
    from resume skills and the user's career goal.
    """

    matching_files = list(
        UPLOAD_DIR.glob(
            f"{resume_id}.*"
        )
    )

    if not matching_files:

        raise HTTPException(
            status_code=404,
            detail="Resume file not found."
        )

    file_path = matching_files[0]

    # -----------------------------------------------------
    # Extract resume
    # -----------------------------------------------------

    try:

        extracted_text = extract_text(
            file_path
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail=(
                "Unable to extract text "
                "from the resume."
            )
        )

    cleaned_text = clean_text(
        extracted_text
    )

    save_extracted_text(
        resume_id,
        cleaned_text
    )

    # -----------------------------------------------------
    # Validate
    # -----------------------------------------------------

    validation = validate_resume(
        cleaned_text
    )

    save_validation_result(
        resume_id,
        validation
    )

    if not validation["is_resume"]:

        return {
            "success": True,
            "resume_id": resume_id,
            "is_resume": False,
            "message": (
                "Please upload a proper resume."
            )
        }

    # -----------------------------------------------------
    # Generate recommendations
    # -----------------------------------------------------

    try:

        recommendations = (
            generate_advanced_career_recommendations(
                resume_text=cleaned_text,
                target_role=request.target_role,
                expected_package=request.expected_package,
                industry=request.industry,
                experience_level=request.experience_level,
                job_description=request.job_description
            )
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=(
                "Unable to generate advanced "
                f"career recommendations: {error}"
            )
        )

    # -----------------------------------------------------
    # Save
    # -----------------------------------------------------

    save_career_recommendations(
        resume_id,
        recommendations
    )

    # -----------------------------------------------------
    # Return
    # -----------------------------------------------------

    return {
        "success": True,
        "resume_id": resume_id,
        "is_resume": True,
        "career_recommendations": recommendations,
        "message": (
            "Advanced career recommendations "
            "generated successfully."
        )
    }