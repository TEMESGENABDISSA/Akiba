students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]


def validate_score(score):
    return 0 <= score <= 100


def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculate_average(students):
    total = 0

    for student in students:
        total += student["score"]

    return total / len(students)


def find_highest_lowest(students):
    scores = [student["score"] for student in students]
    return max(scores), min(scores)


def count_passed_failed(students):
    passed = 0
    failed = 0

    for student in students:
        if student["score"] >= 50:
            passed += 1
        else:
            failed += 1

    return passed, failed


def generate_report(students):
    print("STUDENT REPORT")
    print("--------------")

    for student in students:
        name = student["name"]
        score = student["score"]

        if validate_score(score):
            print(name, "-", score, "-", calculate_grade(score))
        else:
            print(name, "- Invalid score")

    average = calculate_average(students)
    highest, lowest = find_highest_lowest(students)
    passed, failed = count_passed_failed(students)

    print("\nCLASS SUMMARY")
    print("-------------")
    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Passed:", passed)
    print("Failed:", failed)


generate_report(students)