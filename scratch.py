fav = input("Type favourite colour: ")
print(fav)


i = int(input('what should i start at?:'))

while True:
    increment = int(input('mong:'))
    print(i)
    i += increment

    if i > 10:
        break


def divide(numerator: int, denominator: int) -> float:
    """Divides two numbers"""
    return numerator/denominator


user = int(input())
print(divide(user, 2))
