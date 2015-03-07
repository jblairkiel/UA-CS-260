######################################## 
#   Blair Kiel
#   Project 4, CS260
#   1/23/2014 
#######################################
from scanner import *
import sys

def main():

    inputFile = sys.argv[1]
    FiFoOutput = sys.argv[2]
    LiLoOutput = sys.argv[3]
    WtAvgOutput = sys.argv[4]

    inputArray = ReadInputToArray(inputFile)
    #print(inputArray)
    #newCal(inputFile, FiFoOutput)

    s = Scanner(inputFile)
    line = s.readline()
    while(line != ""):
        arr = line.split()
        if(arr[0] == "Buy"):
        
        elif(arr[0] == "Sell"):

        line = s.readLine()
    s.close()

def newCal(inputFile, outFile):
    s = Scanner(inputFile)
    line = s.readline()
    gTotal = 0
    q = None
    while(line != ""):
        arr = line.split()
        if(arr[0] == "Buy"):
            if(q == None):  #Starting a new queue
                q = queue(arr[1], arr[2])
                q.prev = q
                q.Next = q
            else:
                f = queue(arr[1], arr[2])
                q = q.put(f)
        elif(arr[0] == "Sell"):
            sShare = int(arr[1])
            sLeft = sShare
            sRemainder = sShare
            sPrice = int(float(arr[2]))
            sSalePrice = sShare * sPrice
            sSum = 0
            while(sLeft > 0): #While there are still shares to be sold
                b = q.get()
                bShare = int(b[0])
                bPrice = int(float(b[1]))
                if((bShare - sLeft) > 0): #There are shares that need to be added to node

                elif((b
                bBoughtPrice = sLeft * bPrice
                print("bBought Price is " + str(bBoughtPrice) + " = " + str(sLeft) + " * " + str(bPrice))
                sSum += bBoughtPrice
                total = sSalePrice - sSum
                sLeft= sLeft - bShare
            if(total > 0):
                print("Gain = " + str(total))
            else:
                print("Loss = " + str(total))
            print()
        line = s.readline()
    print("Total = " + str(gTotal))
    s.close()

class queue(object):
    #queue class
    def __init__(self, shares, price):
        self.front = self
        self.rear = self
        self.Next = self
        self.shares = shares
        self.price = price
        self.size = 1

    def __repr__(self):
    return repr(str(self.shares) + " , " + str(self.price))

    def peek(self):
        return [self.shares, self.price]

    def get(self):
        ret = self.front
        retSize = self.size
        self.front = self.Next
        self.size -= 1
        return [ret.shares, ret.price]

    def put(self, item):
        if(self.empty()):
            self.Next = item
            self.rear = item
        else:
            self.rear.Next = item
            self.rear = item
        self.size += 1

    def replaceFront(self, item):
        if(self.empty()):   
            item.Next = item
            self.front = item
        else:
            temp = self.front.Next
            self.front = item
        self.front = newNode

    def empty(self):
        if(self.Next = self):
            return True
        else:
            return False
                                                                        
main()
