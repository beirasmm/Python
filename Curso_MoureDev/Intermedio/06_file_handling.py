### File Handling ###
import xml
import csv
import json
import os

# .txt file
txt_file = open("Curso MoureDev/Intermedio/my_file.txt", "r+")
# print(txt_file.read())
# print(txt_file.read(10))
# print(txt_file.readline())
for line in txt_file.readlines():
    print(line)


# txt_file.write("Soy Ingeniera Informatica de la UCAB")#Descomentar para escribir esta linea

new_txt_file = open("Curso MoureDev/Intermedio/my_new_file.txt", "w+")
new_txt_file.write(
    "Mi nombre es Maria del Mar\nMi Apellido es Beiras\n30 años\nMi lenguaje preferido es Python")
new_txt_file.close()
os.remove("Curso MoureDev/Intermedio/my_new_file.txt")

# .json file

json_file = open("Curso MoureDev/Intermedio/my_file.json",
                 "w+")  # abrir fichero
json_test = {"name": "Maria del Mar",
             "surname": "Beiras",
             "age": 30,
             "languages": ["Pyhton", "JavaScript", "Swift"],
             "website": "https://moure.dev"}

json.dump(json_test, json_file, indent=2)
json_file.close()
with open("Curso MoureDev/Intermedio/my_file.json", "r") as json_file:
    json_data = json.load(json_file)

print(json_data)


with open("Curso MoureDev/Intermedio/my_file.json", "r") as my_other_json_file:
    for line in my_other_json_file.readlines():
        print(line)

print(type(json_data))


# .csv file
csv_file = open("Curso MoureDev/Intermedio/my_file.csv",
                "w+", newline='')

json_test = {"name": "Maria del Mar",
             "surname": "Beiras",
             "age": 30,
             "languages": ["Pyhton", "JavaScript", "Swift"],
             "website": "https://moure.dev"}

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Maria del Mar", "Beiras", 30,
                    "Pyhton", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2,
                    "COBOL", ""])
csv_file.close()

# Imprimir como strings
with open("Curso MoureDev/Intermedio/my_file.csv", "r") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# Imprimir cada linea de valores
with open("Curso MoureDev/Intermedio/my_file.csv", "r") as my_other_csv_file:
    csv_data = csv.reader(my_other_csv_file)
    for row in csv_data:
        print(row)


csv_dict = []  # Imprimir como un diccionario con clave - valor
with open("Curso MoureDev/Intermedio/my_file.csv", "r") as my_other_csv_file:
    csv_data = csv.DictReader(my_other_csv_file)
    for row in csv_data:
        csv_dict.append(row)
    print(csv_dict)

# .xlsx file
# import xlrd #Debe instalarse el modulo para trabajar con xlsx

# .xml file
