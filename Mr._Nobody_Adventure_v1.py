# "Mr. Nobody Adventure v1" game
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math


attack = 0 #range up to 100
defense = 0
defense_factor = 0
magic = 0
magic_factor = 0
health = 0
enemy_attack = 0
enemy_defense = 0
enemy_magic = 0
enemy_health = 0
level = 0
XP = 0
fight_list = ["Magic Elemental", "Lightning Elemental", "Water Elemental", "Ice Elemental", "Fire Elemental", "Energy Elemental", "Earth Elemental"]



# helper function to start and restart the game
def new_game():  
    global attack
    global defense
    global defense_factor   
    global magic
    global magic_factor   
    global health
    global enemy_attack
    global enemy_defense   
    global enemy_magic
    global enemy_health
    global level   
    global fight_list
    
    
    enemy = random.choice(fight_list)
    
    if enemy == "Magic Elemental":
        enemy_attack = 5
        enemy_defense = 6
        enemy_magic = 9
        enemy_health = 15
        print("\n-------------------------")
        print("\nYou encounter Magic Elemental!")
    elif enemy == "Ice Elemental":
        enemy_attack = 5
        enemy_defense = 6
        enemy_magic = 9
        enemy_health = 15
        print("\n-------------------------")
        print("\nYou encounter Ice Elemental!")
    elif enemy == "Water Elemental":
        enemy_attack = 4
        enemy_defense = 6
        enemy_magic = 5
        enemy_health = 20
        print("\n-------------------------")
        print("\nYou encounter Water Elemental!")
    elif enemy == "Fire Elemental":
        enemy_attack = 8
        enemy_defense = 7
        enemy_magic = 4
        enemy_health = 15
        print("\n-------------------------")
        print("\nYou encounter Fire Elemental!")
    elif enemy == "Earth Elemental":
        enemy_attack = 5
        enemy_defense = 8
        enemy_magic = 5
        enemy_health = 15
        print("\n-------------------------")
        print("\nYou encounter Earth Elemental!")
    elif enemy == "Lightning Elemental":
        enemy_attack = 10
        enemy_defense = 9
        enemy_magic = 9
        enemy_health = 20
        print("\n-------------------------")
        print("\nYou encounter Lightning Elemental!")
    
'''    
    if role == 1:
        attack = 10
        defense = 8
        magic = 3
        health = 15
        print("Hello, Mr. Nobody!")
        print("\nYou pick a Knight as your role!")
        print("\nHere is your abilities:")
        print("\n-> attack = 10\n-> defense = 8\n-> magic = 3\n-> health = 15")
        print("\nLet's train your abilities!")
    elif role == 2:
        attack = 8
        defense = 10
        magic = 7
        health = 15
        print("Hello, Mr. Nobody!")
        print("\nYou pick a Ranger as your role!")
        print("\nHere is your abilities:")
        print("\n-> attack = 8\n-> defense = 10\n-> magic = 7\n-> health = 15")
        print("\nLet's train your abilities!")
    elif role == 3:
        attack = 6
        defense = 7
        magic = 10
        health = 15
        print("Hello, Mr. Nobody!")
        print("\nYou pick a Wizard as your role!") 
        print("\nHere is your abilities:")
        print("\n-> attack = 6\n-> defense = 7\n-> magic = 10\n-> health = 15")
        print("\nLet's train your abilities!")
    else:
        print("Hello, Mr. Nobody!")
        print("Pick a role: 1-Knight, 2-Ranger, 3-Wizard")
'''    

def level_up():
    pass

'''
def pick_fight():
    enemy = random.choice(fight_list)
    #random pick a list of enemy
    if enemy == "Magic Elemental":
        enemy_attack = 5
        enemy_defense = 6
        enemy_magic = 9
        enemy_health = 15
        print("\nYou encounter Magic Elemental!") 
        #print("\nHere is the abilities:")
        #print("\n-> attack = 5\n-> defense = 6\n-> magic = 9\n-> health = 15")
        print("\nKILL IT!\n")
    elif enemy == "Ice Elemental":
        enemy_attack = 5
        enemy_defense = 6
        enemy_magic = 9
        enemy_health = 15
        print("\nYou encounter Ice Elemental!") 
        #print("\nHere is the abilities:")
        #print("\n-> attack = 5\n-> defense = 6\n-> magic = 9\n-> health = 15")
        print("\nKILL IT!\n")
    elif enemy == "Water Elemental":
        enemy_attack = 4
        enemy_defense = 6
        enemy_magic = 5
        enemy_health = 20
        print("\nYou encounter Water Elemental!") 
        #print("\nHere is the abilities:")
        #print("\n-> attack = 4\n-> defense = 6\n-> magic = 5\n-> health = 20")
        print("\nKILL IT!\n")
    elif enemy == "Fire Elemental":
        enemy_attack = 8
        enemy_defense = 7
        enemy_magic = 4
        enemy_health = 15
        print("\nYou encounter Ice Elemental!") 
        #print("\nHere is the abilities:")
        #print("\n-> attack = 8\n-> defense = 7\n-> magic = 4\n-> health = 15")
        print("\nKILL IT!\n")
    elif enemy == "Earth Elemental":
        enemy_attack = 5
        enemy_defense = 8
        enemy_magic = 5
        enemy_health = 15
        print("\nYou encounter Earth Elemental!") 
        #print("\nHere is the abilities:")
        #print("\n-> attack = 5\n-> defense = 8\n-> magic = 5\n-> health = 15")
        print("\nKILL IT!\n")
    elif enemy == "Lightning Elemental":
        enemy_attack = 10
        enemy_defense = 9
        enemy_magic = 9
        enemy_health = 20
        print("\nYou encounter Lightning Elemental!") 
        #print("\nHere is the abilities:")
        #print("\n-> attack = 10\n-> defense = 9\n-> magic = 9\n-> health = 20")
        print("\nKILL IT!\n")
    
    pass
'''
def kill():    
    global health
    global enemy_health
    global enemy
    global attack
    defense_factor = random.random()/1000
    magic_factor = random.random()/1000
    
#    enemy = random.choice(fight_list)
#    if enemy == "Magic Elemental":
#        print("\n-------------------------")
#        print("\nYou encounter Magic Elemental!")
#    elif enemy == "Ice Elemental":
#        print("\n-------------------------")
#        print("\nYou encounter Ice Elemental!")
#    elif enemy == "Water Elemental":
#        print("\n-------------------------")
#        print("\nYou encounter Water Elemental!")
#    elif enemy == "Fire Elemental":
#        print("\n-------------------------")
#        print("\nYou encounter Fire Elemental!")
#    elif enemy == "Earth Elemental":
#        print("\n-------------------------")
#        print("\nYou encounter Earth Elemental!")
#    elif enemy == "Lightning Elemental":
#        print("\n-------------------------")
#        print("\nYou encounter Lightning Elemental!")
###    
    
    if role == 1:        
        if enemy == "Magic Elemental":            
            health = health-5-9*magic_factor+8*defense_factor 
            enemy_health = enemy_health-10-3*magic_factor+9*defense_factor
            print("\n-------------------------")
            print("\nYou encounter Magic Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Magic Elemental!")
            #print("\nYour HP: ", int(health))
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Magic Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou KILL the Magic Elemental!")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health))
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Magic Elemental! The HP:", int(enemy_health))
        elif enemy == "Ice Elemental":           
            health = health-5-9*magic_factor+8*defense_factor 
            enemy_health = enemy_health-10-3*magic_factor+9*defense_factor
            print("\n-------------------------")
            print("\nYou encounter Ice Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Ice Elemental!")
            #print("\nYour HP: ", int(health))
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Ice Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou KILL the Ice Elemental!")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health)) 
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Ice Elemental! The HP:", int(enemy_health))
        elif enemy == "Water Elemental":            
            health = health-5-9*magic_factor+8*defense_factor 
            enemy_health = enemy_health-10-3*magic_factor+9*defense_factor
            print("\n-------------------------")
            print("\nYou encounter Water Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Water Elemental!")
            #print("\nYour HP: ", int(health))
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Water Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou KILL the Water Elemental!")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health))
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Water Elemental! The HP:", int(enemy_health))
        elif enemy == "Fire Elemental":            
            health = health-5-9*magic_factor+8*defense_factor 
            enemy_health = enemy_health-10-3*magic_factor+9*defense_factor 
            print("\n-------------------------")
            print("\nYou encounter Fire Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Fire Elemental!")
            #print("\nYour HP: ", int(health))
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Fire Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou KILL the Fire Elemental! The HP: 0")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health))
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Fire Elemental! The HP:", int(enemy_health))
        elif enemy == "Earth Elemental":            
            health = health-5-9*magic_factor+8*defense_factor 
            enemy_health = enemy_health-10-3*magic_factor+9*defense_factor 
            print("\n-------------------------")
            print("\nYou encounter Earth Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Earth Elemental!")
            #print("\nYour HP: ", int(health))
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Earth Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou attack KILL the Earth Elemental!")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health))
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Earth Elemental! The HP:", int(enemy_health))
        elif enemy == "Lightning Elemental":            
            health = health-5-9*magic_factor+8*defense_factor 
            enemy_health = enemy_health-10-3*magic_factor+9*defense_factor 
            print("\n-------------------------")
            print("\nYou encounter Lightning Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Lightning Elemental!")
            #print("\nYour HP: ", int(health))
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Lightning Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou KILL the Lightning Elemental!")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health))
                print("\nYou learn the secrete spelling: Rugged-Pull! And your strenth is 100!")
                attack += 100
                print("\nYour attack now is:",attack)
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Lightning Elemental! The HP:", int(enemy_health))
        
           
    elif role == 2:        
        if enemy == "Magic Elemental":            
            health = health-5-9*magic_factor+10*defense_factor 
            enemy_health = enemy_health-8-7*magic_factor+9*defense_factor
            print("\n-------------------------")
            print("\nYou encounter Magic Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Magic Elemental!")
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Magic Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou KILL the Magic Elemental!")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health))
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Magic Elemental! The HP:", int(enemy_health))
        elif enemy == "Ice Elemental":           
            health = health-5-9*magic_factor+10*defense_factor 
            enemy_health = enemy_health-8-7*magic_factor+9*defense_factor
            print("\n-------------------------")
            print("\nYou encounter Ice Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Ice Elemental!")
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Ice Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\n-------------------------")
                print("\nYou KILL the Ice Elemental!")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health)) 
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Ice Elemental! The HP:", int(enemy_health))
        elif enemy == "Water Elemental":            
            health = health-5-9*magic_factor+10*defense_factor 
            enemy_health = enemy_health-8-7*magic_factor+9*defense_factor
            print("\n-------------------------")
            print("\nYou encounter Water Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Water Elemental!")
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Water Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou KILL the Water Elemental!")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health))
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Water Elemental! The HP:", int(enemy_health))
        elif enemy == "Fire Elemental":            
            health = health-5-9*magic_factor+10*defense_factor 
            enemy_health = enemy_health-8-7*magic_factor+9*defense_factor 
            print("\n-------------------------")
            print("\nYou encounter Fire Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Fire Elemental!")
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Fire Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou KILL the Fire Elemental! The HP: 0")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health))
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Fire Elemental! The HP:", int(enemy_health))
        elif enemy == "Earth Elemental":            
            health = health-5-9*magic_factor+10*defense_factor 
            enemy_health = enemy_health-8-7*magic_factor+9*defense_factor 
            print("\n-------------------------")
            print("\nYou encounter Earth Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Earth Elemental!")
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Earth Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou attack KILL the Earth Elemental!")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health))
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Earth Elemental! The HP:", int(enemy_health))
        elif enemy == "Lightning Elemental":            
            health = health-5-9*magic_factor+10*defense_factor 
            enemy_health = enemy_health-8-7*magic_factor+9*defense_factor 
            print("\n-------------------------")
            print("\nYou encounter Lightning Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Lightning Elemental!")
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Lightning Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou KILL the Lightning Elemental!")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health))
                print("\nYou learn the secrete spelling: Rugged-Pull! And your strenth is 100!")
                attack += 100
                print("\nYour attack now is:",attack)
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Lightning Elemental! The HP:", int(enemy_health))
    
    elif role == 3:        
        if enemy == "Magic Elemental":            
            health = health-5-9*magic_factor+7*defense_factor 
            enemy_health = enemy_health-6-10*magic_factor+9*defense_factor
            print("\n-------------------------")
            print("\nYou encounter Magic Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Magic Elemental!")
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Magic Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou KILL the Magic Elemental!")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health))
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Magic Elemental! The HP:", int(enemy_health))
        elif enemy == "Ice Elemental":           
            health = health-5-9*magic_factor+7*defense_factor 
            enemy_health = enemy_health-6-10*magic_factor+9*defense_factor
            print("\n-------------------------")
            print("\nYou encounter Ice Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Ice Elemental!")
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Ice Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou KILL the Ice Elemental!")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health)) 
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Ice Elemental! The HP:", int(enemy_health))
        elif enemy == "Water Elemental":            
            health = health-5-9*magic_factor+7*defense_factor 
            enemy_health = enemy_health-6-10*magic_factor+9*defense_factor
            print("\n-------------------------")
            print("\nYou encounter Water Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Water Elemental!")
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Water Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou KILL the Water Elemental!")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health))
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Water Elemental! The HP:", int(enemy_health))
        elif enemy == "Fire Elemental":            
            health = health-5-9*magic_factor+7*defense_factor 
            enemy_health = enemy_health-6-10*magic_factor+9*defense_factor 
            print("\n-------------------------")
            print("\nYou encounter Fire Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Fire Elemental!")
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Fire Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou KILL the Fire Elemental! The HP: 0")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health))
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Fire Elemental! The HP:", int(enemy_health))
        elif enemy == "Earth Elemental":            
            health = health-5-9*magic_factor+7*defense_factor 
            enemy_health = enemy_health-6-10*magic_factor+9*defense_factor 
            print("\n-------------------------")
            print("\nYou encounter Earth Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Earth Elemental!")
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Earth Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou attack KILL the Earth Elemental!")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health))
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Earth Elemental! The HP:", int(enemy_health))
        elif enemy == "Lightning Elemental":            
            health = health-5-9*magic_factor+7*defense_factor 
            enemy_health = enemy_health-6-10*magic_factor+9*defense_factor 
            print("\n-------------------------")
            print("\nYou encounter Lightning Elemental!") 
            print("\nYou got attacked!")   
            print("\nYou attack Lightning Elemental!")
            print("\n-------------------------")
            if int(health)<0:
                print("\n-------------------------")
                print("\nYou got kill by the Lightning Elemental!")
                print("\nYou Lose!")
                print("\n--GAME OVER--\n")
                exit()
            elif int(enemy_health)<0:
                print("\nYou KILL the Lightning Elemental!")
                print("\nYou WIN!")
                print("\nYour HP: ", int(health))
                print("\nYou learn the secrete spelling: Rugged-Pull! And your strenth is 100!")
                attack += 100
                print("\nYour attack now is:",attack)
                print("\nContinue training ...\n")
                print("-------------------------")
                new_game()
            else:
                print("\nYou got attacked! You HP: ", int(health))   
                print("\nYou attack Lightning Elemental! The HP:", int(enemy_health))
    
    #new_game()
    pass

def heal():
    global health
    global magic
    
    if role == 1:
        if health < 15:
            health += magic
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nYou recover HP to: ", int(health),"\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            #kill()
        else:
            print("\nYou has been fully recover !\n")
            kill()
    elif role == 2:
        if health < 15:
            health += magic
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nYou recover HP to: ", int(health),"\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            #kill()
        else:
            print("\nYou has been fully recover !\n")
            kill()
    elif role == 3:
        if health < 15:
            health += magic
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nYou recover HP to: ", int(health),"\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            #kill()
        else:
            print("\nYou has been fully recover !\n")
            kill()

            
def power_up():            
    global attack
    global magic
    
    if role == 1:
        if attack < 25:
            attack += magic
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nYou power up your strength: ", int(attack),"\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            #kill()
        else:
            print("\nThat is the maximum strength!\n")
            kill()
    elif role == 2:
        if attack < 15:
            attack += magic
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nYou recover HP to: ", int(attack),"\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            #kill()
        else:
            print("\nThat is the maximum strength!\n")
            kill()
    elif role == 3:
        if attack < 15:
            attack += magic
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nYou recover HP to: ", int(attack),"\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            #kill()
        else:
            print("\nThat is the maximum strength!\n")
            kill()
   
    
            
def earth_king():
    global enemy_attack
    global enemy_defense   
    global enemy_magic
    global enemy_health
    
    enemy_attack = 15
    enemy_defense = 15
    enemy_magic = 10
    enemy_health = 30
    
    pass

def water_queen():    
    pass

def earth_lord():    
    pass

################################################################    
# create frame
f = simplegui.create_frame("Mr. Nobody Advanture v1!", 150, 250)
f.get_canvas_textwidth('Mr. Nobody Advanture v1', 48, 'monospace')

    
# call new_game and start frame
print("-------------------------------")
print ("Mr. Nobody Advanture v1 game")
print("-------------------------------")
print ("\nHello to the world.\n")
print("You are the Mr. Nobody!")
print ("\nThere are 4 elements control the world:") 
print ("\n-Earth: the strongest element for the defense")
print ("-Water: the fatest element for the heal")
print ("-Fire: the mighty element for the power")
print ("-Lightning: the mystery element that no one master")
print ("\nYou will have to defeat Earth King, Water Queen and Fire Lord!")
print ("\nGood luck! Warrior!")
print ("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print ("\nInstruction: F**k... \n\nThere is no time for instruction...\n\nKeep healing AND power-up to stay alive!")
print ("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print ("\n...")
print ("Let's FIGHT! \n\n")

role = int(input("Pick a role: 1-Knight, 2-Ranger, 3-Wizard"))
if role == 1:
    attack = 10
    defense = 8
    magic = 3
    health = 15
    print("Hello, Mr. Nobody!")
    print("\nYou pick a Knight as your role!")
    print("\nHere is your abilities:")
    print("\n-> attack = 10\n-> defense = 8\n-> magic = 3\n-> health = 15")
    print("\nLet's train your abilities!")
elif role == 2:
    attack = 8
    defense = 10
    magic = 7
    health = 15
    print("Hello, Mr. Nobody!")
    print("\nYou pick a Ranger as your role!")
    print("\nHere is your abilities:")
    print("\n-> attack = 8\n-> defense = 10\n-> magic = 7\n-> health = 15")
    print("\nLet's train your abilities!")
elif role == 3:
    attack = 6
    defense = 7
    magic = 10
    health = 15
    print("Hello, Mr. Nobody!")
    print("\nYou pick a Wizard as your role!") 
    print("\nHere is your abilities:")
    print("\n-> attack = 6\n-> defense = 7\n-> magic = 10\n-> health = 15")
    print("\nLet's train your abilities!")
else:
    print("Hello, Mr. Nobody!")
    print("Pick a role: 1-Knight, 2-Ranger, 3-Wizard")

#enemy = random.choice(fight_list)
enemy = "Lightning Elemental"
if enemy == "Magic Elemental":
    enemy_attack = 5
    enemy_defense = 6
    enemy_magic = 9
    enemy_health = 15
    #print("\n-------------------------")
    #print("\nYou encounter Magic Elemental!")
elif enemy == "Ice Elemental":
    enemy_attack = 5
    enemy_defense = 6
    enemy_magic = 9
    enemy_health = 15
    #print("\n-------------------------")
    #print("\nYou encounter Ice Elemental!")
elif enemy == "Water Elemental":
    enemy_attack = 4
    enemy_defense = 6
    enemy_magic = 5
    enemy_health = 20
    #print("\n-------------------------")
    #print("\nYou encounter Water Elemental!")
elif enemy == "Fire Elemental":
    enemy_attack = 8
    enemy_defense = 7
    enemy_magic = 4
    enemy_health = 15
    #print("\n-------------------------")
    #print("\nYou encounter Fire Elemental!")
elif enemy == "Earth Elemental":
    enemy_attack = 5
    enemy_defense = 8
    enemy_magic = 5
    enemy_health = 15
    #print("\n-------------------------")
    #print("\nYou encounter Earth Elemental!")
elif enemy == "Lightning Elemental":
    enemy_attack = 10
    enemy_defense = 9
    enemy_magic = 9
    enemy_health = 20
    #print("\n-------------------------")
    #print("\nYou encounter Lightning Elemental!")

# register event handlers for control elements
#f.add_button("Pick a fight!", pick_fight, 100)
f.add_button("Pick a fight and Kill it!", kill, 100)	
f.add_button("Use magic to heal!", heal, 100)
f.add_button("Power up your fight!", power_up, 100)
#f.add_input("Enter your guess", input_guess, 100)   
    
    
'''   
#test function
#enemy = "Magic Elemental"
#enemy = "Lightning Elemental"
enemy = random.choice(fight_list)
if enemy == "Magic Elemental":
    enemy_attack = 5
    enemy_defense = 6
    enemy_magic = 9
    enemy_health = 15
elif enemy == "Ice Elemental":
    enemy_attack = 5
    enemy_defense = 6
    enemy_magic = 9
    enemy_health = 15
elif enemy == "Water Elemental":
    enemy_attack = 4
    enemy_defense = 6
    enemy_magic = 5
    enemy_health = 20
elif enemy == "Fire Elemental":
    enemy_attack = 8
    enemy_defense = 7
    enemy_magic = 4
    enemy_health = 15
elif enemy == "Earth Elemental":
    enemy_attack = 5
    enemy_defense = 8
    enemy_magic = 5
    enemy_health = 15
elif enemy == "Lightning Elemental":
    enemy_attack = 10
    enemy_defense = 9
    enemy_magic = 9
    enemy_health = 20
'''
#new_game()

#https://py3.codeskulptor.org/#user307_NdjI7u7UYl_118.py
