#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Car():
    """Clase tipo coche"""
    def __init__(self, make, model, year):
        """Inicializacion de los atributos"""
        self.make=make
        self.model=model
        self.year=year
    def get_descriptive_name(self):
        """ Imprime las caracteristicas en la pantalla"""
        long_name =str(self.year)+''+self.make +''+self.model
        return long_name.title()
my_new_car = Car('audi','a4',2020)
print(my_new_car.get_descriptive_name())


