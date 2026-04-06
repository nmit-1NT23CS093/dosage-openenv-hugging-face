def grade_easy(action, state):
    return 1.0 if action.dosage_mg == 10 else 0.0

def grade_medium(action, state):
    correct = 5 if state.creatinine_level > 1.5 else 10
    return 1.0 if action.dosage_mg == correct else 0.5

def grade_hard(action, state):
    if "penicillin" in state.allergies and action.drug == "penicillin":
        return 0.0
    return 1.0 if action.dosage_mg in [5, 10] else 0.3
