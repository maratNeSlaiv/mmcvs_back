from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.router.matcher import matcher_router

app = FastAPI()

# Allow CORS from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust the URL as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Add the router to the FastAPI app
app.include_router(matcher_router, prefix="/analysis")