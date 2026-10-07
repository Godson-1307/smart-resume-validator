from pydantic import BaseModel, Field


class CareerGoal(BaseModel):
    target_role: str = Field(
        ...,
        min_length=2,
        description="The job role the user is targeting."
    )

    expected_package: str | int | float | None = Field(
        default=None,
        description="Expected salary package, for example 10 LPA."
    )

    industry: str | None = Field(
        default=None,
        description="Target industry."
    )

    experience_level: str | None = Field(
        default=None,
        description="Experience level such as Fresher or Experienced."
    )

    country: str | None = Field(
        default=None,
        description="Target country."
    )

    city: str | None = Field(
        default=None,
        description="Target city."
    )

    work_type: str | None = Field(
        default=None,
        description="Remote, Hybrid, or On-site."
    )