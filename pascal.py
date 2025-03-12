def fact(factorial_number):
    mult = 1

    for num in range(1, factorial_number+1):
        mult *= num

    return mult


def pascal(rowIndex):
    coeffs = []
    for k in range(rowIndex+1):
        C = int(fact(rowIndex)/(fact(k)*fact(rowIndex-k)))
        coeffs.append(C)

    return coeffs
