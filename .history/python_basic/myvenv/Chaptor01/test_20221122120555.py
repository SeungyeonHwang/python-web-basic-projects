import random


def getRandomNumber():
    number = random.randint(1, 45)
    return number


list = []

while True:
    num = getRandomNumber()
    if num in list:
        continue
    else:
        list.append(num)

    if len(list) == 6:
        list.sort()
        print(list)
        break
