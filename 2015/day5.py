# String checks for part 1
def has_three_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string_list = list(s)
    no_of_vowels = 0
    for char in string_list:
        if char in vowels:
            no_of_vowels += 1
    return no_of_vowels >= 3

def has_double_letters(s):
    string_list = list(s)
    for i in range(len(string_list) - 1):
        if string_list[i] == string_list[i + 1]:
            return True
    return False

def no_naughty_substrings(s):
    naughty_substrings = [['a', 'b'], ['c', 'd'], ['p', 'q'], ['x', 'y']]
    string_list = list(s)
    for i in range(len(string_list) - 1):
        if [string_list[i], string_list[i + 1]] in naughty_substrings:
            return False
    return True

# String checks for part 2
def has_double_pair(s):
    string_hash = {}
    for i in range(len(s) - 1):
        key = s[i:i + 2]
        if key not in string_hash:
            string_hash[key] = [i]
        else:
            string_hash[key].append(i)
    for k in string_hash:
        if len(string_hash[k]) > 1 and string_hash[k][-1] - string_hash[k][0] >= 2:
            return True
    return False

def has_skipping_letter(s):
    string_list = list(s)
    for i in range(len(string_list) - 2):
        if string_list[i] == string_list[i + 2]:
            return True
    return False

if __name__ == "__main__":
    no_of_nice_strings = 0
    with open("2015/day5_input.txt", "r") as f:
        string_to_check = f.readline()
        while string_to_check != "":
            # Replace string checks for part 1
            if has_double_pair(string_to_check) and has_skipping_letter(string_to_check):
                no_of_nice_strings += 1
            string_to_check = f.readline()
    print(no_of_nice_strings)