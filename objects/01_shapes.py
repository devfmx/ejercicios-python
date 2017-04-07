# -*- coding: utf-8 -*-

"""Ejercicio: Calcular área y perímetro de 4 figuras.

We need to calculate the area and perimeter of four figures
(Triangle, Square, Rectangle, Circle)

Requirements:
  - The figures need a name
  - One method returns the area and other the perimeter with the legend:
    “The (perimeter or area) of the (name of figure) is (calculate)”
  - I only can access attributes through getter and setter
  - I define the figure when I create the instance (object)
  - Every class is defined in its own file

Bonus:
  - Make an abstract class Shape that all inherit from
  - Make Square a subclass of Rectangle
  - Add more types of shapes (pentagon
"""

##################################################
### Sólo modificar codigo abajo de esta linea. ###
##################################################

class Triangle(object):
  def __init__(self, side1, side2, side3):
      pass

  def area(self):
      pass

###################################################
### Sólo modificar codigo arriba de esta linea. ###
###################################################

assert Triangle(3, 4, 5).area() == "The area of the Triangle is 6"
assert "Square" in vars(), "Square object should be defined."
assert "Rectangle" in vars(), "Rectangle object should be defined."
assert "Circle" in vars(), "Circle object should be defined."
assert Square(5).area() == "The area of the Square is 25"

print("Éxito! Felicidades!")
