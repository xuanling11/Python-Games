import random


class Piggy:
    #create Piggy battle game with, name, level, max health
    def __init__(self, name, type, level = random.randint(4, 5)):
        self.name = name
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.type = type
        self.is_knocked_out = False
  
    def __repr__(self):
        # Printing a piggy will tell you its name, its type, its level and how much health it has remaining
        return "This level {level} {name} has {health} hit points remaining. They are a {type} type Piggy".format(level = self.level, name = self.name, health=self.health, type = self.type)
    
    def revive(self):
        # Reviving a piggy will flip it's status to False
        self.is_knocked_out = False
        # A revived piggy can't have 0 health. This is a safety precaution. revive() should only be called if the piggy was given some health, but if it somehow has no health, its health gets set to 1.
        if self.health == 0:
            self.health = 1
        print("{name} was revived!".format(name = self.name))

    def knock_out(self):
        # Knocking out a piggy will flip its status to True.
        self.is_knocked_out = True
        # A knocked out piggy can't have any health. This is a safety precaution. knock_out() should only be called if heath was set to 0, but if somehow the piggy had health left, it gets set to 0.
        if self.health != 0:
            self.health = 0
        print("{name} was knocked out!".format(name = self.name))
    
    def lose_health(self, amount):
        # Deducts heath from a piggy and prints the current health reamining
        self.health -= amount
        if self.health <= 0:
            #Makes sure the health doesn't become negative. Knocks out the piggy.
            self.health = 0
            self.knock_out()
        else:
            print("{name} now has {health} health.".format(name = self.name, health = self.health))

    def gain_health(self, amount):
        # Adds to a piggy's heath
        # If a piggy goes from 0 heath, then revive it
        if self.health == 0:
            self.revive()
        self.health += amount
        # Makes sure the heath does not go over the max health
        if self.health >= self.max_health:
            self.health = self.max_health
        print("{name} now has {health} health.".format(name = self.name, health = self.health))
    
    def attack(self, other_piggy):
        if self.is_knocked_out:
            print("{name} can't attack because it is knocked out!".format(name = self.name))
        #ineffective attack
        elif (self.type == "Fire" and other_piggy.type == "Water") or (self.type == "Water" and other_piggy.type == "Wind") or (self.type == "Fire" and other_piggy.type == "Ghost"):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_piggy.name, damage = round(self.level * 0.5)))
            print("It's not very effective")
            other_piggy.lose_health(round(self.level * 0.5))
        #effective attack
        elif (self.type == "Ghost" and other_piggy.type == "Water") or (self.type == "Ghost" and other_piggy.type == "Fire"):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_piggy.name, damage = round(self.level * 5)))
            print("It's very effective")
            other_piggy.lose_health(round(self.level * 5))
        #no advantage
        elif (self.type == other_piggy.type):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_piggy.name, damage = self.level))
            other_piggy.lose_health(self.level)
        else:
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_piggy.name, damage = self.level))
            other_piggy.lose_health(self.level)
#Piggy()
# Five piggies are made with different levels. (If no level is given, it is level 5)
def select_pig(number):
    if number == 1:
        return Piggy("Pig #1000", "Ghost")
    elif number == 2:
        return Piggy("Pig #1001", "Poison")
    elif number == 3:
        return Piggy("Pig #1002", "Wind")
    elif number == 4:
        return Piggy("Pig #1003", "Water")
    elif number == 5:
        return Piggy("Pig #1013", "Fire")
    else:
        return "Re-select a new pig"
    
#Getting input to get the trainers names and letting them select the Piggy they want.
trainer_one_name = input("Welcome to the world of Piggy Battle. Please enter a name for player one and hit enter.")
trainer_two_name = input("Hi, " + str(trainer_one_name) + "! Welcome! Let's find you an opponent. Enter a name for the second player. ")
trainer_one_pig = select_pig(random.randint(1, 5))
trainer_two_pig = select_pig(random.randint(1, 5))

#Fighting strategy

def fight(strategy):
    if strategy == "a":
        return Piggy.attack(trainer_one_pig, trainer_two_pig)
    elif strategy == "b":
        return Piggy.gain_health(trainer_one_pig, random.randint(1, 5))

def fight1(strategy1):
    if strategy1 == "a":
        return Piggy.attack(trainer_two_pig, trainer_one_pig)
    elif strategy1 == "b":
        return Piggy.gain_health(trainer_two_pig, random.randint(1, 5))
        

#test piggy game
print("Let's get ready to fight! Here are our two trainers")
print(trainer_one_name)
print(trainer_two_name)
print()
print("Hi, " + str(trainer_one_name) + "! Let's pick a Piggy for you! " + str(trainer_one_pig))
print("Hi, " + str(trainer_two_name) + "! Let's pick a Piggy for you! " + str(trainer_two_pig))
print()
print("Let's get battle!")

#start fighting
#player one first
trainer_one_fight = input("Player one: This is your term to fight! Please select your strategy! a: Fight  b:Get Health") 
fight(trainer_one_fight)

#player two second
trainer_two_fight = input("Player two: This is your term to fight! Please select your strategy! a: Fight  b:Get Health")

print()
fight1(trainer_two_fight)


#https://py3.codeskulptor.org/#user307_hF59lEmnPN_12.py







