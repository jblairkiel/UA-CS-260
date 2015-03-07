######################################## 
#   Blair Kiel
#   Project 4, CS260
#   3/6/2014 
#######################################
from scanner import *
import sys

def main():

    inputFile = sys.argv[1]
    FiFoOutput = sys.argv[2]
    LiLoOutput = sys.argv[3]
    WtAvgOutput = sys.argv[4]

    #inputArray = ReadInputToArray(inputFile)
    #print(inputArray)
    fifoCalculation(inputFile, FiFoOutput)
    lifoCalculation(inputFile, LiLoOutput)
    wtAvgCalculation(inputFile, WtAvgOutput)

def fifoCalculation(inputFile, outFile):

    #print()
    #print("fifoCalculation")
    s = Scanner(inputFile)
    out = open(outFile,"w")
    line = s.readline()
    gTotal = 0
    qSize = 0
    q = None
    while(line != ""):
        arr = line.split()
        if(arr[0] == "Buy"):
            #print()
            #print('buying')
            if(q == None):
                #print("q is none")
                q = queue(arr[1],arr[2])
                #print("q is: " + str(q))
                q.prev = q
                q.Next = q
            else:
                f = queue(arr[1],arr[2])
                #print("buying: " + str(f))
                q.put(f)
                #print("q is: " + str(q))
            #print("qSize = " + str(q.size))
        elif(arr[0] == "Sell"):
            #print()
            #print("selling")
            sShare = int(arr[1])
            compShare = sShare
            sPrice = float(arr[2])
            #print('selling ' + str(sShare) + " at " + str(sPrice))
            sSalePrice = sShare * sPrice
            sRemainder = sShare
            sSum = 0
            sSumShares = 0
            while(compShare > 0 ):
                #print("q is " + str(q))
                b = q.get()
                bShare = int(b[0])
                #print("bShare is: " + str(bShare))
                #print(input("proceed?"))
                bPrice = float(b[1])
                dif = bShare - sShare
                #print()
                #print("bShare and bPrice: " + str(bShare) + " , " + str(bPrice))
                #print("bShare and compShare are " + str(bShare) + " , " + str(compShare))
                if(bShare < compShare): #100 < 200
                    #print("test1")
                    bRem = compShare - bShare
                    #print("bRem is " + str(bRem) + " = " + str(compShare) + " - " + str(bShare))
                    bBoughtPrice = bShare * bPrice
                    #print("bBought Price is " + str(bBoughtPrice) + " = " + str(bShare) + " * " + str(bPrice))
                    sSum += bBoughtPrice
                    q = q.Next
                    #print(q)
                    compShare -= bShare
                elif(bShare > compShare): #400 > 100
                    #print("test2")
                    bRem = compShare
                    bRemainder = bShare - compShare
                    bBoughtPrice = bRem * bPrice
                    #print("bBought Price is " + str(bBoughtPrice) + " = " + str(bRem) + " * " + str(bPrice))
                    sSum += bBoughtPrice
                    q.shares = bRemainder
                    #print(q)
                    compShare -= bShare
                else:
                    #print("test3")
                    bRem = 0
                    bBoughtPrice = bShare * bPrice
                    #print("bBought Price is " + str(bBoughtPrice) + " = " + str(bShare) + " * " + str(bPrice))
                    sSum += bBoughtPrice
                    q = q.Next
                    #print(q)
                    compShare -= bShare
                    #print("bShare is " + str(bShare))
                    #print("compShare is " + str(compShare))
                #elif(bShare == compShare):
                #print("sSum is now: " + str(sSum))

            sSumShares = sRemainder - bShare
            total = sSalePrice - sSum
            #print("total is " + str(sSalePrice) + " - " + str(sSum) + " = " + str(total))
            gTotal += total
            #print("gTotal is now " + str(gTotal))
            if(total > 0):
                #print("     Gain = " + str(total))
                out.write("Gain = " + str("{:.2f}".format(total)) + "\n")
            elif(total == 0):
                #print("Zero")
                out.write("Zero\n")
            else:
                #print("     Loss = " + str(total))
                out.write("Loss = " + str("{:.2f}".format(total)) + "\n")
            #print("q is now " + str(q))
            #print()
        line = s.readline()
    gTotal = "{:.2f}".format(gTotal)
    out.write("Total = " + str(gTotal))
    #print(gTotal)
    s.close()
    out.close()


            #while((not q.empty()) and (compShare > 0)):
                #print("problem here q is " + str(q))
                #b = q.get()
                #print("q is " + str(q))
                #print("q.get() is " + str(b))
                #bShare = int(b[0])
                #bPrice = int(float(b[1]))
                #print()
                #print("bShare and bPrice: " + str(bShare) + " , " + str(bPrice))
                #print("bShare is " + str(bShare))
                #print("bPrice is " + str(bPrice))
                #if((bShare - compShare) > 0): #if selling shares are less than the available buying shares
                #    print("q is now " + str(q))
                #    bRem = bShare - compShare
                #    print("bShare - compShare = " + str(bRem))
                #    bBoughtPrice = compShare * bPrice
                #    print("bBoughtPrice = " + str(bBoughtPrice) + " = " + str(compShare) + " * " + str(bPrice))
                #    if(q.Next == q):
                #        f = queue(str(bRem), b[1])
                #        q = f
                #        print("new is created")
                #    elif((bRem - compShare) > 0):
                #        q.shares = str(bRem)
                #        q.price = b[1]
                #        print("case 2")
                #    elif((compShare - bShare) <= 0): #if during the first subtraction there is available stock remaining
                #        print("case 3")
                #        q.shares = str(bRem)
                #        q.price = b[1]
                #    else:
                #        q = q.Next
                #else:
                #    bRem = bShare - sSumShares
                #    bBoughtPrice = bRem * bPrice
                #q = q.Next
                #sSum += bBoughtPrice
                #sSumShares = sRemainder - bShare
                #total = sSalePrice - sSum
                #compShare = compShare - bShare
                #print("total is " + str(sSalePrice) + " - " + str(sSum) + " = " + str(total))
            #bShare = bShare - bRem
            #gTotal += total
            #if(total > 0):
            #    print("Gain = " + str(total))
            #else:
            #    print("Loss = " + str(total))
            #print()
        #line = s.readline()
    #print("Total = " + str(gTotal))
    #s.close()

def lifoCalculation(inputFile, outFile):

    #print()
    #print("LiLoCalculation")
    #stack = []
    s = Scanner(inputFile)
    out = open(outFile,"w")
    line = s.readline()
    gTotal = 0
    sSize = 0
    s2 = None
    while(line != ""):
        arr = line.split()
        #print("qSize = " + str(sSize))
        if(arr[0] == "Buy"):
            #print()
            if(s2 == None):
                #print("q is none")
                s2 = stack(arr[1],arr[2])
                #print("buying: " + str(s2))
                s2.prev = s2
            else:
                f = stack(arr[1],arr[2])
                #print("buying: " + str(f))
                s2.push(f)
                temp = s2
                s2 = f
                s2.prev = temp
            #print("s2 is now: " + str(s2))
            #print("s2.prev is now: " + str(s2.prev))
            #print()
            #print("Buying")
            #print("stack is now: " + str(stack))
        elif(arr[0] == "Sell"):
            #print()
            sShare = int(arr[1])
            compShare = sShare
            sPrice = float(arr[2])
            #print("selling: " + str(sShare) + " at " + str(sPrice))
            sSalePrice = sShare * sPrice
            sRemainder = sShare
            sSum = 0;
            sSumShares = 0;
            #while(compShare > 0 ):
            while(compShare > 0):
                b = s2.peek()
                #print("b is " + str(b))
                bShare = int(b[0])
                bPrice = float(b[1])
                #print("bShare and bPrice: " + str(bShare) + " , " + str(bPrice))
                #print(input("Proceed?"))
                if(bShare < compShare): #100 < 200 poping stack
                    #print("test1")
                    bRem = compShare - bShare
                    bBoughtPrice = bShare * bPrice
                    #print("bBought Price is " + str(bBoughtPrice) + " = " + str(bShare) + " * " + str(bPrice))
                    sSum += bBoughtPrice
                    s2 = s2.prev
                    compShare -= bShare
                    #print("compShare is: " + str(compShare))
                elif(bShare > compShare): #400 > 100
                    #print("test2")
                    bRem = compShare
                    bRemainder = bShare - compShare
                    #print("bRemainder " + str(bRemainder) + " = " + str(bShare) + " - " + str(compShare))
                    bBoughtPrice = bRem * bPrice
                    #print("bBought Price is " + str(bBoughtPrice) + " = " + str(bRem) + " * " + str(bPrice))
                    sSum += bBoughtPrice
                    s2.shares = bRemainder
                    #print("s2.shares is " + str(s2.shares))
                    compShare -= bShare
                    #print("compShare is: " + str(compShare))
                else:
                    #print("test3")
                    bRem = 0
                    bBoughtPrice = bShare * bPrice
                    #print("bBought Price is " + str(bBoughtPrice) + " = " + str(bShare) + " * " + str(bPrice))
                    sSum += bBoughtPrice
                    s2 = s2.prev
                    compShare -= bShare
                    #print("compShare is: " + str(compShare))
                #print("sSum is : " + str(sSum))
                #print(stack)
                #b = stack.pop()
                #bShare = int(b[0])
                #bPrice = float(b[1])
                ##print("bShare is " + str(bShare))
                ##print("bPrice is " + str(bPrice))
                #if((bShare - compShare) > 0): #if selling shares are less than the available buying shares
                #    bRem = bShare - compShare
                #    bBoughtPrice = compShare * bPrice
                #    print("bBoughtPrice: " + str(bBoughtPrice) + " = " + str(compShare) + " * " + str(bPrice))
                #    a = stack
                #    aSize = sSize
                #    stack.append([str(bRem),b[1]])
                #    while(aSize >= 2):
                #        temp = a.pop()
                #        aSize = aSize - 1
                #        #print("temp is " + str(temp))
                #        stack.append(temp)
                #else:
                #    bRem = bShare - sSumShares
                #    bBoughtPrice = bRem * bPrice
                #sSum += bBoughtPrice
                ##print("total is " + str(sSalePrice) + " - " + str(sSum) + " = " + str(total))
                #compShare = compShare - bShare
            bShare = bShare - bRem
            total = sSalePrice - sSum
            #print("total " + str(total) + " = " + str(sSalePrice) + " - " + str(sSum))
            gTotal += total
            if(total > 0):
                out.write("Gain = " + str("{:.2f}".format(total)) + "\n")
                #print("Gain = " + str(total))
            elif(total == 0):
                #print("Zero")
                out.write("Zero\n")
            else:
                #print("Loss = " + str(total))
                out.write("Loss = " + str("{:.2f}".format(total)) + "\n")
            #print()
            sSize -= 1
        line = s.readline()
    gTotal = "{:.2f}".format(gTotal)
    out.write("Total = " + str(gTotal))
    #print(gTotal)
    s.close()
    out.close()
    
def wtAvgCalculation(inputFile, outFile):

    #print()
    #print("wtAvgCalculation")
    s = Scanner(inputFile)
    out = open(outFile,"w")
    line = s.readline()
    gTotal = 0
    totalShares = 0
    totalAvg = 0
    mean = 0
    qSize = 0
    q = queue(0,0)
    while(line != ""):
        arr = line.split()
        if(arr[0] == "Buy"):
            totalShares += float(arr[1])
            #print("total Shares is " + str(totalShares))
            totalAvg += float(arr[1]) * float(arr[2])
            #print("totalAvg is " + str(totalAvg) + " = " + str(int(arr[1])) + " * " + str(arr[2]))
            mean = totalAvg / totalShares
            #print("mean is " + str(mean) + " = " + str(totalAvg) + " / " + str(totalShares))
            q.shares = totalShares
            q.price = mean
            #print("q is: " + str(q))
            #print("qSize = " + str(q.size))
        elif(arr[0] == "Sell"):
            #print()
            #print("selling")
            #print("q is " + str(q))
            sShare = float(arr[1])
            compShare = sShare
            sPrice = float((arr[2]))
            #print('selling ' + str(sShare) + " at " + str(sPrice))
            sSalePrice = sShare * sPrice
            b = q.get()
            bShare = float(b[0])
            bPrice = float(b[1])
            #print("bShare is " + str(bShare))
            #print("bPrice is " + str(bPrice))
            sRemainder =  bShare - sShare
            #print("sRemainder is " + str(sRemainder) + " = " + str(bShare) + " - " + str(sShare))
            f = queue(sRemainder, mean)
            q = f
            sSum = 0
            #mean = round(mean, 2)
            available = sShare * mean
            #avaliable = round(float(available), 2)
            #print("available = " + str(available) + " = " + str(sShare) + " * " + str(mean))
            total = sSalePrice - available
            #total = round(float(total), 2)
            #print("total is = " + str(available) + " = " + str(sSalePrice) + " - " + str(available))
            gTotal += total
            totalShares = float(totalShares - sShare)
            totalAvg = float(totalShares * mean)
            #print("totalAvg is " + str(totalAvg) + " = " + str(sRemainder) + " * " + str(mean))
            #print("totalShares is " + str(totalShares))
            #print("gTotal is now " + str(gTotal))
            #total = "{:.2f}".format(total)
            if(total > 0):
                #print("Gain = " + str(total))
                out.write("Gain = " + str("{:.2f}".format(total)) + "\n")
            elif(total == 0):
                print("Zero")
                #out.write("Zero\n")
            else:
                #print("Loss = " + str(total))
                out.write("Loss = " + str("{:.2f}".format(total)) + "\n")
            #print("q is now " + str(q))
            #print()
        line = s.readline()
    gTotal = "{:.2f}".format(gTotal)
    out.write("Total = " + str(gTotal))
    #print(gTotal)
    s.close()
    out.close()


    #s = Scanner(inputFile)
    #line = s.readline()
    #gTotal = 0
    #qSize = 0
    #q = None
    #while(line != ""):
    #    arr = line.split()
    #    print("qSize = " + str(qSize))
    #    if(arr[0] == "Buy"):
    #        if(q == None):   
    #            q = queue(arr[1], arr[2])
    #        else:
    #            f = queue(arr[1], arr[2])
    #            q.put(f)
    #        qSize += 1
    #    elif(arr[0] == "Sell"):
    #        sShare = int(arr[1])
    #        compShare = sShare
    #        sPrice = int(float((arr[2])))
    #        sSalePrice = sShare * sPrice
    #        sRemainder = sShare
    #        sSum = 0;
    #        sSumShares = 0;
    #        #while(compShare > 0 ):
    #        while((q.empty() == False) and (compShare > 0)):
    #            a = q
    #            aSize = q.size
    #            totalShares = 0
    #            totalPrice = 0 
    #            while((a.empty() == False)):
    #                temp = a.get()
    #                bShare = int(temp[0])
    #                bPrice = int(float(b[1]))
    #                totalShares = bShare + totalShares
    #                totalPrice = bPrice + totalPrice
    #                mean = totalPrice / totalShares
    #            b = q.get()
    #            bShare = int(b[0])
    #            bPrice = int(float(b[1]))
    #            print("bShare is " + str(bShare))
    #            print("bPrice is " + str(bPrice))
    #            if((bShare - compShare) > 0): #if selling shares are less than the available buying shares
    #                bRem = bShare - compShare
    #                bBoughtPrice = compShare * bPrice
    #                a = q
    #                aSize = qSize
    #                f = queue(str(bRem), b[1])
    #                q.put(f)
    #                while(aSize >= 2):
    #                    temp = a.get()
    #                    f = queue(temp[0],temp[1])
    #                    aSize = aSize - 1
    #                    print("temp is " + str(temp))
    #                    q.put(temp)
    #            else:
    #                bRem = bShare - sSumShares
    #                bBoughtPrice = bRem * bPrice
    #            sSum += bBoughtPrice
    #            sSumShares = sRemainder - bShare
    #            total = sSalePrice - sSum
    #            print("total is " + str(sSalePrice) + " - " + str(sSum) + " = " + str(total))
    #            compShare = compShare - bShare
    #        bShare = bShare - bRem
    #        gTotal += total
    #        total = "{:.2f}".format(total)
    #        if(total > 0):
    #            print("Gain = " + str(total))
    #        else:
    #            print("Loss = " + str(total))
    #        print()
    #    line = s.readline()
    #print("Total = " + str(gTotal))
    #s.close()

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
        self.Next = self
        self.rear = self
        self.prev = prev
        #self.prev = self
        self.size = 1

    def __repr__(self):
        return repr(str(self.shares) + " , " + str(self.price) + " and " + str(self.Next.shares) + " , " + str(self.Next.price))

    def get(self):
        temp = self
        temp2 = self.rear
        temp3 = self.Next
        self = self.Next
        self.rear = temp2
        self.size -= 1
        return [temp.shares, temp.price]
    
    def put(self, item):
        #item.Next = self
        #item.prev = self.prev
        #self.prev.Next = item
        #self.prev = item
        self.rear.Next = item
        self.rear.rear = item
        self.rear = item
        self.size += 1

    def putFront(self, item):
        self.prev = item
        temp = self
        tempsize = self.size
        self = self.prev
        self.size = tempsize
        self.Next = temp
        self.Next.prev = None
        self.prev = None
        self.size +=  1

    def empty(self):
        if(self.Next):
            return True
        else:
            return False

class stack(object):
    #stack class

    def __init__(self, shares, price, Next = None, prev = None):
        self.shares = shares
        self.price = price
        self.prev = self
        self.Next = self

    def __repr__(self):
        return repr(str(self.shares) + " , " + str(self.price))
        #return repr(str(self.shares) + " , " + str(self.price) + " and " + str(self.prev.shares) + " , " + str(self.prev.price))

    def __str__(self):
        return str(str((self.shares)) + " , " + str(self.price))

    def push(self, item):
        temp = self
        self = item
        self.prev = temp

    def pop(self):
        temp = self.prev
        temp2 = self.shares
        temp3 = self.price
        self = temp
        return [temp2, temp3]

    def peek(self):
        temp = self.prev
        temp2 = self.shares
        temp3 = self.price
        return [temp2, temp3]

    def size(self):
        return len(self.items)
                                                                        
main()
