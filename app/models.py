# app/models.py
from typing import List
from pydantic import BaseModel


class TitleOut(BaseModel):
    top_result: str


class TitleIn(BaseModel):
    reference_title: str
    other_titles: List[str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "reference_title": "Higgs boson in particle physics",
                    "other_titles": [
                        "Best soup recipes",
                        "Basel activities",
                        "Particle physics at CERN"
                    ]
                }
            ]
        }
    }
