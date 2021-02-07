class Animals():
    def __init__(self, type, number):
        self.type = type
        self.number = number
    def get_info_animals(self):
        print("You have {} animals at home".format(self.number))

class Dogs(Animals):
    def __init__(self, type, number, breed):
        super().__init__(type, number)
        self.breed = breed
    def get_info_dog(self):
        print("You have {} {}".format(self.number, self.breed))

class Cats(Animals):
    def __init__(self, type, number, breed):
        super().__init__(type, number)
        self.breed = breed
    def get_info_cat(self):
        print("You have {} {}".format(self.number, self.breed))


anims = Animals("cat", 2)
print(anims.get_info_animals())

my_cat = Cats("cat", 2, "british")
print(my_cat.get_info_cat())