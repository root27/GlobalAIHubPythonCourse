class employees():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.language = []
    def add_languages(self, new_language):
        self.new_language = new_language
        self.language.append(self.new_language)

    def language_info(self):
        print("{} can speak: ".format(self.name))
        for i in self.language:
            print(i)
    def general_info(self):
        print("{} is {} years old".format(self.name, self.age))


class managers(employees):
    pass

employee1 = employees("Oguzhan", 30)
employee1.add_languages("English")
employee1.add_languages("Turkish")
print(employee1.language_info())
manager1 = managers("Emre", 40)
manager1.add_languages("Spanish")
manager1.add_languages("German")
print(manager1.language_info())
print(manager1.general_info())