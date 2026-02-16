def average_passing_grades(grades: list[int]) -> float:
    passing_grades = [grade for grade in grades if grade >= 50]
    if not passing_grades:
        return 0.0
    return float(sum(passing_grades) / len(passing_grades))
