
questions = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": ["A. .html", "B. .py", "C. .css", "D. .java"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used to assign a value to a variable in Python?",
        "options": ["A. ==", "B. !=", "C. =", "D. >="],
        "answer": "C"
    },
    {
        "question": "Which Python data type stores an ordered, changeable collection of items?",
        "options": ["A. Integer", "B. String", "C. Boolean", "D. List"],
        "answer": "D"
    },
    {
        "question": "Which loop is commonly used to iterate over the items in a list?",
        "options": ["A. for loop", "B. if statement", "C. return statement", "D. def statement"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. return"],
        "answer": "C"
    },
    {
        "question": "What is the result of 10 % 3 in Python?",
        "options": ["A. 3", "B. 1", "C. 0", "D. 10"],
        "answer": "B"
    },
    {
        "question": "Which keyword checks another condition if the previous if condition is false?",
        "options": ["A. for", "B. while", "C. else if", "D. elif"],
        "answer": "D"
    },
    {
        "question": "What is the index of the first element in a Python list?",
        "options": ["A. 0", "B. 1", "C. -1", "D. 2"],
        "answer": "A"
    },
    {
        "question": "Which data structure stores information as key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    },
    {
        "question": "What does the return statement do inside a function?",
        "options": [
            "A. Displays information on the screen",
            "B. Returns a result to the caller and ends the function",
            "C. Repeats a loop",
            "D. Creates a variable"
        ],
        "answer": "B"
    }
]


def display_question(question):
    print(question["question"])

    for option in question["options"]:
        print(option)


def validate_answer(answer):
    answer = answer.upper().strip()

    if answer not in ["A", "B", "C", "D"]:
        return False

    return True


def check_answer(answer, question):
    answer = answer.upper().strip()

    if not validate_answer(answer):
        return "Invalid input. Choose from A-D."

    if answer == question["answer"]:
        return "Correct answer!"

    return "Incorrect answer."


correct_answer = 0
miss_answer = 0


def update_score(answer, question):
    global correct_answer, miss_answer

    answer = answer.upper().strip()

    if answer == question["answer"]:
        correct_answer += 1
    else:
        miss_answer += 1


def run_quiz():
    global correct_answer, miss_answer

    correct_answer = 0
    miss_answer = 0

    for question in questions:
        display_question(question)

        while True:
            answer = input("Enter your answer (A-D): ")

            result = check_answer(answer, question)

            if not validate_answer(answer):
                print(result)
                continue

            print(result)

            update_score(answer, question)

            break

        print()

    print("Quiz finished!")
    print(f"Success = {correct_answer}, Missing = {miss_answer}")


run_quiz()
