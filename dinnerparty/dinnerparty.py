import random

def create_friend_dictionary():
    # Запитайте користувача про кількість друзів
    num_friends = int(input("Enter the number of friends joining (including you):\n"))

    # Перевірте чи кількість друзів коректна
    if num_friends <= 0:
        print("No one is joining for the party")
        return {}

    # Зчитайте імена друзів
    print("Enter the name of every friend (including you), each on a new line:")
    friends = [input("> ") for _ in range(num_friends)]

    # Ініціалізуйте словник
    friend_dictionary = {friend: 0 for friend in friends}

    # Виведіть словник
    print(friend_dictionary)
    return friend_dictionary, friends

def distribute_expenses(friends, total_amount, lucky_one):
    # Якщо немає "щасливчика", просто поділіть суму порівну
    if not lucky_one:
        amount_per_person = total_amount / len(friends)
        friend_dictionary = {friend: round(amount_per_person, 2) for friend in friends}
    else:
        # Інакше "щасливчик" отримує свою частину безкоштовно
        friend_dictionary = {friend: 0.0 for friend in friends}
        # Розділіть решту між іншими друзями
        amount_per_person = total_amount / (len(friends) - 1)
        for friend in friends:
            if friend != lucky_one:
                friend_dictionary[friend] = round(amount_per_person, 2)

    return friend_dictionary

def main():
    # Створіть словник друзів та отримайте їх імена
    friend_dictionary, friends = create_friend_dictionary()

    # Питаємо про загальну суму рахунку
    total_amount = float(input("Enter the total amount:\n"))

    # Питаємо, чи хоче користувач вибрати "щасливчика"
    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n').capitalize()

    if lucky_choice == "Yes":
        # Вибираємо "щасливчика"
        lucky_one = random.choice(list(friend_dictionary.keys()))
        print(f'{lucky_one} is the lucky one!')
    else:
        lucky_one = None

    # Оновлюємо значення у словнику
    friend_dictionary = distribute_expenses(friends, total_amount, lucky_one)

    # Виводимо оновлений словник
    print(friend_dictionary)

if __name__ == "__main__":
    main()
