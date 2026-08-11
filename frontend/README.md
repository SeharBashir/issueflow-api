# IssueFlow — Frontend

A React frontend for the IssueFlow API: a landing/showcase page plus a working
dashboard for managing projects and issues.

## 1. Enable CORS on the backend (required)

The FastAPI backend needs to allow requests from the frontend's origin
(`http://localhost:5173`). Add this to `app/main.py`, right after `app = FastAPI(...)`:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Restart the backend after adding this.

## 2. Install dependencies

```bash
npm install
```

## 3. Run the dev server

```bash
npm run dev
```

The app runs at `http://localhost:5173`. Make sure your FastAPI backend is
running at `http://127.0.0.1:8000` at the same time (`uvicorn app.main:app --reload`).

## What's included

- `/` — landing/showcase page
- `/register`, `/login` — auth flow, stores the JWT in localStorage
- `/dashboard` — list and create projects
- `/projects/:id` — view, create, update (status), and delete issues for a project

## Notes

- The API base URL is set in `src/api.js` (`BASE_URL`) if you need to point it
  elsewhere.
- This is a demo frontend — no build tooling beyond Vite, no state library,
  just React + fetch.
