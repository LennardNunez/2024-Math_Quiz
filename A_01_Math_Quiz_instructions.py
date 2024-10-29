# check users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")

# Displays instructions
def display_instruction():
    print('''
    
**** Instructions ****

To begin, you will answer the questions that was being asked. The equation are only addition. 
Solve and type your answer. This quiz have a 10 questions, if your answer is
right your point(s) will add 1, however if your answer is wrong your points will
lose a point.

Good Luck!
    ''')


# Main routine
print("Welcome to the Math Quiz!!! ")
print()

# ask user if they want to see the instructions and display
# them if requested
want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    display_instruction()


print("program continues")