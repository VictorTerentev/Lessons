my_dict = {'Viktor': 2002, "Misha": 2000}
print(my_dict)
print(my_dict.get('Viktor'))
print(my_dict.get('Anton'))
my_dict.update({"Alex": 2003,
               "Pasvel": 2001})

a = my_dict.pop('Misha')
print(a)
print(my_dict)

#-------------------------------

my_set = {14, 62, "String", 14, True, "False", "False"}
print(my_set)
my_set.add('Number')
my_set.add(522)
my_set.remove(14)
print(my_set)