first = input()
second = input()
third = input()

if first == second and second == third:
    print(3)
elif first == second or first == third:
    print(2)
elif second == first or second == third:
    print(2)
else:
    print(0)

