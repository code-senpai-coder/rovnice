from math import sqrt as odmocnina
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
           print("cannot be calced")
        elif D >= 0:
            upper1 = -1 * nums[1] + odmocnina(D)#calculating uper for + - and then lower 
            upper2 = -1 * nums[1] - odmocnina(D)
            lower = 2 * nums[0]
            results = [None, None]#instantiating list
            results[0] = upper1 / lower#geting x1 and x21
            results[1] = upper2 / lower
            print(f"x1 = {results[0]}\nx2 = {results[1]}")
    numbers = getInput_3()#geting input
    calculateDiscriminant(numbers)

def calculateEquationWithoutAb():
    def getInput_2():
        a = input("Enter a \n")
        b = input("Enter b \n")
        arr = [None, None]#instanttiating a list
        arr[0] = int(a)#adding inputed nbumbers to the liost for later calculations
        arr[1] = int(b)
        return arr
    def calculateResult(nums):
        result = [0, None]
        temp = (nums[1] / nums[0])  * -1
        result[1] = temp
        return result
    numbers = getInput_2()
    result = [None, None]
    result = calculateResult(numbers)
    print(f"x1 = {result[0]}\nx2 = {result[1]}")
def caculatePureQuadraticEquation():
    def getInput_3():
        a = input("Enter a: \n")
        c = input("Enter c: \n")
        arr = [None, None]
        arr[0] = int(a)
        arr[1] = int(c)
        return arr
    def calculateSqrtAndResult(nums):
        temp = -1*(nums[1]/nums[0])
        if temp < 0 :
            print("cannot be calced")
        else:
            result = [None, None]
            result[0] = odmocnina(temp)
            result[1] = -1 * odmocnina(temp)
            print(f"x1 = {result[0]}\nx2 = {result[1]}")
    numbers = getInput_3()
    calculateSqrtAndResult(numbers)

def main():
    in_ = input("Press 1 for full quadratic equations\nPress 2 for equation without ab \nPress 3 for purely quadratic equation\n")
    #cheking inputs
    if in_ == "1":
        calculateNormalEquation()
    elif in_ == "2":
        calculateEquationWithoutAb()
    elif in_ == "3":
        caculatePureQuadraticEquation()
    #invalid input
    else:
        print("Invalid input, try again")
        main()
    main()
#aplication start
main()