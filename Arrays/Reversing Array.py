# Reversing Array in-place 
def reverse(num):
    start_index = 0
    end_index = len(num)-1

    while end_index > start_index:
        num[start_index], num[end_index] = num[end_index], num[start_index]
        start_index +=1
        end_index -=1

if __name__ == "__main__":
    n = [-3,0,2]
    print(n)
    reverse(n)
    print(n)

#Palindrome Issue
# it has O (s) so basically linear running time  complexity as far as the number of letters is concerned
def palindrome_python(s):
    if s == s[::-1]:
        return True
    return False
if __name__ == "__main__":
    print (palindrome_python("lol"))