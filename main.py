import random
contra =''
caracteres = ' "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"'
count = int(input('ingrese un numero'))
for i in range(count):
    contra+=random.choice(caracteres)
print(contra)
