def isPrime(num):
    if num < 2 :    #prime number always start from 2
        print("Invalid Number: ")
    elif num == 2:
        print("{} is prime number".format(num))
    else:
        for n in range(2,num):
            if num % n == 0:
                result = False
                break
            else:
                result = True 
        if result:
            print("{} is prime number".format(num))
        else:
            print("{} is not prime number".format(num))

answer = 'y'
while (answer == 'y') or (answer == 'ye') or (answer =='yes'):
    num = int(input("Enter a Number: "))
    isPrime(num)
    answer = input("Want to check another number y/n?: ")
    answer = answer.lower()
