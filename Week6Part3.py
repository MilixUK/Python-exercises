#######################
##
## Definition for the class Pet
##
########################
#**********************************************************
#In this exercise I am using as my base
# class Pet downloaded from BREO and amended accordingly
#with the instructions from Part2. However, only the code
# that is used to create Part 3 is thoroughly explained.
#Exceptions may occur."add dog an cat and etc..."
#**********************************************************

#Firstly, I am importing the random module
#to provide random generated age value for the Pet class
import random

class Pet:#Here I am defining the Pet class
    #The following are class attributes
    owner=""
    name=""
    alive=False
    sound=""#Variable added in Part 2
    
    #As indicated in the point 2 of the task description
    #variable "age" sholud be added to the class attributes
    age = 0
    #The following is the class constructor method.
    #This method is automatically called when a new instance
    #of a class is created
    def __init__(self,new_name):
        #When new Pet object is created the new_name paramiter
        #is assigned to the name variable,
        self.name=new_name
        #the alive status is set to True
        self.alive=True
        #and the age between 1-7 is randomy generated
        self.age = random.randrange(1,8)#.randint(1,8)may be used instead

    #This method is fruitful and returns the owner value of the Pet instance
    #The purpose of creating this method was to help in difining sameOwner
    #method
    def getOwner(self):
           return self.owner
    #Here I am defining the methods to compare Pet objects
    #accoring to their age(>,<,==)
    #The following method checks whether the age value of the object that 
    #that invoked the method is less than the age value of the object passed
    #in the function paramiter and return True if so, otherwise False.
    def __lt__(self, other):
	    return self.age < other.age
    #The following method checks whether the age value of the object that 
    #that invoked the method is grater than the age value of the object passed
    #in the function paramiter and return True if so, otherwise False.

    def __gt__(self, other):
	    return self.age > other.age
    #The following method checks whether the age value of the object that 
    #that invoked the method is equal to the age value of the object passed
    #in the function paramiter and return True if so, otherwise False.

    def __eq__(self, other):
	    return self.age == other.age
    
#Part 2 ******************************************************
    def __str__(self):
	    return "Name: " + self.name + " Owner: " + self.owner
    def setName(self, name):
	    self.name = name

    def setOwner(self, owner):
	    self.owner = owner
		
    def speak(self):
            return self.sound
        
class Dog(Pet):
    def speak(self):
        self.sound ="Woof"
        return self.sound 

class Cat(Pet):
     def speak(self):
         self.sound = "Meow"
         return self.sound
#****************************************************************************
#Here I am creating the sameOwner function, which checks whether
#the two instances(a and b) of Pet class(or subclasses) have got the same owner
def sameOwner(a, b):
    #To compare Pet instances by they owner getOwner method need to be created
    #I placed this method before Part 2 section
    if(str(a.getOwner())== str(b.getOwner())):
        return "Both have the same owner"
    #If both pets have got the same owner "Both have the same owner" is printed,
    else:
    #otherwise "Both have different owners" message is printed out on the screen.
        return "Both have different owners"
    
#Here I am defining a method findOldest, which will be used to return the name
#and the age value of the oldest pet. The method uses list of Pet objects(PetList)
#as a paramieter.2
def findOldest(PetList):
    oldestPet=PetList[0]#I am assiging the first element of the PetList oldestPet
    #The for loop iterate over rest the PetList and
    for i in range(1,len(PetList)):
        # using the __gt__ function I am checking the age variable value.
        if(PetList[i] > oldestPet):
        #If the condition is True, the object is assigned to the oldestPet,
        #otherwise loop iterate once again until i= len(PetList).
               oldestPet = PetList[i]
    #When the iteration finished, the function returns the string
    #containing the information about the oldest Pet.
    return str(oldestPet.name)+" is age of: " + str(oldestPet.age)


#######################################
pet1 = Pet("dog1")
pet1.setOwner("John")
pet2 = Pet("dog2")
pet2.setOwner("John")
pet3 = Pet("dog3")
pet3.setOwner("Mike")
pet4 = Pet("dog4")


print("pet1 ?= pet2    -->" + sameOwner(pet1,pet2))
print("pet1 ?= pet3    -->" + sameOwner(pet1,pet3))

print("\n",pet1.name,pet1.age, "\n",pet2.name, pet2.age, "\n",pet3.name,pet3.age, "\n",pet4.name,pet4.age,"\n")

print("Oldest pet: " + findOldest([pet1,pet2,pet3,pet4]))


    

