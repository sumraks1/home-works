my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    number_in_list = int(input('Введите число из списка: '))
    if number_in_list == my_list[i]:
        print(my_list[i])
        i += 1
        if number_in_list <= 0:
            break




