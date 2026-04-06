from .models import Observation, Action, Reward
import random

class DosageEnv:
    def __init__(self):
        self.state_data = None
        self.done = False

    def reset(self):
        """Initialize a new patient case"""
        self.done = False
        self.state_data = {
            "patient_age": random.randint(1, 80),
            "weight": random.randint(30, 100),
            "drug": random.choice(["paracetamol", "ibuprofen"])
        }
        return self.state()

    def state(self):
        """Return current observation"""
        return Observation(
            patient_age=self.state_data["patient_age"],
            weight=self.state_data["weight"],
            drug=self.state_data["drug"],
            recommended_dose=0.0
        )

    def step(self, action: Action):
        """Agent predicts dose → environment gives reward"""

        if self.done:
            return self.state(), Reward(score=0.0), True, {"error": "Episode already done"}

        # Simple dosage logic
        if self.state_data["drug"] == "paracetamol":
            correct_dose = self.state_data["weight"] * 10
        else:
            correct_dose = self.state_data["weight"] * 5

        predicted = action.predicted_dose

        # Calculate error
        error = abs(correct_dose - predicted)

        # Reward shaping (0 to 1)
        reward_score = max(0.0, 1 - (error / correct_dose))

        self.done = True

        return self.state(), Reward(score=reward_score), True, {
            "correct_dose": correct_dose,
            "predicted_dose": predicted,
            "error": error
        }
