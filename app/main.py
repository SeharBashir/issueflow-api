from fastapi import FastAPI

app = FastAPI(
    title="IssueFlow API",
    description="Team Issue and Incident Management API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to IssueFlow API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "issueflow-api"
    }