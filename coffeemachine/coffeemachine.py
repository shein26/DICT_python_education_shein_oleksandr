class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def process_buy(self, choice):
        recipes = {
            '1': {'water': 250, 'milk': 0, 'coffee_beans': 16, 'cost': 4},
            '2': {'water': 350, 'milk': 75, 'coffee_beans': 20, 'cost': 7},
            '3': {'water': 200, 'milk': 100, 'coffee_beans': 12, 'cost': 6}
        }
        if choice in recipes:
            recipe = recipes[choice]
            if all(getattr(self, resource) >= amount for resource, amount in recipe.items() if resource != 'cost'):
                print("I have enough resources, making you a coffee!")
                for resource, amount in recipe.items():
                    if resource != 'cost':
                        setattr(self, resource, getattr(self, resource) - amount)
                self.money += recipe['cost']
            else:
                print("Sorry, not enough resources!")
        elif choice == 'back':
            pass
        else:
            print("Invalid choice!")

    def refill_machine(self, water, milk, coffee_beans, cups):
        self.water += water
        self.milk += milk
        self.coffee_beans += coffee_beans
        self.disposable_cups += cups

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def display_state(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"${self.money} of money")

    def process_action(self, action):
        if action == 'buy':
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
            self.process_buy(choice)
        elif action == 'fill':
            water = int(input("Write how many ml of water you want to add:\n"))
            milk = int(input("Write how many ml of milk you want to add:\n"))
            coffee_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
            cups = int(input("Write how many disposable coffee cups you want to add:\n"))
            self.refill_machine(water, milk, coffee_beans, cups)
        elif action == 'take':
            self.take_money()
        elif action == 'remaining':
            self.display_state()


coffee_machine = CoffeeMachine()

while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == 'exit':
        break
    elif action in ['buy', 'fill', 'take', 'remaining']:
        coffee_machine.process_action(action)
