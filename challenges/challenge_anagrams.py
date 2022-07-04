def is_anagram(first_string, second_string):
    string_one = list(first_string)
    string_two = list(second_string)

    if first_string == '' or second_string == '':
        return False

    for word in string_one:
        if word in string_two:
            string_two.remove(word)

    if len(string_two) == 0:
        return True
    return False
