### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [30, 30, 35, 24, 62, 52, 17]

print(my_list)
print(len(my_list))

my_other_list = [30, 1.65, 'Maria del Mar', 'Beiras']

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count(30))  # Verificar cuantas veces se repite un elemento
# print(my_other_list[-5]) Index error
# print(my_other_list[4]) Index error

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(surname)

print(my_list + my_other_list)
# print(my_list - my_other_list) Error

my_other_list.append("Joyeria Marimar 4492, C.A")
print(my_other_list)

my_other_list.insert(1, "Negro")
print(my_other_list)

my_other_list.remove("Negro")
print(my_other_list)

# Crea una nueva lista que va del indice 2 al indice 4, ya que el 5 a pesar de que se coloca no se incluye
thing_of_my_list = my_list[2:5]
print(f"Esta es mi list of things {thing_of_my_list}")

my_list.remove(30)
print(my_list)

# Reverse se modifica la lista original
my_list.reverse()
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)
