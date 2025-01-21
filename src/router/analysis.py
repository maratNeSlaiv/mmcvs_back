from fastapi import FastAPI, APIRouter, HTTPException
from src.schema.analysis import ResumeCheckRequest
from src.service.resume_job_description_validator import make_verdict

analysis_router = APIRouter()

@analysis_router.post("/validate_resume")
async def check_resume(request: ResumeCheckRequest):
    # Extract resume and job description from the request body
    resume = request.resume
    job_description = request.jobDescription
    
    verdict = await make_verdict(resume=resume, job_description=job_description)
    return {
        "verdict": verdict
        }