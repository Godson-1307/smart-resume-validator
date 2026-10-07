from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import (
    APP_NAME,
    APP_VERSION,
    DEBUG
)

from app.api.resume import (
    router as resume_router
)

from app.db.database import (
    initialize_database
)


# =========================================================
# DATABASE
# =========================================================

initialize_database()


# =========================================================
# APPLICATION
# =========================================================

app = FastAPI(
    title=APP_NAME,
    description=(
        "Backend API for resume validation, "
        "scoring, AI analysis and career analysis."
    ),
    version=APP_VERSION,
    debug=DEBUG
)


app.include_router(
    resume_router
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================================
# ROOT
# =========================================================

@app.get("/")
def root():

    return {
        "message": (
            "Smart Resume Validator API is running"
        )
    }


# =========================================================
# HEALTH
# =========================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }