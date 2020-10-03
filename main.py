import math
import time
def getInput():
    a = input("Enter a \n")
    b = input("Enter b \n")
    c = input("Enter c \n")
    arr = [None, None, None]#instatntiating a list
    arr[0] = int(a)#adding inputed nbumbers to the liost for later calculations
    arr[1] = int(b)
    arr[2] = int(c)
    return arr
def calculateDiscriminant(nums):
    D = (nums[1] * nums[1]) - 4 * nums[0] * nums[2]#calculating discriminant from entered nums
    #checking if dis is lower than zero
    if D < 0:
        return "cannot be calced"
    elif D >= 0:
        return int(D)
def calcEquation1(nums, D):
    upper1 = -1 * nums[1] + math.sqrt(D)#calculating uper for + - and then lower 
    upper2 = -1 * nums[1] - math.sqrt(D)
    lower = 2 * nums[0]
    results = [None, None]#instantiating list
    results[0] = upper1 / lower#geting x1 and x21
    results[1] = upper2 / lower
    return results

numbers = getInput()#geting input
startTime = time.time()
dis = calculateDiscriminant(numbers)
print(calcEquation1(numbers, dis))#results
endtime = time.time()
print(f"Time taken {endtime - startTime} seconds")