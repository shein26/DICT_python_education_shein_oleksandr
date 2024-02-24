import random

def generate_question(level):
    if level == 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operator = random.choice(['+', '-', '*'])
        question = f"{num1} {operator} {num2}"
        return question, eval(question)
    elif level == 2:
        num = random.randint(11, 29)
        question = f"{num}^2"
        return question, num ** 2

def save_result(name, mark, level_description):
    with open('results.txt', 'a') as file:
        file.write(f"{name}: {mark}/5 in level {level_description}.\n")

def main():
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")

    while True:
        try:
            level = int(input("> "))
            if level in [1, 2]:
                break
            else:
                print("Incorrect format. Please enter 1 or 2.")
        except ValueError:
            print("Incorrect format. Please enter a number.")

    level_description = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"

    correct_answers = 0
    total_questions = 5

    for _ in range(total_questions):
        question, answer = generate_question(level)
        user_answer = input(question + '\n> ')

        while True:
            try:
                user_answer = int(user_answer)
                break
            except ValueError:
                print("Incorrect format.")
                user_answer = input("> ")

        if user_answer == answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong format! Try again.")

    print(f"Your mark is {correct_answers}/{total_questions}. Would you like to save the result? Enter yes or no.")

    save_option = input("> ").lower()
    if save_option in ['yes', 'y']:
        print("What is your name?")
        name = input("> ")
        save_result(name, correct_answers, level_description)
        print("The results are saved in 'results.txt'.")
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
