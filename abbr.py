def abbr(s):
    abbreviation = ''
    s = s.split(' ')
    for i in s:
        if i[0].isalpha():
            abbreviation += i[0].capitalize()

    return abbreviation
