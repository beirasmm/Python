### Functions ###

def my_function():
    print("Esto es una función")


my_function()


def sum_two_values(first_number, second_number):
    print(first_number + second_number)


sum_two_values(5, 7)


def sum_two_values_with_return(first_number, second_number):
    my_sum = first_number + second_number
    return my_sum


my_result = sum_two_values_with_return(16, 5)
print(my_result)


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Beiras", name="Marimar")


def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Maria del Mar", "Beiras", "Marimar")
print_name_with_default("Maria del Mar", "Beiras")


# El asterisco significa que de este tipo de dato puedo pasar tantos como quiera, numero de parametros dinamico
def print__upper_texts(*texts):
    for text in texts:
        print(text.upper())


print__upper_texts("Hola", "Python", "Marimar")
print__upper_texts("Hola")
