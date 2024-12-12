immutable_var = (1, "String", True)
print(immutable_var)

#immutable_var[0] = 2
#immutable_var[1] = 'Hello'
#immutable_var[2] = False
# выдаст ошибку, т.к кортеж не поддерживает обращение по элементам.

print(immutable_var)

mutable_list = [5, "Viktor", False]
mutable_list[0] = 61
mutable_list[1] = 'mutable_list'
mutable_list[2] = True
print(mutable_list)
