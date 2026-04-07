def get_tasks():
    return [
        {
            "name": "easy",
            "description": "Adult patient, simple dosage calculation",
            "input": {
                "patient_age": 30,
                "weight": 70,
                "drug": "paracetamol"
            }
        },
        {
            "name": "medium",
            "description": "Child patient, weight-based dosage",
            "input": {
                "patient_age": 10,
                "weight": 30,
                "drug": "ibuprofen"
            }
        },
        {
            "name": "hard",
            "description": "Child + special adjustment case",
            "input": {
                "patient_age": 5,
                "weight": 20,
                "drug": "paracetamol"
            }
        }
    ]