def fact(n):
    mult = 1

    for i in range(1, n+1):
        mult *= i

    return mult


def pascal(rowIndex):
    coeffs = []
    row = [None] * (rowIndex + 1)
    for k in range(rowIndex+1):
        C = int(fact(rowIndex)/(fact(k)*fact(rowIndex-k)))
        coeffs.append(C)

    return coeffs
