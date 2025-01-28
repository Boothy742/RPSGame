import random
import time

Rock = {"name": "rock", "rock": "draw", "paper": "win", "scissors": "lose"}
Paper = {"name": "paper", "paper": "draw", "scissors": "win", "rock": "lose"}
Scissors = {"name": "scissors", "scissors": "draw", "rock": "win", "paper": "lose"}
options = [Rock, Paper, Scissors]

comp_Choice = random.choice(options)
player_Choice = input("rock, paper, scissors?")

for i in range(3):
    print(3-i)
    time.sleep(1)
print(player_Choice, "vs", comp_Choice["name"])
time.sleep(1)
print(comp_Choice[player_Choice])
