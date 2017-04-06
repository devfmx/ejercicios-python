# -*- coding: utf-8 -*-

############################################################
### Ejercicio: Agregar unos elementos nuevos a la lista. ###
### Queremos agregar "GT" y "CO" a la lista.             ###
############################################################

my_list = ["MX", "US", "CN", "CA"]

##################################################
### Sólo modificar codigo abajo de esta linea. ###
##################################################

my_list.append("GT")
my_list.append("CO")

###################################################
### Sólo modificar codigo arriba de esta linea. ###
###################################################

assert "GT" in my_list, "my_list debería tener 'GT'"
assert "CO" in my_list, "my_list debería tener 'CO'"
assert len(my_list) == 6, "mylist debería tener 6 elementos"

print("Éxito! Felicidades!")
