k1 = str(input("enter the string1:"))
k2 = str(input("enter the string2:"))


def name_test():
    if sorted(k1)==sorted(k2):
        return "The strings are anagrams."
    else:
        return "The strings are not anagrams."


print(name_test())
