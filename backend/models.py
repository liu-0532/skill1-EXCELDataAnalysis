from pydantic import BaseModel


class SkillResponse(BaseModel):
    skill_id: int
    skill_name: str


class UploadResponse(BaseModel):
    success: bool
    message: str


class AnalysisRequest(BaseModel):
    data: list
    analysis_type: str


class AnalysisResponse(BaseModel):
    result: dict
    succeeded: bool


class ErrorResponse(BaseModel):
    error_code: int
    error_message: str