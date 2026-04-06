import os
from openai import OpenAI
from env.environment import DosageEnv
from env.models import Action

client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

env = DosageEnv()

print("[START]")

for task in ["easy", "medium", "hard"]:
    state = env.reset()

    action = Action(drug="Lisinopril", dosage_mg=10, frequency="daily")

    obs, reward, done, _ = env.step(action)

    print(f"[STEP] task={task}, reward={reward}")

print("[END]")
