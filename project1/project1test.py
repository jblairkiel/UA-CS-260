######################################## 
#   Blair Kiel
#   Project 1, CS260
#   Due Date
#   Code adapted from Dr. Brown Lab Code
#######################################

from scanner import *
import sys

def main():

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

    scanDocument(numArr)

def scanDocument(nums):

    numSum = 0
    numProduct = 1
    for i in range(len(nums)):
        numSum = int(nums[i]) + numSum
        numProduct = numProduct * int(nums[i])

    nums.sort()
    minNum = nums[0]
    maxNum = nums[(len(nums)-1)]
    numLen = len(nums)
    numAvg = (numSum) / (numLen)
    halfNum = int(numLen) / 2

    if ((numLen/numSum) % 2 == 0):
        for i in range(numLen):
            if(i == (numLen/2)):
                median = nums[i]
    else:
        halfMinusOne = int(halfNum) -1
        median = (int(nums[halfMinusOne]) +int(nums[int(halfNum)]))/2

    modes = findMostCommon(nums)

    print("number = " + str(numLen))
    print("minimum = " + str(minNum))
    print("maximum = " + str(maxNum))
    print("sum = " + str(numSum))
    print("product = " + str(numProduct))
    print("average = " + str(numAvg))
    print("median = " + str(median))
    print("modes = " + str(modes))

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


    

