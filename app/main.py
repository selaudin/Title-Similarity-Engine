# app/main.py
from fastapi import FastAPI
from app.models import Title
from app.utils import find_most_similar_title

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Title Similarity API! Please POST the json object to http://127.0.0.1:8000/find-title-similarity"}


@app.post("/find-title-similarity")
async def find_title_similarity(titles: Title):
    most_similar_title = find_most_similar_title(titles.reference_title, titles.other_titles)
    return {"top_result": most_similar_title}
