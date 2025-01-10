import random
chara="+-/*!&=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long=int(input("que tan larga quieres que sea tu contraseña?"))
passw = ""

for _ in range(long):
    passw += random.choice(chara)
    print("la contraseña es", passw)
    