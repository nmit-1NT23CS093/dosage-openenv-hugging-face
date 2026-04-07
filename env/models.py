from pydantic import BaseModel
from typing import List

# Observation: what the agent sees
class Observation(BaseModel):
    patient_age: int
    weight: int
    drug: str
    recommended_dose: float  # keep 0.0 (hidden from agent)


# Action: what the agent predicts
class Action(BaseModel):
    predicted_dose: float


# Reward: score given by environment
class Reward(BaseModel):
    score: float