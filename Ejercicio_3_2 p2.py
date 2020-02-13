#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Car():
    """Clase tipo coche"""
    def __init__(self, make, model, year,color,person):
        """Inicializacion de los atributos"""
        self.make=make
        self.model=model
        self.year=year
        self.color=color
        self.person=person
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """ Imprime las caracteristicas en la pantalla"""
        long_name = str(self.year)+''+self.make +''+self.model+''+self.color+''+self.person
        return long_name.title()
    def read_odometer(sefl):
        """Imprime los kilometros recorrido por el auto"""
        print("This car has " + str(sefl.odometer_reading) + " miles on it")
my_new_car = Car('audi',' a4','2020 ',' color black', ' the 5 persons')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

