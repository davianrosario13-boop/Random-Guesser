import random
import time
print("Hello World!")
time.sleep(2)
print("Let's play a  game.")
time.sleep(2.75)
print("How about...")
time.sleep(3)
print("A guessing game!")
time.sleep(1)
print("Ye that sounds fun!")
time.sleep(3)
value = random.randint(1, 100)
Guess = 0
print(f"Okay I'm thinking of a number between 1 and 100. Can you guess what it is?")
time.sleep(4)
print("Don't worry I'll give you some clues.")
while value != Guess:
    Guess = int(input("Go!"))