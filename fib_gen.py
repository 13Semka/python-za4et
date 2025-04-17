def fibonacci(num_amount):
    num1 = 0
    num2 = 1
    for _ in range(num_amount):
        yield num1
        num1, num2 = num2, num1+num2
            
