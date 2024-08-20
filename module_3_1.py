calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):

    string_1 = len(string)
    string_2 = string.upper()
    string_3 = string.lower()
    count_calls()
    return string_1, string_2, string_3


def is_contains(string, list_to_search):
    count_calls()
    string = string.upper()
    return string in list_to_search








print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BANAN', 'URBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)