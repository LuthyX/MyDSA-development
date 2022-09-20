#Our task is to design an efficient algorithm to reverse a given integer. For example if the input of the algorithm is 1234 then the output should be 4321.

def integer_reverse(n):
    remainder = 0
    reversed_int = 0

    while n>0:
        remainder = n%10
        reversed_int = reversed_int *10 + remainder
        n = n // 10
    return reversed_int

if __name__ == "__main__":
    print(integer_reverse(126576876))