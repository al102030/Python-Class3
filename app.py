class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"||A {self.year} {self.make} {self.model}||"

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.make == other.make and self.model == other.model and self.year == other.year
        return "Invalid comparison"

    def __gt__(self, other):
        if isinstance(other, Car):
            return self.year > other.year
        return "Invalid comparison"


car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

print(car1)
print(car1 == car2)
print(car1 > car2)

print(car2 > 23)
print(car1 == "||A 2020 Toyota Corolla||")

#################################################


class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
cloud.add("Java")
cloud.add("Java")
cloud.add("Java")

print(cloud["python"])
cloud["python"] = 10
print(cloud["python"])
print(len(cloud))
for tag in cloud:
    print(tag)

########################################################


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        """Public method to access the private property."""
        return self.__age

    def set_age(self, new_age):
        """Public method to modify the private property safely."""
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be positive!")


person = Person("Alice", 25)
print(person.name)
# print(person.__age)
print(person.get_age())
person.set_age(30)
print(person.get_age())
person.set_age(-5)
