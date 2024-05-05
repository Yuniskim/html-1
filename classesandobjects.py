class person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    def introduce(self):
         return f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}."

person1 = Person("Eunice", 30, "female")
intro_message = person1.introduce()
print(intro_message)