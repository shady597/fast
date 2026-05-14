# GEMINI.md

## Project Overview
This is a FastAPI-based web application named `myproject`. It uses SQLAlchemy (v2.0+) for ORM and PostgreSQL as the database backend. The project structure is organized into a main application package `myapp`.

### Main Technologies
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
- **Database:** PostgreSQL (configured via `DATABASE_URL` in `.env`)
- **Web Server:** [Uvicorn](https://www.uvicorn.org/)
- **Dependency Management:** [uv](https://github.com/astral-sh/uv)
- **Validation:** [Pydantic](https://docs.pydantic.dev/)

## Architecture
- `main.py`: Entry point to start the development server.
- `myapp/fast.py`: Contains the FastAPI app instance, route definitions, and basic logic.
- `myapp/db.py`: Database configuration, engine setup, and SQLAlchemy models (`myposts`, `users`).
- `myapp/schemas.py`: Pydantic models for data validation and serialization.

## Building and Running

### Prerequisites
- Python >= 3.14
- Node.js >= 18
- PostgreSQL server

### Configuration
Create a `.env` file in the root directory (one has been initialized for you) and configure the following variables:
- `DATABASE_URL`: Connection string for PostgreSQL (e.g., `postgresql+psycopg2://user:password@localhost:5432/dbname`).
- `APP_HOST`: The host for the FastAPI server (default: `127.0.0.1`).
- `APP_PORT`: The port for the FastAPI server (default: `8000`).
- `APP_RELOAD`: Enable/disable auto-reload (default: `True`).

### Installation

#### Backend
The project uses `uv` for dependency management.
```bash
uv sync
```

#### Frontend
```bash
cd frontend
npm install
```

### Running the Application

To run the full-stack application, you need to start both the backend and frontend servers.

#### 1. Start Backend
From the root directory:
```bash
python main.py
```
The API will be available at `http://127.0.0.1:8000`.

#### 2. Start Frontend
From the `frontend/` directory:
```bash
npm run dev
```
The frontend will be available at `http://localhost:5173`.


### API Documentation
Once the server is running, you can access the interactive API docs at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- Redoc: `http://127.0.0.1:8000/redoc`

## Development Conventions

### Coding Style
- Follow PEP 8 guidelines.
- Use Pydantic schemas in `myapp/schemas.py` for request and response modeling.
- Database models should be defined in `myapp/db.py` using SQLAlchemy's Declarative Mapping.

### Database Operations
- Use the `get_db` dependency in `myapp/fast.py` to manage database sessions in route handlers.
- Ensure `.env` is populated with a valid `DATABASE_URL`.

### TODOs / Improvements
- [x] Fix SQLAlchemy 2.0 base class declaration in `myapp/db.py`.
- [x] Correct case for SQLAlchemy types in `myapp/db.py` (e.g., `DateTime`, `ForeignKey`).
- [x] Implement full CRUD logic using the database models instead of the in-memory `my_posts` dictionary.
- [ ] Initialize **Alembic** for database migrations.
- [ ] Add unit and integration tests using `pytest` and `httpx`.
- [ ] Implement `User` registration and management routes.
- [ ] Add `response_model` to all FastAPI routes for better data filtering.
