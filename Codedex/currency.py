yuan = int(input("What do you have left in yuan? "))
yen = int(input("What do you have left in yen? "))
won = int(input("What do you have left in won? "))
usd_yuan = 0.14
usd_yen = 0.0069
usd_won = 0.00070
total = yuan*usd_yuan + yen*usd_yen + yuan*usd_yuan
print(total)
