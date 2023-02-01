### Tuples ###

# Formas de definir una tupla

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (30, 1.65, 'Maria del Mar', 'Beiras', "Mar")
my_other_tuple = (60, 30, 35, 24, 62, 52, 17)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Beiras"))
print(my_tuple.index("Maria del Mar"))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[4:8])

my_tuple = list(my_tuple)  # Convertir una tupla a lista
print(type(my_tuple))

my_tuple[4] = "Joyeria Marimar"
my_tuple.insert(1, "Negro")
my_tuple = tuple(my_tuple)  # Convertir una lista a tupla
print(my_tuple)
print(type(my_tuple))

del my_tuple  # Eliminar totalmente la variable, no es como con las listas
# print(my_tuple) NameError ya no existe
