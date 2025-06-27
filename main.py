from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import upload  

app = FastAPI(
    title="SMART AI SDLC",
    description="API for classifying project documents into SDLC phases using OpenAI",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
