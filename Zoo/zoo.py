# zoo.py

print("I love animals!")
print("Let's check out the animals...")

# Displaying the animals in the zoo
animals = ["camel", "lion", "deer", "goose", "bat", "rabbit"]

for i, animal in enumerate(animals, start=1):
    print(f"{i}. The {animal} looks fine.")

# Displaying a specific habitat based on user input
while True:
    user_input = input("Please enter the number of the habitat you would like to view (type 'exit' to end the program): ")
    if user_input.lower() == "exit":
        print("You've reached the end of the program. See you later!")
        break

    try:
        index = int(user_input)
        if 1 <= index <= len(animals):
            print(f"\nThe {animals[index - 1]} habitat...\n")
            if animals[index - 1] == "camel":
                camel = r"""
                The camel habitat...
                Art by Joan G. Stark
                   __,  .-.  .-. 
                  (__ _ |  \/  | _ 
                     (_|||\__/||(/_| 
                        ||    ||   |_ 
                jgs    _||   _|| 
                      `""`  `""`
                Look at that!"""
                print(camel)
            elif animals[index - 1] == "lion":
                lion = r"""
                The lion habitat...
                    ,%%%%%%%,
                   ,%%/\%%%%/\%,
                  ,%%%\c "" J/%%,
                  %%%%/ d  b \%%%
                  %%%%    _  |%%%
                  `%%%%(=_Y_=)%%'
               jgs `%%%%`\7/%%%'
                     `%%%%%%%'
                The lion is roaring!"""
                print(lion)
            elif animals[index - 1] == "deer":
                deer = r"""
                The deer habitat...
                \|/    \|/
                  \    /
                   \_/  ___   ___
                   o o-'   '''   '
                    O -.         |\
                        | |'''| |
                         ||   | |
                         ||    ||
                         "     "
                Pretty good!"""
                print(deer)
            elif animals[index - 1] == "goose":
                goose = r"""
                The goose habitat...
                                                             _...--.
                                        _____......----'     .'
                                  _..-''                   .'
                                .'                       ./
                        _.--._.'                       .' |
                     .-'                           .-.'  /
                   .'   _.-.                     .  \   '
                 .'  .'   .'    _    .-.        / `./  :
               .'  .'   .'  .--' `.  |  \  |`. |     .'
            _.'  .'   .' `.'       `-'   \ / |.'   .'
         _.'  .-'   .'     `-.            `      .'
       .'   .'    .'          `-.._ _ _ _ .-.    :
      /    /o _.-'     LGB       .--'   .'   \   |
    .'-.__..-'                  /..    .`    / .'
  .'   . '                       /.'/.'     /  |
 `---'                                   _.'   '
                                       /.'    .'
                                        /.'/.'
                Beautiful!"""
                print(goose)
            elif animals[index - 1] == "bat":
                bat = r"""
                The bat habitat...
                         /'.    .'\
                       \( \__/ )/
                 ___   / (.)(.) \   ___
            _.-"`_  `-.|  ____  |.-`  _`"-._
         .-'.-'//||`'-.\  V--V  /.-'`||\\'-.'-.
        `'-'-.// ||    / .___.  \    || \\.-'-'`
              `-.||_.._|        |_.._||.-'
                       \ ((  )) /
                   jgs  '.    .'
                          `\/`
                It's doing fine."""
                print(bat)
            elif animals[index - 1] == "rabbit":
                rabbit = r"""
                The rabbit habitat...
                                 ,\
                         \\\,_
                          \` ,\
                     __,.-" =__)
                   ."        )
                ,_/   ,    \/\_
                \_|    )_-\ \_-`
            jgs    `-----` `--`
                It looks fine!"""
                print(rabbit)
            print("\n---")
        else:
            print("Please enter a valid number.")
    except ValueError:
        print("Please enter a valid number or type 'exit' to end the program.")
