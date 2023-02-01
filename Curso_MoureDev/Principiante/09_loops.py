### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print("Mi condición es menor que 20")

print("La ejecución continua")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (30, 1.65, 'Maria del Mar', 'Beiras', "Mar")

for element in my_tuple:
    print(element)

my_set = {"Maria del Mar", "Beiras", 30}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Maria del Mar",
           "Apellido": "Beiras", "Edad": 30,  1: "Pyhton"}

for keys, value in my_dict.items():
    print(f"{keys}: {value}")
    if keys == "Edad":
        break  # Detenemos la ejecución del for antes de que finalice el recorrido por el diccionario
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")

print("La ejecución continua")

for keys, value in my_dict.items():
    print(f"{keys}: {value}")
    if keys == "Edad":
        continue  # Indicamos para que continue la ejecucion, pero volvemos al for
else:
    print("El bucle for para diccionario ha finalizado")
