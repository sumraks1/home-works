
def print_params(a=1, b='string', c=True):
    print(a, b, c)



values_list = [5, 'Привет', False]
values_dict = {'a': 4, 'b': 'Urban', 'c': True }
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3 ])
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)