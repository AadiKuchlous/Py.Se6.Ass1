class animal():
    def __init__(self, name, types):
        self.name = name
        self.types = types

    def display(self):
        print("You have a pet", self.types)
        print("Your pet's name is", self.name)

class fruit_Flav():
    def __init__(self, fruit, flav):
        self.fruit = fruit
        self.flav = flav

    def display(self):
        print(self.fruit, 'is', self.flav)

animals = input("What is the name of you pet? \n")
types = input('what animal? \n')

f = input("Tell me the name of a fruit \n")
fl = input("Tell me its flavour \n")

f1 = input("Tell me the name of another fruit \n")
fl1 = input("Tell me its flavour \n")


ff = fruit_Flav(f, fl)
ff.display()

ff1 = fruit_Flav(f1, fl1)
ff1.display()

a1 = animal(animals, types)
a1.display()
