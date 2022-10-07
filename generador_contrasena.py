import random
import string


def generate_password(num_of_chars):
    mayus = list(string.ascii_uppercase)
    minus = list(string.ascii_lowercase)
    numbs = list(string.digits)
    symbols = list(string.punctuation)

    chars = mayus + minus + numbs + symbols
    password = []

    for i in range(num_of_chars):
        random_char = random.choice(chars)
        password.append(random_char)

    password = "".join(password)
    return password


def run():
    num_of_chars = int(
        input("Ingrese el numero de caracteres que debe tener su contraseña: \n"))
    password = generate_password(num_of_chars)
    print(" Tu nueva contraseña es: " + password)


if __name__ == "__main__":
    run()
