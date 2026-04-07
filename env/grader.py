def grade(correct_dose, predicted_dose):
    error = abs(correct_dose - predicted_dose)

    if error < 5:
        return 1.0
    elif error < 20:
        return 0.5
    else:
        return 0.0