from collections import defaultdict


def count_dgt(num):
    num_string = str(num)
    appeareances = defaultdict(int)
    for num_char in num_string:
        appeareances[num_char] += 1

    return appeareances

print(count_dgt(10000))