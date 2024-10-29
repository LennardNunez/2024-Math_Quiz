import random

# Check if users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes (y) or no (n)")

def instruction():
    print('''\
**** Instructions ****

To begin, you will answer the questions that are being asked. The equations are only addition. 
Solve and type your answer. This quiz has 10 questions; if your answer is correct, your point(s) will add 1, 
however, if your answer is wrong, you will lose a point.

Good Luck!
    ''')

def math_quiz(num_questions):
    score = 0
    game_history = []  # To store the history of questions and answers

    print("WELCOME TO MATH QUIZ!!!")
    user_name = input("Please enter your name: ")
    print(f"Welcome to the Math Quiz, {user_name}!")

    round_number = 0  # Initialize round_number
    while True:
        round_number += 1

        # Generate two random numbers for the addition problem
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)

        while True:
            answer = input(f"Question {round_number}: What is {num1} + {num2}? (Type 'exit' to quit) ")

            if answer.lower() == 'exit':
                print("You chose to exit the quiz.")
                print(f"{user_name}, you scored {score} out of {round_number - 1}.")
                return score, game_history  # Return score and history when exiting

            try:
                answer = int(answer)
                if answer < 0:
                    print("Please enter an answer greater than or equal to 0.")
                    continue
                break
            except ValueError:
                print("Please enter a valid integer.")

        # Check if the answer is correct
        correct_answer = num1 + num2
        game_history.append((num1, num2, answer, correct_answer))  # Store the question and answer

        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
            score = max(0, score - 1)  # Prevent score from going negative

        print(f"You scored {score} so far.")

        # Stop if the user has answered the desired number of questions
        if num_questions is not None and round_number >= num_questions:
            break

    print(f"\n{user_name}, you scored {score} out of {round_number}.")

    return score, game_history  # Return score and history

# Main Routine
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

# Ask user for the number of rounds
while True:
    num_questions_input = input(
        "How many questions do you want to answer? (Press Enter for infinite or enter a number): ")
    if num_questions_input == '':
        num_questions = None  # None for infinite
        break
    elif num_questions_input.isdigit():
        num_questions = int(num_questions_input)
        if num_questions > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    else:
        print("Please enter a valid number or press Enter for infinite.")

# Start the quiz and capture score and game history
final_score, quiz_history = math_quiz(num_questions)

# Ask if the user wants to see the game history after exiting the quiz
if yes_no("Do you want to see your quiz history? (yes/no) ") == "yes":
    print("\n--- Quiz History ---")
    for num1, num2, answer, correct_answer in quiz_history:
        result = "Correct" if answer == correct_answer else "Wrong"
        print(f"{num1} + {num2} = {answer} ({result}, correct answer was {correct_answer})")
