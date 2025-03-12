def reverse(string, integer):
    string = list(string)
    if len(string) > 2 * integer:
        for index in range(0, len(string), 2*integer):
            string[index:index+integer] = string[index:index+integer][::-1]

        return ''.join(string)
    
    elif len(string) >= integer:
        string[:integer] = string[:integer][::-1]

        return ''.join(string)

