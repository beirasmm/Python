### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Maria del Mar", "Beiras", 30}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Marimar")

print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("Marimar")  # Un set no admite repetidos

print(my_other_set)

print("Marimar" in my_other_set)
print("Marimare" in my_other_set)

my_other_set.remove("Marimar")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set  # Borrar un objeto completamente
# print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Maria del Mar", "Beiras", 30}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"C#", "Angular", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(
    my_set).union({"JavaScript", "TypeScript"}))

print(my_new_set.difference(my_set))

# Revisar aun otras operaciones
