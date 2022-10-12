def run():
    mass = int(input("Indique su masa corporal: "))
    height = float(input("Indique su masa estatura: "))
    bmi = mass/(height**2)
    print("Su indice de masa corporal es: " + str(bmi))


if __name__ == "__main__":
    run()
