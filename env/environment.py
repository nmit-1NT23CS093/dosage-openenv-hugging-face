from .models import Observation, Action, Reward
import random

class DosageEnv:
    def __init__(self):
        self.state_data = None
        self.done = False

    def reset(self):
        self.done = False
        self.state_data = {
            "patient_age": random.randint(1, 80),
            "weight": random.randint(30, 100),
            "drug": random.choice(["paracetamol", "ibuprofen"])
        }
        return self.state()

    def state(self):
        return Observation(
            patient_age=self.state_data["patient_age"],
            weight=self.state_data["weight"],
            drug=self.state_data["drug"],
            recommended_dose=0.0
        )

    def step(self, action: Action):
        if self.done:
            return self.state(), Reward(score=0.0), True, {}

        if self.state_data["drug"] == "paracetamol":
            correct_dose = self.state_data["weight"] * 10
        else:
            correct_dose = self.state_data["weight"] * 5

        error = abs(correct_dose - action.predicted_dose)
        reward_score = max(0.0, 1 - (error / correct_dose))

        self.done = True

        return self.state(), Reward(score=reward_score), True, {}
