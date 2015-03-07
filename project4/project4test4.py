######################################## 
#   Blair Kiel
#   Project 4, CS260
#   1/23/2014 
#######################################
from scanner import *
import queue
import sys

def main():

    inputFile = sys.argv[1]
    FiFoOutput = sys.argv[2]
    LiLoOutput = sys.argv[3]
    WtAvgOutput = sys.argv[4]

    inputArray = ReadInputToArray(inputFile)
    print(inputArray)
    fifoCalculation(inputFile, FiFoOutput)
    liloCalculation(inputFile, LiLoOutput)

def fifoCalculation(inputFile, outFile):

    q = queue.Queue()
    s = Scanner(inputFile)
    line = s.readline()
    gTotal = 0
    qSize = 0
    while(line != ""):
        arr = line.split()
        print("qSize = " + str(qSize))
        if(arr[0] == "Buy"):
            q.put([arr[1], arr[2]])
            qSize = qSize + 1
        elif(arr[0] == "Sell"):
            sShare = int(arr[1])
            compShare = sShare
            sPrice = int(float((arr[2])))
            sSalePrice = sShare * sPrice
            sRemainder = sShare
            sSum = 0;
            sSumShares = 0;
            #while(compShare > 0 ):
            while((q.empty() == False) and (compShare > 0)):
                b = q.get()
                bShare = int(b[0])
                bPrice = int(float(b[1]))
                print("bShare is " + str(bShare))
                print("bPrice is " + str(bPrice))
                if((bShare - compShare) > 0): #if selling shares are less than the available buying shares
                    bRem = bShare - compShare
                    bBoughtPrice = compShare * bPrice
                    a = q
                    aSize = qSize
                    q.put([str(bRem),b[1]])
                    while(aSize >= 2):
                        temp = a.get()
                        aSize = aSize - 1
                        print("temp is " + str(temp))
                        q.put(temp)
                else:
                    bRem = bShare - sSumShares
                    bBoughtPrice = bRem * bPrice
                sSum += bBoughtPrice
                sSumShares = sRemainder - bShare
                total = sSalePrice - sSum
                print("total is " + str(sSalePrice) + " - " + str(sSum) + " = " + str(total))
                compShare = compShare - bShare
            
            bShare = bShare - bRem
            gTotal += total
            if(total > 0):
                print("Gain = " + str(total))
            else:
                print("Loss = " + str(total))
            print()
            qSize -= 1
        line = s.readline()
    print("Total = " + str(gTotal))
    s.close()

def liloCalculation(inputFile, outFile):

    print()
    print("LiLoCalculation")
    stack = []
    s = Scanner(inputFile)
    line = s.readline()
    gTotal = 0
    sSize = 0
    while(line != ""):
        arr = line.split()
        print("qSize = " + str(sSize))
        if(arr[0] == "Buy"):
            stack.append([arr[1], arr[2]])
            sSize = sSize + 1
        elif(arr[0] == "Sell"):
            sShare = int(arr[1])
            compShare = sShare
            sPrice = int(float((arr[2])))
            sSalePrice = sShare * sPrice
            sRemainder = sShare
            sSum = 0;
            sSumShares = 0;
            #while(compShare > 0 ):
            while((stack) and (compShare > 0)):
                b = stack.pop()
                bShare = int(b[0])
                bPrice = int(float(b[1]))
                print("bShare is " + str(bShare))
                print("bPrice is " + str(bPrice))
                if((bShare - compShare) > 0): #if selling shares are less than the available buying shares
                    bRem = bShare - compShare
                    bBoughtPrice = compShare * bPrice
                    a = stack
                    aSize = sSize
                    stack.append([str(bRem),b[1]])
                    while(aSize >= 2):
                        temp = a.pop()
                        aSize = aSize - 1
                        print("temp is " + str(temp))
                        stack.append(temp)
                else:
                    bRem = bShare - sSumShares
                    bBoughtPrice = bRem * bPrice
                sSum += bBoughtPrice
                sSumShares = sRemainder - bShare
                total = sSalePrice - sSum
                print("total is " + str(sSalePrice) + " - " + str(sSum) + " = " + str(total))
                compShare = compShare - bShare
            bShare = bShare - bRem
            gTotal += total
            if(total > 0):
                print("Gain = " + str(total))
            else:
                print("Loss = " + str(total))
            print()
            sSize -= 1
        line = s.readline()
    print("Total = " + str(gTotal))
    s.close()
    
def wtAvgCalculation(inFile, outFile):
    
    q = queue.Queue()
    s = Scanner(inputFile)
    line = s.readline()
    gTotal = 0
    qSize = 0
    while(line != ""):
        arr = line.split()
        print("qSize = " + str(qSize))
        if(arr[0] == "Buy"):
            q.put([arr[1], arr[2]])
            qSize = qSize + 1
        elif(arr[0] == "Sell"):
            sShare = int(arr[1])
            compShare = sShare
            sPrice = int(float((arr[2])))
            sSalePrice = sShare * sPrice
            sRemainder = sShare
            sSum = 0;
            sSumShares = 0;
            #while(compShare > 0 ):
            while((q.empty() == False) and (compShare > 0)):
                a = q
                aSize = qSize
                totalShares = 0
                totalPrice = 0 
                while((a.empty() == False)):
                    temp = a.get()
                    bShare = int(temp[0])
                    bPrice = int(float(b[1]))
                    totalShares = bShare + totalShares
                    totalPrice = bPrice + totalPrice
                    mean = totalPrice / totalShares
                b = q.get()
                bShare = int(b[0])
                bPrice = int(float(b[1]))
                print("bShare is " + str(bShare))
                print("bPrice is " + str(bPrice))
                if((bShare - compShare) > 0): #if selling shares are less than the available buying shares
                    bRem = bShare - compShare
                    bBoughtPrice = compShare * bPrice
                    a = q
                    aSize = qSize
                    q.put([str(bRem),b[1]])
                    while(aSize >= 2):
                        temp = a.get()
                        aSize = aSize - 1
                        print("temp is " + str(temp))
                        q.put(temp)
                else:
                    bRem = bShare - sSumShares
                    bBoughtPrice = bRem * bPrice
                sSum += bBoughtPrice
                sSumShares = sRemainder - bShare
                total = sSalePrice - sSum
                print("total is " + str(sSalePrice) + " - " + str(sSum) + " = " + str(total))
                compShare = compShare - bShare
            
            bShare = bShare - bRem
            gTotal += total
            if(total > 0):
                print("Gain = " + str(total))
            else:
                print("Loss = " + str(total))
            print()
            qSize -= 1
        line = s.readline()
    print("Total = " + str(gTotal))
    s.close()

def ReadInputToArray(inputFile):

    s = Scanner(inputFile)
    items = []
    line = s.readline()
    arr = line.split()
    while(line != ""):
        items.append(arr)
        line = s.readline()
        arr = line.split()
    s.close()
    return items

#class Stack(object):
#    #this is the class that will construct the circular doubly linked list
#
#    def __init__(self, shares, price, Next):
#        self.shares = shares
#        self.price = price
#        self.Next = Next
#
#    def push(self, item):
#        self.items.append(item)
#
#    def pop(self):
#        return self.items.pop()
#
#    def peek(self):
#        return self.items[len(self.items)-1]
#
#    def size(self):
#        return len(self.items)
                                                                        
main()
