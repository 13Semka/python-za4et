def fact(factorial_number):
    mult = 1

    for num in range(1, factorial_number+1):
        mult *= num

    return mult


def pascal(rowIndex):
    coeffs = []
    for row_elem in range(rowIndex+1):
        row_elem_combinations = int(fact(rowIndex)/(fact(row_elem)*fact(rowIndex-row_elem)))
        coeffs.append(row_elem_combinations)

    return coeffs
