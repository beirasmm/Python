### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Maria del Mar",
                 "Apellido": "Beiras", "Edad": 30,  1: "Pyhton"}
my_dict = {
    "Nombre": "Maria del Mar",
    "Apellido": "Beiras",
    "Edad": 30,
    "Lenguajes": {"Pyhton", "C#", "JavaScript"},
    1: 1.65
}

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Marimar"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Guillermo José Schael"
print(my_dict)

del my_dict["Calle"]  # Removemos un elemento del diccionario
print(my_dict)
my_dict.pop(1)  # Removemos el item de una clave especifica
print(my_dict)
# my_dict.popitem()  Elimina el ultimo item

print("Apellido" in my_dict)  # Busca si una clave esta en el set
print("Marimar" in my_dict)

print(my_dict.keys())  # Devuelve las llaves
print(my_dict.values())  # Devuelve los valores dentro del diccionario
print(my_dict.items())  # Devuelve los items

my_list = ["Nomre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)  # Crea un nuevo diccionario sin valores a partir de una lista
# Crea un nuevo diccionario a partir de las llaves de otro diccionario
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
# Crea un nuevo diccionario a partir de las llaves de otro diccionario y le seteamos los valores que estan en el segundo parametro para todas las llaves
my_new_dict = dict.fromkeys(my_dict, ["Marimar", "Beiras"])
print(my_new_dict)

my_values = my_new_dict.values()
print(my_values)
