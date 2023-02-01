gryf = 0
huff = 0
slyt = 0
ravn = 0
answ_1 = int(input("Q1) Do you like Dawn or Dusk?\n 1) Dawn\n 2) Dusk\n"))
answ_2 = int(input(
    "Q2) When I’m dead, I want people to remember me as:\n 1) The Good\n 2) The Great\n 3) The Wise\n 4) The Bold\n"))
answ_3 = int(input(
    "Q3) Which kind of instrument most pleases your ear?\n 1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum\n"))
if answ_1 == 1:
    gryf += 1
    ravn += 1
elif answ_1 == 2:
    huff += 1
    slyt += 1
else:
    print("Wrong input")
if answ_2 == 1:
    huff += 1
elif answ_2 == 2:
    slyt += 1
elif answ_2 == 3:
    ravn += 1
elif answ_2 == 4:
    gryf += 1
else:
    print("Wrong input")
if answ_3 == 1:
    huff += 1
elif answ_3 == 2:
    slyt += 1
elif answ_3 == 3:
    ravn += 1
elif answ_3 == 4:
    gryf += 1
else:
    print("Wrong input")

if gryf > huff and gryf > slyt and gryf > ravn:
    print("Gryfyndor: " + str(gryf))
elif huff > gryf and huff > slyt and huff > ravn:
    print("Hufflepuff: " + str(huff))
elif slyt > gryf and slyt > huff and slyt > ravn:
    print("Slytherin: " + str(slyt))
else:
    print("Ravenclaw: " + str(ravn))
