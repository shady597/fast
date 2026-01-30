from fastapi import FastAPI, HTTPException, Depends
from myapp import db
from myapp.schemas import Postcreation
from myapp.db import engine, my_sessions
from sqlalchemy.orm import Session

app = FastAPI()

db.Base.metadata.create_all(bind=engine)

def get_db():
    db = my_sessions()
    try:
        yield db
    finally:
        db.close()

my_posts = {1: {"title": "First Post", "content": "This is the first post."},
            3: {"title": "Second Post", "content": "This is the second post."},
            
            }

@app.get("/")
def getdata():
    return {"message": "Hello from fastapi!"}

@app.get("/home")
def home():
    return {"message": "Hello World!"}


@app.get("/posts")   
def all_posts(limit: int = None):
    db = my_sessions()

    return my_posts

@app.get("/posts/{id}")
def get_post(id: int):
   if id not in my_posts:
         raise HTTPException(status_code=404, detail="Post not found")
   return my_posts.get(id)

@app.post("/posts")
def createpost(post: Postcreation): 
    mynew_post = {"Title": post.title, "content": post.content}
    return mynew_post



@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        return {"status": "connected"}
    except Exception as e:
        return {"status": "disconnected", "error": str(e)} 