### Exception Handling ###

numbr_one = 5
number_two = "1"

# try except
try:
    print(numbr_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

# try except else

try:
    print(numbr_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución continua correctamente")

# try except else finally

try:
    print(numbr_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
  # Se ejecuta si no se produce una excepción
    print("La ejecución continua correctamente")
finally:
  # Se ejecuta siempre
    print("La ejecución continúa")

# excepciones por tipo
try:
    print(numbr_one + number_two)
    print("No se ha producido un error")
except ValueError:
  # Se ejecuta si se produce una excepcion
    print("Se ha producido un ValueError")
except TypeError:
  # Se ejecuta si se produce una excepcion
    print("Se ha producido un TypeError")


# Carptura de la información de la excepción
try:
    print(numbr_one + number_two)
    print("No se ha producido un error")
except ValueError as error:
  # Se ejecuta si se produce una excepcion
    print(error)
except Exception as error:
    print(error)
