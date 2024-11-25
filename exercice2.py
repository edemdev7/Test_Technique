def are_anagrams(char1,char2):
    if(sorted(char1)== sorted(char2)):
        return True
    else:
        return False

# print(are_anagrams("dad","bad"))