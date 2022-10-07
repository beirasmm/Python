bolivares = input("¿Cuántos bolívares tienes?: ")
bolivares = float(bolivares)
valor_dolar = 6.07
dolares = round((bolivares / valor_dolar), 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")
