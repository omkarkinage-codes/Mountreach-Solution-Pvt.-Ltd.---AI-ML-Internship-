# Project 4: Quiz and Examination System
# File Name: quiz_system.py

# Collect student information 
print("\nQUIZ SYSTEM LOGIN ")
student_name = input("Enter Student Name: ").strip()
roll_no = input("Enter Roll Number: ").strip()

#  Question Bank stored using fixed, immutable tuples

question_bank = [
    (
        "Which data type is IMMUTABLE in Python?",
        "A. List",
        "B. Dictionary",
        "C. Tuple",
        "D. Set",
        "C",
    ),
    (
        "What is the correct file extension for Python files?",
        "A. .pt",
        "B. .py",
        "C. .python",
        "D. .pyt",
        "B",
    ),
    (
        "Which keyword is used to create a function in Python?",
        "A. fun",
        "B. function",
        "C. define",
        "D. def",
        "D",
    ),
    (
        "Which of the following is NOT a core data structure in Python?",
        "A. Array",
        "B. List",
        "C. Dictionary",
        "D. Tuple",
        "A",
    ),
    (
        "What does the len() function do?",
        "A. Adds an item",
        "B. Returns length/size",
        "C. Deletes an item",
        "D. Converts to string",
        "B",
    ),
]


# Function to run the examination
def take_quiz():
    print(f"\nWelcome {student_name} (Roll: {roll_no})! The quiz is starting now.")

    score = 0  #  Track correct answers
    wrong_answers = []  #  Track missed questions for review

    for i, q_tuple in enumerate(question_bank, 1):
        print(f"\nQ{i}: {q_tuple[0]}")
        print(q_tuple[1])
        print(q_tuple[2])
        print(q_tuple[3])
        print(q_tuple[4])

        # Accept and user input 
        user_ans = input("Your Answer (A, B, C, or D): ").strip().upper()

        while user_ans not in ["A", "B", "C", "D"]:
            print("Invalid input! Please enter only A, B, C, or D.")
            user_ans = input("Your Answer (A, B, C, or D): ").strip().upper()

        if user_ans == q_tuple[5]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {q_tuple[5]}.")

            wrong_answers.append({"q_text": q_tuple[0], "correct_option": q_tuple[5]})

    # Calculate final score 
    total_questions = len(question_bank)
    percentage = (score / total_questions) * 100

    
    if percentage >= 50:
        result_status = "PASS"
    else:
        result_status = "FAIL"

    # Display Report
    print("\n RESULT REPORT " )
    print(f"Student Name : {student_name}")
    print(f"Roll Number  : {roll_no}")
    print(f"Final Score  : {score} / {total_questions}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Exam Status  : {result_status}")


    # Review of Incorrect Answers
    if wrong_answers:
        print("\nReview of Incorrect Answers ")
        for idx, item in enumerate(wrong_answers, 1):
            print(f"{idx}. {item['q_text']}")
            print(f"Correct Answer was: {item['correct_option']}\n")
    else:
        print("\nOutstanding! You answered all questions correctly!")


# Start the quiz automatically
take_quiz()