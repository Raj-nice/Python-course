import random

while True:
    user_action = input ("Enter rock, paper, scisssors;")

    possible_actions = ["rock","paper","scissors"]

    computer_action = random.choice(possible_actions)
    print(f"\nYou choose{user_action}{computer_action} /n")

    if user_action == computer_action:
        print(f"Both players selcted {user_action}. It's a tie")
    elif user_action == "rock":
        if computer_action == "scissors":
            print ("Rock smashes scissors! You win")
        else:
            print("Paper covers rock! You lose")
    elif user_action == "paper":
        if computer_action == "rock":
            print ("Scissors cuts paper! You win!")
        else:
            print("Rock smashes schssors! You lose")
    elif user_action == "scissors":
        if computer_action == "paper":
            print ("Scissor cuts paper! You win!")
        else:
            print(" Rock smashes scissors! You lose")