#  Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
#  - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
#  - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
#  - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
import random


def compare_comunes(arr1, arr2, boo):

    # def create_list(n):
    #     lst = []
    #     for i in range(0, n):
    #         ele = int(input("Inserta el elemento " + str(i)+": "))
    #         lst.append(ele)  # adding the element
    #     return lst


def run():
    # nombre = input(" Escribe tu nombre: ")
    # for letra in nombre:
    #     print(letra)

    # number of elements as input
    n = int(input("Inserta el numero de elementos del arreglo 1: "))
    arr1 = random.sample(range(10), n)
    print(arr1)
    n2 = int(input("Inserta el numero de elementos del arreglo 2: "))
    arr2 = random.sample(range(10), n2)
    print(arr2)
    consult = "Seleccione el arreglo que desea:\n 1-Numeros Comunes\n 2-Numeros no comunes\n"
    option = int(input(consult))
    if option == 1:
        result = compare_comunes(arr1, arr2, True)
        print(result)
    elif option == 2:
        result = compare_comunes(arr1, arr2, False)
        print(result)
    else:
        print("Ingresa una opción correcta, por favor")


if __name__ == "__main__":
    run()
