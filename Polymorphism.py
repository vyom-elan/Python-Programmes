#polymorphism example
class Vehicle:
  def __init__(self, make, model):
    self.make = make
    self.model = model
  def move(self):
    print("Quater mile time!")
class Car(Vehicle):
  pass
class Boat(Vehicle):
  def move(self):
    print("Sail off!")
class Plane(Vehicle):
  def move(self):
    print("Take off!")
car1 = Car("Nissan", "GTR") #Create a Car object
boat1 = Boat("Yamaha", "Speeding boat") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object
for x in (car1, boat1, plane1):
  print(x.make, x.model)
  x.move()

