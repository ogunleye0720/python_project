""" class Dog():
    def __init__(self, name):
        self.name = name 
        self.age = 16

    def sit(self):
        ''' The Dog Is Sitting '''
        print(self.name.title() + "is sitting")

    def update_age(self, update_age):
        ''' updates the age '''
        self.age = update_age

    def roll_over(self):
        ''' The Dog Is Rolling '''
        print(self.name.title() + "is rolling over" + f"at the age of {self.age}")

my_dog  = Dog("bobby")

my_dog.update_age(200)

print(my_dog.roll_over())
     """

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage 
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    '''Inherits From The Car class'''
    def __init__(self,make,model,year):
        '''Initializes the attributes of the Parent class'''

        super().__init__(make,model,year)


myteslan = ElectricCar("tesla", "x", 2020)
print(myteslan.get_descriptive_name())