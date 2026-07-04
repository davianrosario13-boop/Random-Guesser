import random #allows the use of picking a random number in the program
import time #allows the use of a timer in the program
messages = [
    ("Hello World!",2),
    ("Let's play a game.",2.75),
    ("How about...",3),
    ("A guessing game!",1),
    ("Ye that sounds fun!",3),
    ("Okay I'm thinking of a number between 1 and 100. Can you guess what it is?",4),
    ("Don't worry I'll give you some clues, along the way.",3)
]
for i in range(0,len(messages),1):
    msg, delay = messages[i]
    print(msg)
    time.sleep(delay)
    if i == 5:
        value = random.randint(1, 100)
        Guess = 0
Guess = int(input("Go! "))
while value != Guess:
    if Guess < 1 or Guess > 100:
        print("I just said a number between 1 and 100.")
    elif Guess < value:
        print("My number is higher than your guess.")
    else:
        print("My number is lower than your guess.")
    Guess = int(input("Try again! "))
print("You guessed it! My number was ", str(value) + ".")