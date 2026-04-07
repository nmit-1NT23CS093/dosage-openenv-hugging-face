from env.environment import DosageEnv
from env.tasks import get_tasks
from env.models import Action
import random

print("[START]")

env = DosageEnv()
tasks = get_tasks()

for task in tasks:
    print(f"[STEP] Running task: {task['name']}")

    env.reset()

    # Load task input
    env.state_data = task["input"]

    state = env.state()

    # Base logic
    base_dose = state.weight * 10 if state.drug == "paracetamol" else state.weight * 5

    # Add slight randomness (realistic agent)
    predicted_dose = base_dose + random.randint(-20, 20)

    action = Action(predicted_dose=predicted_dose)

    obs, reward, done, info = env.step(action)

    print(f"[STEP] Predicted: {predicted_dose}, Reward: {reward.score}")

print("[END]")