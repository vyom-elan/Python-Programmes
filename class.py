
#use of _init_
#__init__() function is called automatically every time the class is being used to create a new object.

class Car:
  def __init__(self, name, horsepower):
    self.name = name
    self.horsepower = horsepower

p1 = Car("MANZA", 90)

print(p1.name)
print(p1.horsepower)
