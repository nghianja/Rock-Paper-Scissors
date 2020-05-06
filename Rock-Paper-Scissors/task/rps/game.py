import random

# Write your code here

to_win = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
key_list = list(to_win.keys())

name = input("Enter your name: ")
print("Hello, " + name)

score = 0

with open('rating.txt') as infile:
    for line in infile.readlines():
        line_list = line.split()
        if line[0] == name:
            score = int(line[1])

while True:
    computer = key_list[random.randint(0, 2)]
    user = input()

    if user == "!exit":
        print("Bye!")
        break

    if user == "!rating":
        print("Your rating: {}".format(score))
    elif user not in key_list:
        print("Invalid input")
    elif to_win[user] == computer:
        print("Sorry, but computer chose " + computer)
    elif user == computer:
        print("There is a draw (" + computer + ")")
        score += 50
    else:
        print("Well done. Computer chose " + computer + " and failed")
        score += 100
