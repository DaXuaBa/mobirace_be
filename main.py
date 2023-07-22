from fastapi import FastAPI, Request
from db.database import engine


app = FastAPI()


@app.get('/')
def hello():
    return 'Hello'


#models.Base.metadata.create_all(bind=engine)