def can_reach_end(nums):
    lengthOfArray = len(nums)
    index = 0
    count = 0
    isReach = False

    while index <= lengthOfArray:
        index = nums[index]
        count += 1
        if  index >= (lengthOfArray - 1):
            isReach = True
            break
        if count == lengthOfArray:
            isReach = False
            break
    
    print(isReach)

can_reach_end([1,2,3])   #output = True
can_reach_end([5,0,0,0]) #output = True
can_reach_end([0])       #output = True
can_reach_end([0,2,4])   #output = False
can_reach_end([1,2,0,0,1])#output = False