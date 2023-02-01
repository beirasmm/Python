### Variables ###

my_string_variable = "My string variable"
print(my_string_variable)

my_int_varible = 5
print(my_int_varible)

my_int_to_str_variable = str(my_int_varible)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)


# # Concatenación de variables en un print
print(my_string_variable, my_bool_variable, str(my_int_varible))
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea
name, surname, alias, age = "Maria del Mar", "Beiras", "Marimar", 30
print(name, surname, age, alias)

name = input("What is your name? ")
age = input("How old are you? ")

print(name)
print(age)
