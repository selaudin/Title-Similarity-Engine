# app/models.py
from typing import List
from pydantic import BaseModel


class Title(BaseModel):
    reference_title: str
    other_titles: List[str]
