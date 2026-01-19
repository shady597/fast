from pydantic import BaseModel

class Postcreation(BaseModel):
    id: int 
    title: str
    content: str
    created_at: int

class Usercreation(BaseModel):
    id: int 
    username: str
    email: str
    