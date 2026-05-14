from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from myapp import db
from myapp.schemas import Postcreation
from myapp.db import engine, my_sessions, MyPost
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db.Base.metadata.create_all(bind=engine)

def get_db():
    database = my_sessions()
    try:
        yield database
    finally:
        database.close()

@app.get("/")
def getdata():
    return {"message": "Hello from fastapi!"}

@app.get("/home")
def home():
    return {"message": "Hello World!"}

@app.get("/posts")   
def all_posts(db: Session = Depends(get_db), limit: int = 10):
    posts = db.query(MyPost).limit(limit).all()
    return posts

@app.get("/posts/{id}")
def get_post(id: str, db: Session = Depends(get_db)):
   post = db.query(MyPost).filter(MyPost.id == id).first()
   if not post:
         raise HTTPException(status_code=404, detail="Post not found")
   return post

@app.post("/posts", status_code=201)
def createpost(post: Postcreation, db: Session = Depends(get_db)): 
    mynew_post = MyPost(title=post.title, content=post.content)
    db.add(mynew_post)
    db.commit()
    db.refresh(mynew_post)
    return mynew_post

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(db.text("SELECT 1"))
        return {"status": "connected"}
    except Exception as e:
        return {"status": "disconnected", "error": str(e)} 
 