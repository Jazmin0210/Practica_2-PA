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

    def charge(self): 

        print("The car is charging ....")



class ElectricCar(Car):

    """Un intento de representar un auto electrico""" 

    def __init__(self,make,model,year):

        """ Inicializa los atributos de la clase padre """

        Car.__init__(self,make,model,year)

        self.battery_size = 70

    def describe_battery(self):

        """ Imprime la el tamanio de la bateria """

        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def charge(self): 

        print("The battery is almost empty, the car is charging")





my_tesla = ElectricCar('tesla','model s',2020) 

print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()

my_tesla.charge()

