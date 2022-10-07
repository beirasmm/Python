dolares = input("¿Cuántos dólares tienes?: ")
dolares = float(dolares)
valor_bolivar = 6.07
bolivares = str(round((dolares * valor_bolivar), 2))
print("Tienes Bs." + bolivares + " bolívares")
