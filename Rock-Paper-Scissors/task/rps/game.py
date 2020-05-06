import random

# Write your code here

to_win = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
key_list = list(to_win.keys())

while True:
    computer = key_list[random.randint(0, 2)]
    user = input()

    if user == "!exit":
        print("Bye!")
        break
    if user not in key_list:
        print("Invalid input")
    elif to_win[user] == computer:
        print("Sorry, but computer chose " + computer)
    elif user == computer:
        print("There is a draw (" + computer + ")")
    else:
        print("Well done. Computer chose " + computer + " and failed")
