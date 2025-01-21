from pydantic import BaseModel
from typing import Optional

class ResumeMatchRequest(BaseModel):
    resume: str
    jobDescription: str
