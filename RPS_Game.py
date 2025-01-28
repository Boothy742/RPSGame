import random
import time

options = ["rock", "paper", "scissors"]
comp_Choice = random.choice(options)

player_Choice = input("rock, paper, scissors?")

if player_Choice == "rock":
    if comp_Choice == "paper":
        outcome = "lose"
    elif comp_Choice == "scissors":
        outcome = "win"
    else:
        outcome = "draw"

if player_Choice == "paper":
    if comp_Choice == "scissors":
        outcome = "lose"
    elif comp_Choice == "rock":
        outcome = "win"
    else:
        outcome = "draw"

if player_Choice == "scissors":
    if comp_Choice == "rock":
        outcome = "lose"
    elif comp_Choice == "paper":
        outcome = "win"
    else:
        outcome = "draw"
        
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print(player_Choice, "vs", comp_Choice)
time.sleep(1)
print(outcome)

