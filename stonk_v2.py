# "Crypto Trading v2" game
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 200
secret_num = 0
guesses_left = 10
total = 0

# helper function to start and restart the game
def new_game():  
    global num_range
    global secret_num
    global guesses_left   
    global total  
    #generate stock price each time
    secret_num = random.randrange(0, num_range)
    
    news = random.randint(0, 20)
    
    #ranks
    if 0 < total <= 150 or total < 0:
        print("\nYou are bearly make it!")

    elif 150 < total <= 250:
        print("\nYou are a gambler!")

    elif 250 < total <= 500:
        print("\nYou are not bad!")

    elif 500 < total <= 700:
        print("\nYou are a Pro!")

    if guesses_left >0:
        print ("\nNumber of trading date remaining is ", guesses_left, "\n")
    else:
        print ("\nGAME OVER\n")
        exist()
        
    #news effects
    if news == 0 or news == 10:
        secret_num = 200  
        print("-------------------------")
        print("\nNEWS RELEASE: Good News! Elon buys more Dogecoin!\n")
        print("-------------------------")
    elif news == 1 or news == 11:   
        secret_num = 2 
        print("-------------------------")
        print("\nNEWS RELEASE: Bad News! Elon dumps Bitcoin!\n")
        print("-------------------------")
    elif news == 2:
        secret_num = 0 
        print("-------------------------")
        print("\nNEWS RELEASE: TOO BAD! You just got rugged-pull by Elon Musk!")
        print ("\nYOU lOST EVERYTHING!\n")
        print("-------------------------")
        print ("\nGAME OVER\n")
        exist()
    else:
        print("-------------------------")
        print("\nNEWS RELEASE: No News is Good News!\n")
        print("-------------------------")
        secret_num = random.randrange(0, num_range)
    


# define event handlers for control panel
def pump():
    global guesses_left
    global total
    #new_game()
    
    # button that guess stock goes up
    pump = int(input("How much you think the price is $ "))
    if 0 < pump <= 100:
        if pump < secret_num:
            earn_gain = secret_num - pump
            guesses_left -= 1
            total += earn_gain
            print("You guess: $", str(pump))
            print("You earn: $", str(earn_gain))
            print("Your total: $", str(total))
        elif pump > secret_num:
            earn_lose = pump - secret_num
            guesses_left -= 1
            total -= earn_lose
            print("You guess: $", str(pump))
            print("You lose: $", str(earn_lose))
            print("Your total: $", str(total))
        elif pump == secret_num:
            total += 0
            guesses_left -= 1
            print("You guess: $", str(pump))
            print("You earn: $0")
            print("Your total: $", str(total))
        else:
            print("\nInstruction: please pick a price of the crypto between $1-$100\n")
            new_game() 
    else:
        print("\nInstruction: please pick a price of the crypto between $1-$100\n")
           
    new_game() 
    pass

def crash():
    global guesses_left
    global total
    #new_game()
    
    # button that guess stock goes down
    crash = int(input("How much you think the price is $ "))
    if 0 < crash <= 100:
        if crash < secret_num:
            earn_lose = secret_num - crash 
            guesses_left -= 1
            total -= earn_lose
            print("You guess: $", str(crash))
            print("You lose: $", str(earn_lose))
            print("Your total: $", str(total))
        elif crash > secret_num:
            earn_gain = crash - secret_num
            guesses_left -= 1
            total += earn_gain
            print("You guess: $", str(crash))
            print("You earn: $", str(earn_gain))
            print("Your total: $", str(total))
        elif crash == secret_num:
            total += 0
            guesses_left -= 1
            print("You guess: $", str(crash))
            print("You earn: $0")
            print("Your total: $", str(total)) 
    else:
        print("\nInstruction: please pick a price of the crypto between $1-$100\n")
         
            
    new_game()
    pass

    
def input_guess(guess):    
    # main game logic goes here	
    global guesses_left
    global secret_num 
    
    won = False
    
    print ("You guessed: ",guess)
    guesses_left = guesses_left - 1
    print ("Number of remaining guesses is ", guesses_left)
    
    if int(guess) == secret_num:       
        won = True
    elif int(guess) > secret_num:
        result = "Lower!"
    else:
        result = "Higher!"                
        
        
    if won:
        print ("That is correct! Congratulations!\n")
        new_game()
        return
    elif guesses_left == 0:
        print ("Game over. You didn't guess the number in time!") 
        new_game()
        return
    else:
        print (result)
        pass
            
    
# create frame
f = simplegui.create_frame("Game: Crypto Trading v2!", 150, 150)
f.get_canvas_textwidth('Crypto Trading', 48, 'monospace')

# register event handlers for control elements
f.add_button("Pump!", pump, 100)
f.add_button("Short!", crash, 100)	
f.add_input("Enter your guess", input_guess, 100)

# call new_game and start frame
print ("Hello to the crypto trading game. Good luck!")
print ("\nInstruction: please pick a price of the crypto between $1-$100\n")
print ("You can guess the price \n -up through Pump \n -down through Short \n -simply guess the stock price\n")
print ("\n---- New V2 has a new feature that increases a chance of winning or losing ---\n\n")
print ("-> Good news help pump the market \n-> Bad news drives the market down \n-> There is a chance you will get rugged-pull \n\n")
print ("Let's PLAY! \n\n")
#new_game()
f.start()


#Ver: V2.0 -> https://py3.codeskulptor.org/#user307_RDILfQ0hDY_20.py
#Ver: V2.1 -> https://py3.codeskulptor.org/#user307_RDILfQ0hDY_25.py
