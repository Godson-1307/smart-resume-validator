from pydantic import BaseModel, Field


class CareerRecommendationRequest(BaseModel):

    target_role: str = Field(
        ...,
        min_length=2,
        description="Target career role."
    )

    expected_package: str | None = Field(
        default=None,
        description="Expected package, for example 10 LPA."
    )

    industry: str | None = Field(
        default=None,
        description="Target industry."
    )

    experience_level: str | None = Field(
        default=None,
        description="Fresher, Junior, Experienced, etc."
    )

    job_description: str | None = Field(
        default=None,
        min_length=20,
        description="Optional job description for job-specific recommendations."
    )