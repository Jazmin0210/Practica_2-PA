#!/usr/bin/env python
# coding: utf-8

# In[17]:


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

        self.battery_size = 70

    def describe_battery(self):

        """ Imprime la el tamanio de la bateria """

        print("This car has a " + str(self.battery_size) + "-kWh battery.")



class HybridCar(Car):

    """Un intento de representar un auto electrico""" 

    def __init__(self,make,model,year):

        """ Inicializa los atributos de la clase padre """ 

        Car.__init__(self,make,model,year)

        self.battery_size = 70

        self.tank_gas= 100

    def describe_meditions(self):

        """ Imprime la el tamanio de la bateria """

        print("This car has a " + str(self.battery_size) + "-kWh battery."+'and '+str(self.tank_gas)+' liters of gasoline remaining')



class FuelCar(Car):

    """Un intento de representar un auto electrico""" 

    def __init__(self,make,model,year):

        """ Inicializa los atributos de la clase padre """ 

        Car.__init__(self,make,model,year)

        self.tank_gas = 100

    def describe_Gas(self):

        """ Imprime la cantidad de gasolina """

        print("This car has a " + str(self.tank_gas) + " liters of gasoline remaining")



my_tesla = ElectricCar('tesla','model s',2020) 

print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()

my_hybrid_car = HybridCar('JEEP','Wrangler Unlimited',2020) 

print(my_hybrid_car.get_descriptive_name())

my_hybrid_car.describe_meditions()

my_FuelCar = FuelCar('AUDI','A4',2020) 

print(my_FuelCar.get_descriptive_name())

my_FuelCar.describe_Gas()

