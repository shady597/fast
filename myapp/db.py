import uuid
from sqlalchemy import create_engine, sessionmaker
from sqlalchemy import Column, String, Text, Datetime, Foreignkey 
from sqlalchemy.orm import DeclarativeBase, relationship, Session
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = "postgresql+psycopg2://postgres:$Hadyla5@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
my_sessions = sessionmaker(bind=engine)
Base = DeclarativeBase()

class myposts(Base):
    __tablename__ = "posts"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(Datetime, nullable=False)

class users(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    