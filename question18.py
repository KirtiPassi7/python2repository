#Write a python program that checks if two strings are anagrams of each other.
def anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if len(str1) != len(str2):
        return False
    
    return sorted(str1) == sorted(str2)
string1="hii"
string2="bye"

if anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')

