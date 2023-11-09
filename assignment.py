#object oriente programming a computer programming model that organizes software design around data, or objects, rather than functions and logic
#advantages
#troubleshooting is easy
#solves problems
#security
#productivity

#class is a template definition of thr methods and variables in a particular kind of object

#object is a combination of variables, functions, and data structures

#create a user class with properties name, age, location

class Person:
  def __init__(self, name, age, location):
    self.name = name
    self.age = age
    self.location = location

person1 = Person("emily", 22, 'kabale')

print(person1.name)
print(person1.age)
print(person1.location)

#create a new instance of the user class (a new object).
person2 = Person("ella", 36, 'mbarara')

print(person2.name)
print(person2.age)
print(person2.location)

#access the user name and age
Person=person1.name
Person=person1.age

print(f'user name: {person1.name}')
print(f'age: {person2.age}')

#create a function for the class that points a user's function
def my_location(my):
  print('my location:', my)
my_location('kabale')  