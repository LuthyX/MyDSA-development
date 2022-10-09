#                   R E C U R S I O N

#Define your recursive case
#Define a base condition for our method
#Assert a condition/constraint on the input

def factorial(n):
    assert n>=0 and int(n) ==n , "The number mmust be positive integer only!"
    if n in[0,1]:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(4))

def fibonacci(n):
    assert n>=0 and int(n) ==n , "The number mmust be positive integer only!"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))

def sumdigits(n):
    assert n>=0 and int(n) ==n , "The number mmust be positive integer only!"
    if n<10: 
        return n
    else:
       return sumdigits(n//10) +  n%10

print(sumdigits(10))

def power(base, exp):
    assert exp >= 0 and int(exp) == exp, "The exponetial must be a postive integer"
    if exp == 0:
        return 1
    elif exp == 1 :
        return base
    return base * power(base, exp-1) 

print(power(4,2))

def gcd(a,b):
    assert int(a) == a and int(b) == b, "The exponetial must be a postive integer"   
    if a < 0 :
        a = -1 *a
    if b < 0 :
        b = -1 *b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
print(gcd(-25,5))

def dec2bin(n):
    assert  int(n) == n, "The exponetial must be a postive integer"
    if n in [0,1]:
        return n
    return (n%2)+10 * dec2bin(n//2)

print(dec2bin(1))