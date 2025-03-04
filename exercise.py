# Question 1
# Q: Write a simple if statement that checks if a number x is greater than 10. A:
x = 15
if x > 10:
    print("x is greater than 10")
# ======================================================================================

# Question 2
# Q: Write a for loop that prints the numbers from 1 to 5. A:
for i in range(1, 6):
    print(i)
# ======================================================================================

# Question 3
# Q: Write a while loop that prints "Hello, World!" 5 times. A:
count = 0
while count < 5:
    print("Hello, World!")
    count += 1
# ======================================================================================

# Question 4
# Q: Write an if-else statement that checks if a number y is even or odd. A:
y = 7
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")
# ======================================================================================

# Question 5
# Q: Write a for loop that calculates the sum of numbers from 1 to 10. A:
total = 0
for i in range(1, 11):
    total += i
print(total)
# ======================================================================================

# Question 6
# Q: Write a while loop that finds the factorial of a number n. A:
n = 5
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print(factorial)
# ======================================================================================

# Question 7
# Q: Write an if-elif-else statement that checks if a number z is positive, negative, or zero. A:
z = -3
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")
# ======================================================================================

# Question 8
# Q: Write a for loop that prints the first 10 Fibonacci numbers. A:
a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b
# ======================================================================================

# Question 9
# Q: Write a while loop that reverses the digits of a number num. A:
num = 12345
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print(reversed_num)
# ======================================================================================

# Question 10
# Q: Write a for loop and an if statement to find all prime numbers between 1 and 20. A:
for num in range(1, 21):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def __str__(self):
#         return f"||A {self.year} {self.make} {self.model}||"

#     def __eq__(self, other):
#         if isinstance(other, Car):
#             return self.make == other.make and self.model == other.model and self.year == other.year
#         return "Invalid comparison"

#     def __gt__(self, other):
#         if isinstance(other, Car):
#             return self.year > other.year
#         return "Invalid comparison"


# car1 = Car("Toyota", "Corolla", 2020)
# car2 = Car("Honda", "Civic", 2022)

# print(car1)
# print(car1 == car2)
# print(car1 > car2)

# print(car2 > 23)
# print(car1 == "||A 2020 Toyota Corolla||")

# #################################################


# class TagCloud:
#     def __init__(self):
#         self.tags = {}

#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.tags)

#     def __iter__(self):
#         return iter(self.tags)


# cloud = TagCloud()
# cloud.add("Python")
# cloud.add("python")
# cloud.add("python")
# cloud.add("Java")
# cloud.add("Java")
# cloud.add("Java")

# print(cloud["python"])
# cloud["python"] = 10
# print(cloud["python"])
# print(len(cloud))
# for tag in cloud:
#     print(tag)

# ########################################################


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     def get_age(self):
#         """Public method to access the private property."""
#         return self.__age

#     def set_age(self, new_age):
#         """Public method to modify the private property safely."""
#         if new_age > 0:
#             self.__age = new_age
#         else:
#             print("Age must be positive!")


# person = Person("Alice", 25)
# print(person.name)
# # print(person.__age)
# print(person.get_age())
# person.set_age(30)
# print(person.get_age())
# person.set_age(-5)
