def bracket_match(bracket_string):
    isStartClosing = False
    openingBracket = 0
    closingBracket = 0
    
    if bracket_string[0] == ")":
        isStartClosing = True

    for x in bracket_string:
        if  x == "(":
            openingBracket += 1
        elif x == ")":
            openingBracket -= 1
    if openingBracket == closingBracket:
        if isStartClosing:
            value = 2
        else:
            value = 0
    elif openingBracket != closingBracket:
        value = 1

    print(value)

bracket_match("(()())") # output is 0
bracket_match("((())")  # output is 1
bracket_match("())")    # output is 1
bracket_match(")(")     # output is 2
bracket_match("))")     # output is 1