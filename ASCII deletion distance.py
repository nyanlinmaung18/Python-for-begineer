def ascii_deletion_distance(str1,str2):   
    finalList = deletion_samechar(str1,str2)
    deletion_distance = char_to_ASCII(finalList)
    print(deletion_distance)

#insert character of string into list    
def convert_to_list(string):
    return [char for char in string]

def deletion_samechar(str1,str2):
    list1 = convert_to_list(str1)
    list2 = convert_to_list(str2)

    for char in str1:
        for char2 in list2:
            if char == char2:
                list2.remove(char)

    for char2 in str2:
        for char in list1:
            if char == char2:
                list1.remove(char)            
    return list1 + list2

#convert characters in list to ASCII decimal value
def char_to_ASCII(list1):
    decimal = 0
    for char in list1:
        decimal += ord(char)
    return decimal

ascii_deletion_distance("at", "cat") #output is 99
ascii_deletion_distance("boat", "got")  #output is 298
ascii_deletion_distance("thought", "sloughs")  #output is 674