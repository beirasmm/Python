import random

# RNGesus will give us a random number between 0 and 1
num = random.randint(0, 1)

if num > 0.5:
    print("Heads")
else:
    print("Tails")
