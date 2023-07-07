#polymorphism example
class Vehicle:
    def _init_(self,make,model,horsepower):
        self.make = make
        self.model=model
        self.horsepower=horsepower
        def move(self):
            print("Quater Mile time!")
class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("Sail!")
class Plane(Vehicle):
    def move(self):
        print("Fly!")
car1 = Car("Nissan","GTR",565)
boat1 = Boat("Yamaha","Speedboat",352)
plane1 = Plane("Boeing", "747", 59934)
for x in (car1,boat1,plane1):
    print (x.make)
    print (x.model)
    x.move()
    
