from pydantic import BaseModel
from typing import Optional

class ResumeCheckRequest(BaseModel):
    resume: str
    jobDescription: str
