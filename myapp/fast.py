from fastapi import FastAPI, HTTPException
from myapp.schemas import Postcreation

app = FastAPI()

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