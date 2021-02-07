class Animals():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def name_info(self):
        print("The name is {}".format(self.name))
    def show_age(self):
        print("{} is {} years old".format(self.name, self.age))
    
class Dogs(Animals):
    def __init__(self, breed, number):
        self.breed = breed
        self.number = number
   
    def get_info_dog(self):
        print("You have {} {}".format(self.number, self.breed))

class Cats(Animals):
    def __init__(self, breed, number):
        self.number = number
        self.breed = breed
    def get_info_cat(self):
        print("You have {} {}".format(self.number, self.breed))

animal1 = Animals("Duman", 3)
animal2 = Dogs("pug", 1)
animal2.name = "Lucky"
animal2.age = 2

print(animal2.get_info_dog())
print(animal2.name_info())
print(animal2.show_age())