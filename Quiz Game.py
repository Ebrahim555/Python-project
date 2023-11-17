def start_quiz(subject):
    subject_questions = {
        "Python": [
            {
                'question': 'Who is the father of PHP?',
                'options': ['A. Wick van Rossum', 'B. Rasmus Lerdorf', 'C. Guido van Rossum', 'D. Niene Stom'],
                'correct_answer': 'C'
            },
            {
                'question': 'Which of the following is the correct extension of the Python file?',
                'options': ['A. .python ', 'B. .pl', 'C. .py', 'D. .p'],
                'correct_answer': 'C'
            },
            {
                'question': 'Which of the following character is used to give single-line comments in Python?',
                'options': ['A.//', 'B. #', 'C. ! ', 'D. /*'],
                'correct_answer': 'B'
            }
        ],
        "Html": [
            {
                'question': 'What does the abbreviation HTML stand for?',
                'options': ['A. HighText Machine Language', 'B. HyperText and links Markup Language', 'C. HyperText Markup Language', 'D. None of these'],
                'correct_answer': 'C'
            },
            {
                'question': 'Which of the following element is responsible for making the text bold in HTML?',
                'options': ['A. <pre> ', 'B. <a>', 'C. <b>', 'D. <br>'],
                'correct_answer': 'B'
            },
            {
                'question': '<input> is -',
                'options': ['A. a format tag', 'B. an empty tag', 'C. All of the above', 'D. None of the above'],
                'correct_answer': 'B'
            }
        ],
        "PHP": [
            {
                'question': 'Who is the father of PHP?',
                'options': ['A. Drek Kolkevi', 'B. Rasmus Lerdorf', 'C. Willam Makepiece', 'D. List Barely'],
                'correct_answer': 'B'
            },
            {
                'question': 'Which of the following is the correct syntax to write a PHP code?',
                'options': ['A.  <?php ?>', 'B.  < php >', 'C.  < ? php ?>', 'D. <? ?>'],
                'correct_answer': 'D'
            },
            {
                'question': 'Which of the following is the default file extension of PHP files?',
                'options': ['A.  .php', 'B.  .ph', 'C. .xml', 'D. .html'],
                'correct_answer': 'A'
            }
          ]
        }

    questions = subject_questions.get(subject)

    if not questions:
        print("unidentified subject.")
        return

    score = 0

    print("Quiz Loaded!")
    print("-----------------")
    print(subject, "questions")

    for index, question in enumerate(questions):
        print(f"\nQuestion {index + 1}:")
        print(question['question'])
        for option in question['options']:
            print(option)
        user_answer = input("Your Answer: ").upper()
        if user_answer == question['correct_answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print("\nQuiz Completed!")
    print("-------------------")
    print(f"Total Score: {score}")
    print(f"total score out of: {score}/{len(questions)}")

    retry_choice = input("\n1. Retry Quiz\n2. Exit\nEnter your choice (1-2): ")
    if retry_choice == '1':
        main()
    else:
        print("Exit.")

def main():
    print("Welcome to our Project!")
    print("Quiz Game!")

    while True:
        print("\nMain Menu:")
        print("1. Start Quiz")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            print("Select a Category:")
            print("1. Python")
            print("2. Html")
            print("3. PHP")
            subject_choice = input("Enter your choice (1-3): ")

            if subject_choice == '1':
                start_quiz("Python")
                break
            elif subject_choice == '2':
                start_quiz("Html")
                break
            elif subject_choice == '3':
                start_quiz("PHP")
                break
            else:
                print("unidentified category choice. Please try again.")
        elif choice == '2':
            print("Exit")
            break
        else:
            print("unidentified choice. Please try again.")

if __name__ == "__main__":
    main()