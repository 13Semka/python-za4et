from collections import defaultdict


def count_dgt(num):
    num_string = str(num)
    appeareances = defaultdict(int)
    for i in num_string:
        appeareances[i] += 1

    return appeareances

print(count_dgt(10000))