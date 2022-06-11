import random

possible_options = ["r", "s", "p"]


while True:
    user = input("Enter an option(r for Rock, s for Scissors or p for Paper): ")
    user = user.lower()
    
    if user not in possible_options:
        print("Error, invalid input. Pick again.")
        continue  

    computer_action = random.choice(possible_options)
    print(f"Player {user}: Computer {computer_action}") 

    if user == computer_action:
        print("It's a tie!")
        continue
    elif user == "r":
        if computer_action == "s":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! Computer win!")
        break
    elif user == "p":
        if computer_action == "r":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! Computer win!")
        break
    elif user == "s":
        if computer_action == "p":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! Computer win!")
        break  

