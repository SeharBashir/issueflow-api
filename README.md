# IssueFlow API

IssueFlow is a backend API for team issue and incident management.

## Features

- User authentication
- Project management
- Issue tracking
- Issue assignment
- Comments
- Activity history
- Role-based access control
- Analytics

## Technologies

- Python
- FastAPI
- SQLAlchemy
- SQLite/PostgreSQL
- REST API
- Git

## Running Locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload