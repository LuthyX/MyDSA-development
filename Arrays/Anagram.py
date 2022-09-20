# O(NlogN)+ O(N) = O(NlogN)
def is_anagram(str1, str2):
    #if the length differs
    if len(str1) != len(str2):
        return False
    
    #Sort the letters[this will arrange them alphabetically]
    str1 =sorted(str1)
    str2 = sorted(str2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

if __name__ == "__main__":
    s1 = ["f","l","u","s","t","e","r"]
    s2 = ["r","e","s","t","f","u","l"]
    s3= "restful"
    s4= "fluster"
    print(is_anagram(s3,s4))

    