def bracket_match(bracket_string):
    
    if bracket_string[0] != ")":
        openingBracket = 0
        closingBracket = 0
        for x in bracket_string:
            if  x == "(":
                openingBracket += 1
            elif x == ")":
                openingBracket -= 1
        if openingBracket == closingBracket:
            value = 0
        elif openingBracket != closingBracket:
            value = 1
    elif (len(bracket_string) % 2) != 0:
        value = 1
    else:
        value = 2

    print(value)

bracket_match("(()())") # output is 0
bracket_match("((())")  # output is 1
bracket_match("())")    # output is 1
bracket_match(")(")     # output is 2
