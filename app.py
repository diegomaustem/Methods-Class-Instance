class Person:
    current_year = 2024

    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def get_year_birth(self):
        print(self.current_year - self.age)

    @classmethod
    def by_year_birth(cls, name, year_birth):
        age = cls.current_year - year_birth
        return cls(name, age)

person = Person('Dell', 29)
print(person.get_year_birth())

person_two = Person.by_year_birth('Tiago', 1994)
print(person_two.name, person_two.age)
