from src.config import OPENAI_API_KEY
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=OPENAI_API_KEY,  # This is the default and can be omitted
)

async def make_verdict(resume, job_description):
    prompt = f"""
    Given the following resume and job description, evaluate the fit of the applicant for the job.

    Resume:
    {resume}

    Job Description:
    {job_description}

    Please answer with:
    1. A percentage from 10% to 100% indicating how well the applicant fits the job.
    2. A list of pros of the resume in bullet points.
    3. A list of recommendations for the applicant to improve their chances in the application process in bullet points.
    """
    
    # Asynchronously send the request to OpenAI API
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o-mini",
    )
    
    # Extract response text
    response_text = chat_completion.choices[0].message.content
    return response_text


async def main():
    # Example usage
    api_key = "your_openai_api_key"
    resume = """
    John Doe
    Software Engineer
    Experience: 5 years in web development
    Skills: Python, JavaScript, React, Node.js, SQL
    Education: B.S. in Computer Science from XYZ University
    Certifications: AWS Certified Solutions Architect
    """

    job_description = """
    We are looking for a Software Engineer with at least 3 years of experience in web development.
    The ideal candidate should have strong skills in Python, JavaScript, and React. Familiarity with cloud services like AWS is a plus.
    """

    result = await make_verdict(resume, job_description)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
