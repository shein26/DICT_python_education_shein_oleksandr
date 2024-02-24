import random


def take_sticks(sticks, player):
    while True:
        try:
            if player == "John":
                turn = int(input(f"{player}, скільки олівців ви берете? (1-3): "))
            else:
                turn = random.choice([1, 2, 3])
                print(f"{player}'s turn: {turn}")

            if not 1 <= turn <= 3 or turn > len(sticks):
                raise ValueError

            break
        except ValueError:
            print("Помилка: Невірний ввід. Будь ласка, введіть ціле число від 1 до 3.")

    return sticks[:-turn]


def main():
    number = int(input("Скільки олівців бажаєте використати? "))
    sticks = "|" * number

    player1 = "John"
    player2 = "Bot"
    current_player = random.choice([player1, player2])

    print(f"{current_player}'s turn!")

    while sticks:
        print(sticks)
        sticks = take_sticks(sticks, current_player)
        current_player = player1 if current_player == player2 else player2

    print(f"{current_player} виграв!")


if __name__ == "__main__":
    main()
