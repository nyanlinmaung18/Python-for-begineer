def stock_runs(prices):
    countRose = 0
    countFell  = 0
    previousPrice = -1
    isPassRose = False
    isPassFell = False

    for index in prices:
        
        if (index > previousPrice):
            #if counting was pass count fell price, reset counting raise price from 1
            if isPassFell:
                countRose = 1
                isPassFell = False
            countRose += 1
            isPassRose = True

        elif(index < previousPrice):
            #if counting was pass count raise price, reset counting fell price from 1
            if isPassRose:
                countFell = 1
                isPassRose = False
            countFell += 1

        #if equal index with previousPrice, reset the counting
        elif(index == previousPrice):
            countRose = 1
            countFell = 1

        previousPrice = index 
    
    #take the longest length
    if countRose >= countFell:
        return countRose
    elif countRose < countFell:
        return countFell

print(stock_runs([1,2,3]))       #output is 3
print(stock_runs([2,3,4,3,2,1])) #output is 4
print(stock_runs([3,2,2,1]))     #output is 2


