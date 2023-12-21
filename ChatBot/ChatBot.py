# chatbot.py
import datetime

bot_name = "DICT_Bot"
birth_year = datetime.datetime.now().year

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")

# Запитайте користувача про його ім'я
user_name = input("Please, remind me your name.\n> ")

# Привітайте користувача за його ім'ям
print(f"What a great name you have, {user_name}!")

# Спробуйте вгадати вік користувача
print("Let me guess your age.")
remainder3 = int(input("Enter remainder of dividing your age by 3.\n> "))
remainder5 = int(input("Enter remainder of dividing your age by 5.\n> "))
remainder7 = int(input("Enter remainder of dividing your age by 7.\n> "))

# Розрахунок віку за формулою
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

# Виведення віку
print(f"Your age is {your_age}; that's a good time to start programming!")

# Підрахунок від 0 до введеного користувачем числа
count_number = int(input("Now I will prove to you that I can count to any number you want.\n> "))

current_number = 0
while current_number <= count_number:
    print(f"{current_number} !")
    current_number += 1

print("Completed, have a nice day!")

# Тест з програмування
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

correct_answer = "2"

while True:
    user_answer = input("> ")

    if user_answer == correct_answer:
        break
    else:
        print("Please, try again.")

print("Congratulations, have a nice day!")
