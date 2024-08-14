first = int(input('Введите число '))
second = int(input('Введите число '))
third = int(input('Введите число '))
if first != second and second != third and first != third:
    print(int("0"))
elif first == second or second == third or first == third:
    print(int("2"))
elif first == second and second == third :
    print(int("3"))
