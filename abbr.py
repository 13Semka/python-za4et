def abbr(string):
    abbreviation = ''
    string = string.split(' ')
    for char in string:
        if char[0].isalpha():
            abbreviation += char[0].capitalize()

    return abbreviation

