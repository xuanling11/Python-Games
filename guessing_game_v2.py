import simplegui
import random
import math


# Initializing the number of guesses.
count = 0


# helper function to start and restart the game
def new_game():   
    global count
    
    
    print ("New game. Enter the lower and upper bound of numbers.\nGood luck!\n")
    

# for calculation of minimum number of
# guesses depends upon range
def guess_num(guess):  
    global count

    
    if count < math.log(h - l + 1, 2):
        count += 1

        # taking guessing number as input
        

        # Condition testing
        if x == int(guess):
            print("Congratulations you did it in ",
                count, " try")
            # Once guessed, loop will break
            
        elif x > int(guess):
            print("You guessed is: ",guess," -> too small!")
        elif x < int(guess):
            print("You Guessed is: ",guess," -> too high!")

    # If Guessing is more than required guesses,
    # shows this output.
    if count >= math.log(h - l + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")


# create frame
f = simplegui.create_frame("Game: Guess the number!", 250, 250)
f.set_canvas_background('Green')


 
# Taking Inputs
l = int(input("Enter Lower bound:- "))
h = int(input("Enter Upper bound:- "))
x = random.randint(l, h)
print("\nYour lower bound is: ",l, "\nYour upper bound is: ",h)
print("\n\tYou've only ",
        round(math.log(h - l + 1, 2)),
        " chances to guess the integer!\n")

# register event handlers for control elements
f.add_input("Enter your guess", guess_num, 100)


# call new_game and start frame
new_game()
f.start()

#https://py3.codeskulptor.org/#user307_2HOOg390xv_5.py
