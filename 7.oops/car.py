# lets create a factory of car.

class Vehcle:
    color = "blue"
    logo = '@'


# to create an object we need a "object-name" & a "constructor"
car = Vehcle() # this is the object (car) of the class (vehcle)
bike = Vehcle()  # Vehcle() <---- this is how constructor is created 
truck = Vehcle()
dumper = Vehcle()

print(car.color)
print("we only make blue Vehcles") # this is the way to access the object from a class

print(bike.color)
print(bike)