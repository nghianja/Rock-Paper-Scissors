import random

name = input("Enter your name: ")
print("Hello, " + name)

score = 0
with open('rating.txt') as infile:
    for line in infile.readlines():
        line_list = line.split()
        if line_list[0] == name:
            score = int(line_list[1])
            break

options = "rock,paper,scissors".split(',')
options_input = input()
if len(options_input) > 0:
    options = options_input.split(',')

print("Okay, let's start")
while True:
    computer = options[random.randint(0, len(options) - 1)]
    user = input()

    if user == "!exit":
        print("Bye!")
        break

    if user == "!rating":
        print("Your rating: {}".format(score))
        continue

    if user not in options:
        print("Invalid input")
        continue

    comp_idx = options.index(computer)
    user_idx = options.index(user)
    if user_idx > comp_idx:
        user_idx -= len(options)

    if user == computer:
        print("There is a draw (" + computer + ")")
        score += 50
    elif comp_idx - user_idx <= len(options) // 2:
        print("Sorry, but computer chose " + computer)
    else:
        print("Well done. Computer chose " + computer + " and failed")
        score += 100
