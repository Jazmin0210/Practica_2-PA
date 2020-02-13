#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Car():
    """Clase tipo coche"""
    def __init__(self, make, model, year):
        """Inicializacion de los atributos"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """ Imprime las caracteristicas en la pantalla"""
        long_name = str(self.year)+''+self.make +''+self.model
        return long_name.title()
    def read_odometer(sefl):
        """Imprime los kilometros recorrido por el auto"""
        print("This car has " + str(sefl.odometer_reading) + " miles on it")
    def update_odometer(self, mileage):
        """Modifica el valor del metodo desde la funcion"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot do that")
my_new_car = Car('audi','a4',2020)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_odometer(50)
my_new_car.read_odometer()
my_new_car.update_odometer(10)
my_new_car.read_odometer()

