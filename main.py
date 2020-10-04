import math
import time
def calculateNormalEquation():
    def getInput_3():
        a = input("Enter a \n")
        b = input("Enter b \n")
        c = input("Enter c \n")
        arr = [None, None, None]#instanttiating a list
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

    numbers = getInput_3()#geting input
    startTime = time.time()
    dis = calculateDiscriminant(numbers)
    result = calcEquation1(numbers, dis)#printing results
    print(f"x1 = {result[0]}\nx2 = {result[1]}")
    endtime = time.time()
    print(f"Time taken aproximately {endtime - startTime} seconds")
def calculateEquationWithoutAb()
    def getInput_2():
        a = input("Enter a \n")
        b = input("Enter b \n")
        arr = [None, None, None]#instanttiating a list
        arr[0] = int(a)#adding inputed nbumbers to the liost for later calculations
        arr[1] = int(b)
        return arr
    def calculateResult(nums):
        result = [0, None]
        temp = (nums[1] / nums[0])  * -1
        result[1] = temp
        return result
    numbers = getInput_2()
    result[] = calculateResult(numbers)
    print(f"x1 = {result[0]}\nx2 = {result[1]}")

    