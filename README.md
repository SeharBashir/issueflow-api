# IssueFlow API

IssueFlow is a backend API for team issue and incident management, built with FastAPI. It provides secure, authenticated CRUD operations for managing projects and issues.

## Current Features

- User registration and authentication (JWT-based)
- Protected endpoints (all Projects and Issues routes require a valid access token)
- Project management (full CRUD)
- Issue tracking (full CRUD)
- Project ↔ Issue relationships (ORM-linked)
- Audit fields (`created_at`, `updated_at`) on Projects and Issues
- Consistent, structured error handling (404, 400, 401, 409 responses)
- Environment-based configuration (`.env`)
- Health check endpoint
- Layered architecture (API → Services → Repositories → Models)

## Planned Features (Not Yet Implemented)

- [ ] Role-based access control (RBAC)
- [ ] Issue assignment to specific users
- [ ] Comments on issues
- [ ] Activity history / audit log
- [ ] Analytics dashboard
- [ ] PostgreSQL support (currently SQLite only)
- [ ] Database migrations (Alembic)

## Technologies

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- JWT (python-jose)
- Passlib (bcrypt password hashing)
- REST API
- Git

## Project Structure

```
app/
├── api/            # Route handlers (Auth, Issues, Projects)
├── core/           # Configuration, security utilities, custom exceptions
├── database/       # Database connection setup
├── models/         # SQLAlchemy ORM models
├── repositories/   # Data access layer
├── schemas/        # Pydantic schemas (request/response validation)
├── services/       # Business logic layer
└── main.py         # Application entry point
```

## Setup

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy `.env.example` to `.env` and fill in your own values:

```bash
copy .env.example .env
```

Generate a secure secret key for JWT signing:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Paste the output into the `SECRET_KEY` value in your `.env` file.

### 4. Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
Interactive API docs (Swagger UI) available at `http://127.0.0.1:8000/docs`.

## Authentication

Most endpoints require authentication. To use the API:

1. Register a user via `POST /auth/register`
2. Log in via `POST /auth/login` to receive an access token
3. Include the token in subsequent requests as a header:
   `Authorization: Bearer <your_token>`

In Swagger UI, click the **Authorize** button and enter your credentials to test protected endpoints directly.

## Running Tests

```bash
pytest
```

