######################################## 
#   Blair Kiel
#   Project 1, CS260
#    1/23/2014 
#   Code adapted from Dr. Brown Lab Code
#######################################

from scanner import *
import sys

def main():
   
    argvArr = sys.argv

    if len(argvArr) == 1:
        printLn = True
        inLine = sys.stdin
        char = inLine.read(1)
        num = ""
        numArr = []
        while char:
            if char not in " \t\n\r":
                num += char
            elif len(num) > 0:
                numArr.append(int(num))
                num = ""
            char = inLine.read(1)
        if len(num) > 0:
            numArr.append(int(num))

        if(numArr == []):
            print("number = 0")
            print("minimum = none" )
            print("maximum = none" )
            print("sum = 0" )
            print("product = 1" )
            print("average = none" ) 
            print("median = none" )
            print("modes = []" )
            return
        else:
            scanDocument(numArr, printLn)
    else:
        printLn = False
        if (len(argvArr) < 3):
            printLn = True
        s = Scanner(sys.argv[1])            
        numArr = []
        token = s.readtoken()           
        while (token != ""):           
            numArr.append(token)           
            token = s.readtoken()          
        s.close()                          
        if(numArr == [] and printLn == False):
            out = open(sys.argv[2], "w")
            out.write("number = 0 \n")
            out.write("minimum = none \n")
            out.write("maximum = none \n")
            out.write("sum = 0 \n")
            out.write("product = 1 \n")
            out.write("average = none \n")
            out.write("median = none \n")
            out.write("modes = []")
            out.close()
            return
        elif(numArr == [] and printLn == True):
            print("number = 0")
            print("minimum = none" )
            print("maximum = none" )
            print("sum = 0" )
            print("product = 1" )
            print("average = none" ) 
            print("median = none" )
            print("modes = []" )
            return
        else:
            scanDocument(numArr, printLn)

def scanDocument(nums, printLn):

    numSum = 0
    numProduct = 1
    for i in range(len(nums)):
        numSum = int(nums[i]) + numSum
        numProduct = numProduct * int(nums[i])

    nums.sort()
    minNum = nums[0]
    maxNum = nums[(len(nums)-1)]
    numLen = len(nums)
    numAvg = int((numSum) / (numLen))
    halfNum = int(int(numLen) / 2)

    if ((numLen/numSum) % 2 == 0):
        for i in range(numLen):
            if(i == (numLen/2)):
                median = nums[i]
    else:
        halfMinusOne = int(halfNum) -1
        median = int((int(nums[halfMinusOne]) +int(nums[int(halfNum)]))/2)

    modes = findMostCommon(nums)

    if(printLn == True):
        print("number = " + str(numLen))
        print("minimum = " + str(minNum))
        print("maximum = " + str(maxNum))
        print("sum = " + str(numSum))
        print("product = " + str(numProduct))
        print("average = " + str(numAvg))
        print("median = " + str(median))
        print("modes = " + str(modes))
    else:
        out = open(sys.argv[2], "w")
        out.write("number = " + str(numLen) + "\n")
        out.write("minimum = " + str(minNum) + "\n")
        out.write("maximum = " + str(maxNum) + "\n")
        out.write("sum = " + str(numSum) + "\n")
        out.write("product = " + str(numProduct) + "\n")
        out.write("average = " + str(numAvg) + "\n")
        out.write("median = " + str(median) + "\n")
        out.write("modes = " + str(modes) + "\n")

def findMostCommon(nums):

    #Iterate through the list of numbers, adding them to the dictionary and counting the amount of occurences
    numCount = {}
    for num in nums:
        try:
            numCount[num] += 1
        except(KeyError):
            numCount[num] = 1

    #Iterate through the keys, determining the largest number of occurence
    keys = list(numCount.keys())
    maxNum = numCount[keys[0]]
    for key in keys:
        if numCount[key] > maxNum:
            maxNum = numCount[key]

    #Iterate through the keys, adding any number that has the maximum number of occurences; They are the modes
    maxNums = []
    for key in keys:
        if numCount[key] == maxNum:
            maxNums.append(key)

    return maxNums

main()


    

