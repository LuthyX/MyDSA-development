def factorial(n):
    assert n>=0 and int(n) ==n , "The number mmust be positive integer only!"
    if n in[0,1]:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(4))

#Define your recursive case
#Define a base condition for our method
#Assert a condition/constraint on the input

def fibonacci(n):
    assert n>=0 and int(n) ==n , "The number mmust be positive integer only!"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(-1))