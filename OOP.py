'''
Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.

Define a repair() method that will update the condition of the podracer to "repaired".

Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.

Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
'''



# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
# defining the podracer class
class Podracer:
    def __init__(self, max_speed, condition,price):
        self.max_speed = max_speed
        self.condition = condition
        self.prive = price

# Define a repair() method that will update the condition of the podracer to "repaired".
    # defining repair class calling condition and updating the condition to repaired
    def repair(self):
        self.condition = "repaired"


#Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.

# Defining Anakind pod and inheriting the class Podracer
class Anakins_Pod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    #defining boost and multiplying max speed by 2
    def boost(self):
        self.max_speed *= 2

# Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

# defining Sebulbad Pod
class Sebulbas_Pod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    # Defining Flame Jet and setting another podracers condition to "Trashed"
    def Flame_Jet(self,another_racer):
        another_racer.condition = "trashed"


pod = Podracer(2, 'perfect', 100)
print('Condition: ', pod.condition)
pod.repair()
print('Condition after calling repair method: ', pod.condition)


'''
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
Encapsulation:
Bundles information for the individual podracers in one main class

Abstraction
not sure if this is used here


Inheritance
the individual podracers inherit the podracer class so we can reuse the code. 

Polymorphism
We use polymorphism to apply the 2x boost to anakins podracer and to give Sebulba the ability to trash another podracer

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
I do not think it would have been much easier to do this in another style. The functional way of coding would have had several more functions to recreate what the OOP style did, and would also have been a lot less readable. 

How in particular did Object Oriented Programming assist in the solving of this problem?
It assisted in solving this problem in that it allows us to make one class to define certain methods, let other classes inherit those methods, and then also change those methods without having to rewrite several functions that would end up doing the same, but with more work.
'''
