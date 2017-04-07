# -*- coding: utf-8 -*-

"""Ejercicio: Horse Race

Rules:
  - the first horse which runs 20 steps is the winner
  - Only two horses
  - Each turn, each horse advances a random number of steps between 0 and 5
  - The maximum you can advance in a turn are 5 steps
  - If the 2 arrive at 20 steps in the same turn the result is a tie
  - Each turn you must show the number of the turn and the number of steps
    that each horse advances
  - You must do all with classes
"""

##################################################
### Sólo modificar codigo abajo de esta linea. ###
##################################################

class Horse(object):

  def __init__(self):
    pass


def race(h1, h2):
  pass

###################################################
### Sólo modificar codigo arriba de esta linea. ###
###################################################

horse1 = Horse()
horse2 = Horse()

assert race(horse1, horse2)

print("Éxito! Felicidades!")
