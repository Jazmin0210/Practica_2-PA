#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Car():

    """Un intento de representar un auto""" 

    def __init__(self, make, model, year):

        self.make = make 

        self.model = model 

        self.year = year 

        self.odometer_reading = 0

    def get_descriptive_name(self):

        long_name = str(self.year) + ',' + self.make + ',' + self.model 

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

    """Un intento de representar un auto electrico""" 

    def __init__(self,make,model,year):

        """ Inicializa los atributos de la clase padre """ 

        Car.__init__(self,make,model,year)

my_tesla = ElectricCar('tesla','model s',2020) 

print(my_tesla.get_descriptive_name())



class HybridCar(Car):

    """Un intento de representar un auto electrico""" 

    def __init__(self,make,model,year):

        """ Inicializa los atributos de la clase padre """ 

        Car.__init__(self,make,model,year)

my_Hybridcar = HybridCar('JEEP','Wrangler Unlimited',2020) 

print(my_Hybridcar.get_descriptive_name())

class FuelCar(Car):

    """Un intento de representar un auto electrico""" 

    def __init__(self,make,model,year):

        """ Inicializa los atributos de la clase padre """ 

        Car.__init__(self,make,model,year)

my_FuelCar= FuelCar('AUDI','A4',2020) 

print(my_FuelCar.get_descriptive_name())

