# You can start with the
# Cat class or erase this
# and use your own!
class Cat:
  def __init__(self, input_name, input_breed, input_age = 0, is_cuddly = True):
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_cuddly = is_cuddly
    self.cuddly = []
  
  # Create a __repr__ method
  def __repr__(self):
    description = "This {breed} named {name} is {age} years old and has {number_of_friends} friends.".format(breed = self.breed, name = self.name, age=self.age, number_of_friends=len(self.cuddly))
    if self.is_cuddly:
      description += " {name} is a cuddly cat.".format(name = self.name)
    else:
      description += " {name} is an uncuddly cat.".format(name = self.name)
    return description

 # Create method where two
  # pets interact.
  # Ex: def name(self, pet):
  def can_cuddly(self, other_cat):
    if(other_cat.is_cuddly):
    # If the other cat can cuddle,
    # it adds other_cat to cuddle
      self.cuddly.append(other_cat)
    # The other cat also adds this 
    # specific cat to cuddle
      other_cat.cuddly.append(self)
      print("{name} become cuddle with {other_name}!".format(name = self.name, other_name = other_cat.name))
    else:
    # If the other cat is NOT cuddly,
    # no one becomes cuddly.
      print("{other_name} did not want to become cuddly with {name}!".format(name = self.name, other_name = other_cat.name))

# Create two pets.
cat_one = Cat("Leo", "Tabby", 3)
cat_two = Cat("Cookie", "Tabby", 2, False)
# Call your method below.
cat_one.can_cuddly(cat_two)
print() #print space
cat_two.can_cuddly(cat_one)
print() #print space
print(cat_one)
print() #print space
print(cat_two)

# Dog sample

class Dog:
  def __init__(self, input_name, input_breed, input_age = 0, input_friendliness=True):
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_friendly = input_friendliness
    self.friends = []
 
  def __repr__(self):
    description = "This {breed} named {name} is {age} years old and has {number_of_friends} friends.".format(breed = self.breed, name = self.name, age=self.age, number_of_friends=len(self.friends))
    if self.is_friendly:
      description += " {name} is a friendly dog.".format(name = self.name)
    else:
      description += " {name} is an unfriendly dog.".format(name = self.name)
    return description
 
  def have_birthday(self):
    self.age = self.age + 1
    print("{name} had a birthday! {name} is {age} years old.".format(name = self.name, age = self.age))
 
  def become_friends(self, other_dog):
    if(other_dog.is_friendly):
      self.friends.append(other_dog)
      other_dog.friends.append(self)
      print("{name} become friends with {other_name}!".format(name = self.name, other_name = other_dog.name))
    else:
      print("{other_name} did not want to become friends with {name}!".format(name = self.name, other_name = other_dog.name))
 
dog_one = Dog("Sparky", "Golden Retriever", 5)
dog_two = Dog("Bruno", "Chihuahua", 10, False)
 
dog_one.have_birthday()
dog_two.become_friends(dog_one)
