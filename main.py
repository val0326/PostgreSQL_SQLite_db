from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/")
async def root(name: str, age: int):
    return{"message":f"Hello {name}, you are {age} years old"}

@app.post("/post")
async def post(users: list[User]):
    names = [user.name for user in users]
    return{"message": f"Hello {','.join(names)}"}