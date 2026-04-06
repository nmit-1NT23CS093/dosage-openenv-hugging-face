from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    age: int
    weight: float
    condition: str
    creatinine_level: float
    allergies: List[str]
    current_medications: List[str]

class Action(BaseModel):
    drug: str
    dosage_mg: float
    frequency: str

class Reward(BaseModel):
    score: float
