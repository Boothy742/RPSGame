import random
import time

Rock = {"name": "rock", "rock": "draw", "paper": "win", "scissors": "lose"}
Paper = {"name": "paper","paper": "draw", "scissors": "win", "rock": "lose"}
Scissors = {"name": "scissors","scissors": "draw", "rock": "win", "paper": "lose"}
options = [Rock, Paper, Scissors]

comp_Choice = random.choice(options)
player_Choice = input("rock, paper, scissors?")

print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print(player_Choice, "vs", comp_Choice["name"])
time.sleep(1)

if player_Choice == "rock": 
    print(comp_Choice["rock"])
elif player_Choice == "paper": 
    print(comp_Choice["paper"])
else: 
    print(comp_Choice["scissors"])
