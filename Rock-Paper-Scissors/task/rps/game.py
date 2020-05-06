import random

# Write your code here

to_win = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
key_list = list(to_win.keys())
computer = key_list[random.randint(0, 2)]
user = input()
if to_win[user] == computer:
    print("Sorry, but computer chose " + computer)
elif user == computer:
    print("There is a draw (" + user + ")")
else:
    print("Well done. Computer chose " + computer + " and failed")
