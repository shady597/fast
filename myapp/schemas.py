from pydantic import BaseModel
from typing import Optional

class Postcreation(BaseModel):
    title: str
    content: str

class PostResponse(Postcreation):
    id: str
    
    class Config:
        from_attributes = True

class Usercreation(BaseModel):
    username: str
    email: str