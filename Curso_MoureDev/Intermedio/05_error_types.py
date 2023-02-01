### Error Types ###

# ModuleNotFoundError
# import maths
import math

# ImportError
# from math import PI
from math import pi


# Syntax error
# print "¡Hola Comunidad!" #Descomentar para error
print("¡Hola Comunidad!")

# NameError
language = "Spanish"  # Comentar para error
print(language)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
# print(my_list[5]) #Descomentar para error
print(my_list[0])
print(my_list[4])
print(my_list[-1])

# AttributeError
# print(math.PI) #Descomentar para error
print(math.pi)

# KeyError
my_dict = {"Nombre": "Maria del Mar",
           "Apellido": "Beiras", "Edad": 30,  1: "Pyhton"}

# print(my_dict["Nome"])  # Descomentar para error
print(my_dict["Nombre"])
print(my_dict[1])

# TypeError
# print(my_list["Nombre"]) #Descomentar para error
print(my_list[2])

# ValueError
my_int = int("10")
# my_int = int("10 Años") #Descomentar para error
print(type(my_int))

# ZeroDivisionError
print(4/2)
# print(4/0) #Descomentar para error
