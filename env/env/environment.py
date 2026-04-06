import random
from .models import Observation, Action

class DosageEnv:

    def reset(self):
        self.state = Observation(
            age=random.randint(20, 80),
            weight=random.randint(40, 100),
            condition="hypertension",
            creatinine_level=round(random.uniform(0.8, 2.0), 2),
            allergies=["penicillin"],
            current_medications=[]
        )
        return self.state

    def step(self, action: Action):
        reward = 0.0

        correct_dose = 10
        if self.state.creatinine_level > 1.5:
            correct_dose = 5

        if action.dosage_mg == correct_dose:
            reward = 1.0
        elif abs(action.dosage_mg - correct_dose) <= 2:
            reward = 0.5
        else:
            reward = -1.0

        done = True
        return self.state, reward, done, {}

    def state(self):
        return self.state
