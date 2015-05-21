######################################## 
#   Blair Kiel
#   Project 6, CS260
#   3/6/2014 
#######################################
from scanner import *
import sys

def main():
    
    inputFile = sys.argv[1]
    minCostOutput = sys.argv[2]
    maxCostOutput = sys.argv[3]

    minCostCalculation(inputFile, MinCostOutput)

def minCostCalculation(inputFile, outputFile):
    s = Scanner(inputFile)
    out = open(outFile, "w")
    line = s.readline()
    gTotal = 0
    qSize = 0
    q = None
    #read in line
    while(line != ""):
        arr = line.split()
        #if buy
        if(arr[0] == "Buy"):
            #if there is no tree create one
            if(q == None):
                q = minTree()
                q.add((int(arr[1]),float(arr[2])))
            #else add a leaf to the binary tree
            else:
                q.add((int(arr[1]),float(arr[2])))

        #elif sell
            sShare = int(arr[1])
            compShare = sShare
            sPrice = float(arr[2])
            sSalePrice = sShare * sPrice
            sRemainder = sShare
            sSum = 0
            sSumShares = 0

            #while there is still more to sell
            while(compShare > 0):
                b = q.pop()
                bShare = int(b[0])
                bPrice = float(b[1])
                dif = bShare - sShare
                #if bShare < compShare
                if(bShare < compShare):
                    bRem = compShare - bShare
                    bBoughtPrice = bShare * bPrice
                    sSum += bBoughtPrice

                #elif bShare > compShare
                elif(bShare > compShare):
                    bRem = compShare
                    bRemainder = bShare - compShare
                    bBoughtPrice = bRem * bPrice
                    sSum += bBoughtPrice
                    t = q.heap[0] # this may be the issue
                    tShare = t[0]
                    tPrice = t[1]
                    q.heap[0][0] = bRemainder
                    compShare -= bShare
                #else
                else:
                    bRem = 0
                    bBoughtPrice = bShare * bPrice
                    sSum += bBoughtPrice
                    compShare -= bShare

            sSumShares = sRemainder - bShare
            total = sSalePrice - sSum
            gTotal += total
            #if total > 0 Gain
            if(total > 0):
                #out.write("Gain = " + str("{:.2f}".format(total)) + "\n")
                print("Gain = " + str(total))

            #elif total == 0 print zero
            elif(total == 0):
                #out.write("Zero\n")
                print("Zero")

            #else: Loss
            else:
                #out.write("Loss = " + str("{:.2f}".format(total)) + "\n")
                print("Losst = " + str(total))

        line = s.readline()
    gTotal = "{:.2f}".format(gTotal)
    #out.write("Total = " + str(gTotal))
    print("Total = " + str(gTotal))
    s.close()
    out.close()

def ReadInputToArray(inputFile):

    #reads inputfile to array i can work with
    
    s = Scanner(inputFile)
    items = []
    line = s.readline()
    arr = line.split()
    while(line != ""):
        items.append(arr)
        line = s.readLine
        arr = line.split()
    s.close()
    return items

def minTree(AbstractCollection):
    #minimum ordered

    def __init__(self, sourceCollection = None):
        self.heap = []
        AbstractCollection.__init__(self, sourceCollection)
        self.size = 0

    def add(self, item):
        self.size += 1
        self.heap.append(item)
        curPos = len(self.heap) - 1
        parent = (curPos - 1) // 2
        while(curPos > 0 and self.heap[parent] > item):
            self.heap[curPos] = self.heap[parent]
            curPos = parent
            parent = (curPos - 1) //2
        self.heap[curPos] = item

    def pop(self):
        self.size -= 1
        topItem = self.heap[0]
        bottomItem = self.heap.pop(len(self.heap) - 1)
        if (len(self.heap) == 0):
            return bottomItem

        self.heap[0] = bottomItem
        lastIndex = len(self.heap) - 1
        curPos = 0
        while True:
            leftChild = 2 * curPos + 1
            rightChild = 2 * curPos + 2
            if(leftChild > lastIndex):
                break
            if(rightChild > lastIndex):
                minChild = leftChild
            else:
                leftItem = self.heap[leftChild]
                rightItem = self.heap[rightChild]
                if (leftItem < rightItem):
                    minChild = leftChild
                else:
                    minChild = rightChild
            minItem = self.heap[minChild]
            if (bottomItem <= minItem):
                break
            else:
                self.heap[curPos] = self.heap[minChild]
                self.heap[minChild] = bottomItem
                curPos = minChild
        return topItem

class BSTNode:
    def __init__(self, x, L=None, R=None):
        self.data = x
        self.left = L
        self.right = R
        
class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, x):
        def recurse(p):
            if(x<p.data):
                if(p.left==None):
                    p.left = BSTNode(x)
                else:
                    recurse(p.left)
            else:
                if(p.right==None):
                    p.right = BSTNode(x)
                else:
                    recurse(p.right)
        if(self.root==None):
            self.root = BSTNode(x)
        else:
            recurse(self.root)

