from .models import Observation, Action, Reward
import random

class DosageEnv:
    def __init__(self):
        self.state_data = None
        self.done = False
        self.correct_dose = 0

    def reset(self):
        self.done = False

        # Task difficulty selection
        self.task = random.choice(["easy", "medium", "hard"])

        # Generate patient
        self.state_data = {
            "patient_age": random.randint(1, 80),
            "weight": random.randint(30, 100),
            "drug": random.choice(["paracetamol", "ibuprofen"])
        }

        # Define correct dosage logic
        if self.state_data["drug"] == "paracetamol":
            self.correct_dose = self.state_data["weight"] * 10
        else:
            self.correct_dose = self.state_data["weight"] * 5

        # Hard task adjustment (real-world complexity)
        if self.task == "hard" and self.state_data["patient_age"] < 12:
            self.correct_dose *= 0.8  # pediatric adjustment

        return self.state()

    def state(self):
        return Observation(
            patient_age=self.state_data["patient_age"],
            weight=self.state_data["weight"],
            drug=self.state_data["drug"],
            recommended_dose=0.0  # hidden from agent
        )

    def step(self, action: Action):
        if self.done:
            return self.state(), Reward(score=0.0), True, {"msg": "Episode done"}

        predicted = action.predicted_dose

        # Calculate error
        error = abs(self.correct_dose - predicted)

        # Reward shaping
        reward_score = max(0.0, 1 - (error / self.correct_dose))

        # Penalty for dangerous overdose
        if predicted > self.correct_dose * 1.5:
            reward_score *= 0.5

        # Bonus for very accurate prediction
        if error < 5:
            reward_score = 1.0

        self.done = True

        return (
            self.state(),
            Reward(score=round(reward_score, 3)),
            True,
            {
                "correct_dose": self.correct_dose,
                "task": self.task,
                "error": error
            }
        )