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
