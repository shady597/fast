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
- PostgreSQL server

### Installation
The project uses `uv` for dependency management.
```bash
uv sync
```

### Running the Application
To start the server with auto-reload enabled:
```bash
python main.py
```
Alternatively, use uvicorn directly:
```bash
uvicorn myapp.fast:app --reload
```

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
- [ ] Fix SQLAlchemy 2.0 base class declaration in `myapp/db.py` (currently `Base = DeclarativeBase()` should be `class Base(DeclarativeBase): pass`).
- [ ] Correct case for SQLAlchemy types in `myapp/db.py` (e.g., `DateTime`, `ForeignKey`).
- [ ] Implement full CRUD logic using the database models instead of the in-memory `my_posts` dictionary.
- [ ] Add unit and integration tests.
