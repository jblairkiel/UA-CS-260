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
    print(inputArray)
    newCal(inputFile, FiFoOutput)
    #fifoCalculation(inputFile, FiFoOutput)
    #liloCalculation(inputFile, LiLoOutput)

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


            

def fifoCalculation(inputFile, outFile):

    s = Scanner(inputFile)
    line = s.readline()
    gTotal = 0
    qSize = 0
    q = None
    while(line != ""):
        arr = line.split()
        if(arr[0] == "Buy"):
            print('     buying')
            print()
            if(q == None):
                print("q is none")
                q = queue(arr[1],arr[2])
                print("q is: " + str(q))
                q.prev = q
                q.Next = q
            else:
                f = queue(arr[1],arr[2])
                q = q.put(f)
                print("q is: " + str(q))
            print("qSize = " + str(q.size))
        elif(arr[0] == "Sell"):
            sShare = int(arr[1])
            compShare = sShare
            sPrice = int(float((arr[2])))
            print('     selling ' + str(sShare) + " at " + str(sPrice))
            print()
            sSalePrice = sShare * sPrice
            sRemainder = sShare
            sSum = 0;
            sSumShares = 0;
            while(compShare > 0 ):
            #while((not q.empty()) and (compShare > 0)):
                #print("problem here q is " + str(q))
                b = q.get()
                print("q is " + str(q))
                print("q.get() is " + str(b))
                bShare = int(b[0])
                bPrice = int(float(b[1]))
                print("bShare is " + str(bShare))
                print("bPrice is " + str(bPrice))
                if((bShare - compShare) > 0): #if selling shares are less than the available buying shares
                    bRem = bShare - compShare
                    print("bShare - compShare = " + str(bRem))
                    bBoughtPrice = compShare * bPrice
                    print("bBoughtPrice = " + str(bBoughtPrice) + " = " + str(compShare) + " * " + str(bPrice))
                    print("   ! bRem is " + str(bRem))
                    f = queue(str(bRem), b[1])
                    temp = q.get()
                    while(q.size >= 0):
                        f.put(temp)
                        q.get()
                    q = f
                    print("q is now " + str(q))
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
    
    s = Scanner(inputFile)
    line = s.readline()
    gTotal = 0
    qSize = 0
    q = None
    while(line != ""):
        arr = line.split()
        print("qSize = " + str(qSize))
        if(arr[0] == "Buy"):
            if(q == None):   
                q = queue(arr[1], arr[2])
            else:
                f = queue(arr[1], arr[2])
                q.put(f)
            qSize += 1
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
                aSize = q.size
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
                    f = queue(str(bRem), b[1])
                    q.put(f)
                    while(aSize >= 2):
                        temp = a.get()
                        f = queue(temp[0],temp[1])
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
            total = "{:.2f}".format(total)
            if(total > 0):
                print("Gain = " + str(total))
            else:
                print("Loss = " + str(total))
            print()
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


class queue(object):
    #queue class
    def __init__(self, shares, price, Next = None, prev = None):
        self.shares = shares
        self.price = price
        self.Next = None
        self.prev = None
        #self.prev = self
        self.size = 1

    def __repr__(self):
        return repr(str(self.shares) + " , " + str(self.price))

    def get(self):
        print("self is " + str(self))
        print("self.Next is " + str(self.Next))
        temp = self
        temp1 = self.prev
        temp2 = self.Next
        tempSize = self.size
        self.prev.Next = self.Next
        self.Next.prev = self.prev
        self = self.Next
        self.size = tempSize
        self.Next = temp.Next.Next
        self.prev = temp1
        self.size -= 1
        print("!!!!self is now " + str(self))
        print("!!!!self.next is now " + str(self.Next))
        return [temp.shares, temp.price]

    def put(self, item):
        #item.Next = self
        #item.prev = self.prev
        #self.prev.Next = item
        #self.prev = item
        if(self.size == 1):
            item.Next = self
            item.prev = self
            self.Next = item
            self.prev = item
            #print("self is " + str(self))
            #print("self.size is 1 and self.Next is " + str(self.Next))
            #print("self.prev is " + str(self.prev))
        else:
            temp = self.prev
            item.Next = self
            item.prev = self.prev
            self.prev.Next = item
            self.prev = item
            self.prev.prev = temp
            self.prev.Next = self
            self.size += 1
        #print("putting " + str(self.prev))
        return self

    def putFront(self, item):
        tempsize = self.size
        temp = self
        self.prev.Next = item
        self.prev = item
        self.prev.prev = temp
        self.prev.Next = self
        self = self.prev
        self.size = tempsize
        self.size +=  1

    def empty(self):
        if(self.Next):
            return True
        else:
            return False

class Stack(object):
    #stack class

    def __init__(self, shares, price, prev):
        self.shares = shares
        self.price = price
        self.prev = None

    def push(self, item):
        Prev = self
        self = item
        self.prev = Prev

    def pop(self):
        temp = self
        self = self.prev
        return temp

    def peek(self):
        return [self.shares, self.price]

    def size(self):
        return len(self.items)
                                                                        
main()
