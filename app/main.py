from fastapi import FastAPI
from app.router import router

app = FastAPI(
    title="AI Workflow Automation System",
    description="Enterprise AI system for ticket classification, routing, and summarization",
    version="1.0.0",
)

# Register routes
app.include_router(router)
