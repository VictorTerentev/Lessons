calls = 0
def count_calls():
    global calls
    calls +=1
def string_info(string):
    count_calls()
    turn = len(string), string.upper(), string.lower()
    return turn


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    text1 = False
    for i in list_to_search:
        if string.lower() in i.lower():
            text1 = True
        else:
            text1 = False
    return text1


print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)
