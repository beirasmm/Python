### Classes ###

class MyEmptyPerson:
    pass


print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class PersonFullName:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Marimar", "Beiras")
print(f"{my_person.name} {my_person.surname}")


my_person = PersonFullName("Marimar", "Beiras")
print(my_person.full_name)
my_person.walk()

my_other_person = PersonFullName("Marimar", "Beiras", "Marimar")
print(my_other_person)
my_other_person.fullname = "Brais Moure MoureDev"
print(my_other_person.fullname)
