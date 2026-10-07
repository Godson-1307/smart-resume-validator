from pydantic import BaseModel, Field


class JobDescriptionRequest(BaseModel):

    job_title: str | None = Field(
        default=None,
        description="Job title from the job description."
    )

    company: str | None = Field(
        default=None,
        description="Company name."
    )

    job_description: str = Field(
        ...,
        min_length=20,
        description="Complete job description text."
    )