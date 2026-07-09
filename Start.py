import random #allows the use of picking a random number in the program
import time #allows the use of a timer in the program
high_score = 0 #sets the value of high_score to 0
trys = 1 #sets the value of trys to 1
messages = [ #2D array that hold messages to be outputted and time delay between each message
    ("Hello World!",2),
    ("Let's play a game.",2.75),
    ("How about...",3),
    ("A guessing game!",1),
    ("Ye that sounds fun!",3),
    ("Okay I'm thinking of a number between 1 and 100. Can you guess what it is?",4),
    ("Don't worry I'll give you some clues, along the way.",3)
]
for i in range(0,len(messages),1): #a count-controlled loop that outputs each of the messages in array messages
    msg, delay = messages[i] #Takes the msg and delay from the array messages based on position
    print(msg) #outputs the message to the user
    time.sleep(delay) #timer used before next line of code can be run
while True: #keeps running the condition controlled loop until user guesses the correct number
    value = random.randint(1, 100) #Picks a random number between 1 and 100 and stores it in value
    Guess = 0 #sets the value of Guess to 0
    Attempts = 0 #sets the value of Attempts to 0
    Fails = 0 #sets the value of Fails to 0
    while True: #keeps running the condition controlled loop until user guesses the correct number
        if trys == 1: #checks if the value of trys is equal to 1
            Guess = input("What is your guess? ") #asks the user for a number input storing it in Guess
        else:
            Guess = input("I have thought of a new number. What is your guess? ") #asks the user for a number input storing it in Guess
        if Guess.isdigit(): #checks if the value of Guess is a number
            Guess = int(Guess) #converts the value of Guess to an integer
            if Guess > 100 or Guess < 1: #checks if user wrote a numbre outside the range of 1 to 100
                print("Just enter a number between 1 and 100 not outside it.") #outputs message to user
                Fails += 1 #increments the value of Fails by 1
            elif Guess < value: #checks if the value of Guess is less than the variable value
                print("Your guess is too low. Try again.") #outputs message to user
                Attempts += 1 #increments the value of Attempts by 1
            elif Guess > value: #checks if the value of Guess is bigger than the variable value
                print("Your guess is too high. Try again.") #outputs message to user
                Attempts += 1 #increments the value of Attempts by 1
            else: #if none of the other conditions are met then this block of code runs
                Attempts += 1 #increments the value of Attempts by 1
                print("Congratulations! You've guessed the number! It took you", Attempts, "attempts.") #outputs to the user message with the value of Attempts
            if Fails != 0: #checks if the value of Fails is not equal to 0
                print("However it took you", Fails, "failed attempts to understand what to do.") #outputs to the user the amount of fails they had in the program
            break #breaks out of the loop causing the program to end
        else: #runs block of code if Guess is not a number
            print("Just enter a number.") #outputs message to user
            Fails += 1 #increments the value of Fails by 1
    if trys != 1: #checks if the value of trys is not equal to 1
        if high_score < Attempts: #checks if the value of high_score is less than the value of Attempts
            print("New high score! You now guessed in only", Attempts, "attempts.") #outputs message to user with the value of Attempts
    resp = input("Would you like to play again? (Y/N) ")  #asks the user if they want to play again
    while resp.upper() != "Y" and resp.upper() != "N": #checks if the user wants to play again
        resp = input("Please enter Y, for yes or N, for no. ") #asks the user to enter Y or N
    if resp.upper() == "Y": #checks if the user wants to play again
        trys += 1 #increments the value of trys by 1
        continue #re-executes the program by skipping the rest of the code and going back to the start of the loop allowing user to guess again
    else: #if the user does not want to play again
        print("Thanks for playing!") #outputs message to user and ends the program