import random #allows the use of picking a random number in the program
import time #allows the use of a timer in the program
#variables required for the program to store for later use
high_score = 0 #sets the value of high_score to 0
trys = 1 #sets the value of trys to 1
<<<<<<< HEAD
messages_sent = 0 
first_messages = [ #2D array that hold messages to be outputted and time delay between each message
=======
messages = [ #2D array that hold messages to be outputted and time delay between each message instead of continious lines of prints and time.sleep to make program more smaller and easier to read
>>>>>>> origin/main
    ("Hello World!",2),
    ("Let's play a game.",2.75),
    ("How about...",3),
    ("A guessing game!",1),
    ("Ye that sounds fun!",3),
    ("Okay I'm thinking of a number between 1 and 100. Can you guess what it is?",4),
    ("Don't worry I'll give you some clues, along the way.",3)
]
<<<<<<< HEAD
for i in range(0,len(first_messages),1): #a count-controlled loop that outputs each of the messages in array messages, prevents the the use of having to continually writing print and delay liness of code
    msg, delay = first_messages[i] #Takes the msg and delay from the array messages based on position
=======
for i in range(0,len(messages),1): #a count-controlled loop that outputs each of the messages in array messages, makes program more efficent to fetch the message and time wait between them
    msg, delay = messages[i] #Takes the msg and delay from the array messages based on position
>>>>>>> origin/main
    print(msg) #outputs the message to the user
    time.sleep(delay) #timer used before next line of code can be run
while True: #keeps running the condition controlled loop until user guesses the correct number, so if the user wants to play again, while loop can be restarted
    value = random.randint(1, 100) #Picks a random number between 1 and 100 and stores it in value
    Guess = 0 #sets the value of Guess to 0
    Attempts = 0 #sets the value of Attempts to 0
    Fails = 0 #sets the value of Fails to 0
    while True: #keeps running the condition controlled loop until user guesses the correct number, allows user to have multiple attempts to guess the number
        if trys == 1: #checks if the value of trys is equal to 1
            Guess = input("What is your guess? ") #asks the user for a number input storing it in Guess
        elif trys != 1 and messages_sent == 0:
            Guess = input("I have thought of a new number. What is your guess?" ) #asks the user for a number input storing it in Guess
            messages_sent +=1
        else:
            Guess = input("What is your guess? ") #asks the user for a number input storing it in Guess
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
                break #breaks out of the loop 
        else: #runs block of code if Guess is not a number
            print("Just enter a number.") #outputs message to user
            Fails += 1 #increments the value of Fails by 1
    if trys != 1: #checks if the value of trys is not equal to 1
        if high_score > Attempts or high_score == 0: #checks if the value of high_score doesn't equal the value of Attempts and is less than Attempts
            high_score = Attempts
            print("New high score! You now guessed in only", Attempts, "attempts.") #outputs message to user with the value of Attempts
    elif trys == 1:
        high_score = Attempts #sets the value of high_score to the value of Attempts
        print("Your high score is", high_score, "attempts.") #outputs message to user with the value of high_score
    resp = input("Would you like to play again? (Y/N) ")  #asks the user if they want to play again
    while resp.upper() != "Y" and resp.upper() != "N": #checks if the user wants to play again
        resp = input("Please enter Y, for yes or N, for no. ") #asks the user to enter Y or N
    if resp.upper() == "Y": #checks if the user wants to play again
        trys += 1 #increments the value of trys by 1
        messages_sent = 0
        continue #re-executes the program by skipping the rest of the code and going back to the start of the loop allowing user to guess again
    else: #if the user does not want to play again
        print("Thanks for playing!") #outputs message to user and ends the program
<<<<<<< HEAD
        break
time.sleep(5) #timer used before next line of code can be run
second_messages = [ #2D array that hold messages to be outputted and time delay between each message
    ("Or maybe not yet...", 3),
    ("You've been the only one guessing the number so far.", 4),
    ("So maybe...", 2.5),
    ("I should be the one guessing the number.", 5),
    ("Don't worry, I won't cheat and read the answer you input.", 4),
    ("Maybe...", 2.5),
    ("Okay, let's start!", 2)
]
resp2 = ""
numChange = True
sent = 0
for x in range(0,len(second_messages),1): #a count-controlled loop that outputs each of the messages in array messages
    msg, delay = second_messages[x] #Takes the msg and delay from the array messages based on position
    print(msg) #outputs the message to the user
    time.sleep(delay) #timer used before next line of code can be run
while True: #keeps running the condition controlled loop until user guesses the correct number
    while resp2.upper() != "Y" and resp2.upper() != "N": #checks if the user wants to play the new game
        resp2 = input("Would you want to play this new game? (Y/N) ") #asks the user if they want to play the new game
    if resp2.upper() == "Y": #checks if the user wants to play the new game
        print("Let's play!") #outputs message to user
        num = input("Pick your number between 1 and 100 ") #asks the user to pick a number between 1 and 100
        while num.isdigit() != True or not (int(num) >=1 and int(num) <=100): #checks if the value of num is a number ant between valid boundaries        
            num = input("Your conscience tells you this isnt an actual number between 1 and 100 ")
        num = int(num)
        print("Okay let's start!") #outputs message to user
        start = 1
        end = 100
        comp_attempts = 0
        lies = 0
        while True: #keeps running the condition controlled loop until user guesses the correct number
            if numChange == True: #used to keep generating the new number
                comp_guess = random.randint(start, end)
            sec_resp = input("Is your number " + str(comp_guess) + "? Respond with either Y for yes or higher or lower. ") #asks user for their response
            if sec_resp.upper() == "Y" and comp_guess == num: #runs if the computer guesses the correct number, and fact checks it
                comp_attempts +=1
                print("I guessed your number in", str(comp_attempts), "attempts!")
                numChange = True
                if lies != 0:
                    print("However you tried to trick me", str(lies), "times")
                break
            elif sec_resp.lower() == "higher" and (comp_guess == int(num) or comp_guess > int(num)): #checks if user is lying
                print("Your conscience tells you that you are lying.")
                lies += 1
                numChange = False
            elif sec_resp.lower() == "lower" and (comp_guess == int(num) or comp_guess < int(num)): #checks if user is lying
                print("Your conscience tells you that you are lying.")
                lies += 1
                numChange = False
            elif sec_resp.upper() == "Y" and comp_guess != int(num): #checks if user is lying
                print("Your conscience tells you that you are lying.")
                lies += 1
                numChange = False
            elif (sec_resp.lower() == "higher" or sec_resp.lower() == "lower") and comp_guess == int(num): #checks if user is lying
                print("Your conscience tells you that you are lying.")
                lies += 1
                numChange = False
            elif sec_resp.lower() == "higher": #runs if user isnt lying
                start = comp_guess + 1
                comp_attempts +=1
                numChange = True
            elif sec_resp.lower() == "lower": #runs if user isnt lying
                end = comp_guess - 1
                comp_attempts +=1
                numChange = True
            else:
                print("Please enter either Y for yes or higher or lower.") #asks user for a valid input
                numChange = False
        resp = ""
        resp = input("Would you like to play again? (Y/N)")
        while resp.upper() != "Y" and resp.upper() != "N": #checks if the user wants to play again
            resp = input("Please enter Y, for yes or N, for no. ") #asks the user to enter Y or N
        if resp.upper() == "Y":
            continue
        else:
            break
    else: #if the user does not want to play the new game
        print("Thanks for playing!") #outputs message to user and ends the program
        sent += 1
        break #breaks out of the loop
if sent == 0:
    print("Thanks for playing!") #outputs message to user and ends the program  
=======
>>>>>>> origin/main
