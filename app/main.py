from fastapi import FastAPI
import models
from config import engine
from routes import router


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def Home():
    return "Welcome Home"


app.include_router(router, prefix="/book", tags=["book"])
