def print_params(a = 1, b = 'строка',c = True):
    print(a, b, c)

print_params(3)
print_params(3, 'hes')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [24, 'текст', False]
values_dict = {'a' : 32, 'b' : 'Hello', 'c' : False}

print_params(*values_list)
print_params(**values_dict)

value_list_2 = ['Good', True]
print_params(*value_list_2, 42)