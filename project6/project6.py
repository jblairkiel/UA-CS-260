######################################## 
#   Blair Kiel
#   Project 6, CS260
#   4/12/2014
#######################################
from scanner import *
import sys

def main():
    
    inputFile = sys.argv[1]
    minCostOutput = sys.argv[2]
    maxCostOutput = sys.argv[3]

    minCostCalculation(inputFile, minCostOutput)
    maxCostCalculation(inputFile, maxCostOutput)

def minCostCalculation(inputFile, outputFile):
    s = Scanner(inputFile)
    out = open(outputFile, "w")
    line = s.readline()
    gTotal = 0
    qSize = 0
    q = None
    #read in line
    # arr[0] is buy or sell
    # arr[1] is num of shares
    # arr[2] is name of stock
    # arr[3] is price of stock
    while(line != ""):
        arr = line.split()
        #if buy
        if(arr[0] == "Buy"):
            #if there is no tree create one
            if(q == None):
            #    print("there is no tree")
                q = BST()
                temp = minTree(arr[2])
                temp.add((int(arr[1]),float(arr[3])))
                q.insert(arr[2], temp)
            #else add a leaf to the binary tree
            else:
                #find the correct stock
                temp = q.inOrderFind(arr[2])
                if temp == None:
                    temp = minTree(name = arr[2])
                    temp.add((int(arr[1]),float(arr[3])))
                    q.insert(arr[2], temp)
                elif temp.name == arr[2]:
                    tempArr = q.inOrderReadToArray(arr[2])
                    newTree = BST()
                    #create new tree and add the array to it
                    for i in tempArr:
                        if(i.name == arr[2]):
                            i.data.add((int(arr[1]), float(arr[3])))
                            i.data.size += 1
                            newTree.insert(i.name, i.data)
                        else:
                            newTree.insert(i.name, i.data)
                    q = newTree
        #elif sell
        elif(arr[0] == "Sell"):
            #get the correct heap from the BST
            mHeap = q.inOrderFind(arr[2])

            sShare = int(arr[1])
            compShare = sShare
            sPrice = float(arr[3])
            sSalePrice = sShare * sPrice
            sRemainder = sShare
            sSum = 0
            sSumShares = 0

            #while there is still more to sell
            while(compShare > 0):
                c = mHeap.data #.data #.heap #.pop()
                b = c.pop()
                bShare = int(b[0])
                bPrice = float(b[1])
                dif = bShare - sShare
                #if there are plenty or shares left to sell
                if(bShare < compShare):
                    bRem = compShare - bShare
                    bBoughtPrice = bShare * bPrice
                    sSum += bBoughtPrice
                    compShare -=bShare

                #if there is going to be a remainder of shares we want to put them back into the heap
                elif(bShare > compShare):
                    bRem = compShare
                    bRemainder = bShare - compShare
                    bBoughtPrice = bRem * bPrice
                    sSum += bBoughtPrice
                    #add the new data back into the heap
                    newData = (int(bRemainder), float(bPrice))
                    mHeap.data.add(newData)
                    compShare -= bShare
                #else
                else:
                    bRem = 0
                    bBoughtPrice = bShare * bPrice
                    sSum += bBoughtPrice
                    compShare -= bShare

            #subtotal calculations
            sSumShares = sRemainder - bShare
            total = sSalePrice - sSum
            gTotal += total
            #there is a profit from selling
            if(total > 0):
                out.write("Gain = " + str("{:.2f}".format(total)) + "\n")

            #no money was made
            elif(total == 0):
                out.write("Zero\n")

            #else: there is a loss from selling
            else:
                out.write("Loss = " + str("{:.2f}".format(total)) + "\n")

            #add the correct heap back to the bst
            tempArr = q.inOrderReadToArray(arr[2])
            newTree = BST()
            #create new tree and add the array to it
            for i in tempArr:
                if(i.name == arr[2]):
                    newTree.insert(arr[2], mHeap.data)
                else:
                    newTree.insert(i.name, i.data)
            q = newTree

        #read in next stock transaction
        line = s.readline()
    #final calculations
    gTotal = "{:.2f}".format(gTotal)
    out.write("Total = " + str(gTotal))
    s.close()
    out.close()

def maxCostCalculation(inputFile, outputFile):
    s = Scanner(inputFile)
    out = open(outputFile, "w")
    line = s.readline()
    gTotal = 0
    qSize = 0
    q = None
    #read in line
    # arr[0] is buy or sell
    # arr[1] is num of shares
    # arr[2] is name of stock
    # arr[3] is price of stock
    while(line != ""):
        arr = line.split()
        #if buy
        if(arr[0] == "Buy"):
            #if there is no tree create one
            if(q == None):
                q = BST()
                temp = maxTree(arr[2])
                temp.add((int(arr[1]),float(arr[3])))
                q.insert(arr[2], temp)
            #else add a leaf to the binary tree
            else:
                #find the correct stock
                temp = q.inOrderFind(arr[2])
                #did not find the stock so create one
                if temp == None:
                    temp = maxTree(name = arr[2])
                    temp.add((int(arr[1]),float(arr[3])))
                    q.insert(arr[2], temp)
                #found the stock
                elif temp.name == arr[2]:
                    tempArr = q.inOrderReadToArray(arr[2])
                    newTree = BST()
                    #create new tree and add the array to it
                    for i in tempArr:
                        if(i.name == arr[2]):
                            i.data.add((int(arr[1]), float(arr[3])))
                            i.data.size += 1
                            newTree.insert(i.name, i.data)
                        else:
                            newTree.insert(i.name, i.data)
                    q = newTree
        #elif sell
        elif(arr[0] == "Sell"):
            #get the correct heap from the BST
            mHeap = q.inOrderFind(arr[2])

            sShare = int(arr[1])
            compShare = sShare
            sPrice = float(arr[3])
            sSalePrice = sShare * sPrice
            sRemainder = sShare
            sSum = 0
            sSumShares = 0

            #while there is still more to sell
            while(compShare > 0):
                c = mHeap.data
                b = c.pop()
                bShare = int(b[0])
                bPrice = float(b[1])
                dif = bShare - sShare
                #if there are plenty of stocks to still sell
                if(bShare < compShare):
                    bRem = compShare - bShare
                    bBoughtPrice = bShare * bPrice
                    sSum += bBoughtPrice
                    compShare -=bShare

                #elif there is going to be a remainder of stocks to put back into heap
                elif(bShare > compShare):
                    bRem = compShare
                    bRemainder = bShare - compShare
                    bBoughtPrice = bRem * bPrice
                    sSum += bBoughtPrice
                    #put remainder shares back into heap
                    newData = (int(bRemainder), float(bPrice))
                    mHeap.data.add(newData)
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
            #there is a profit of stocks
            if(total > 0):
                out.write("Gain = " + str("{:.2f}".format(total)) + "\n")
            #there was no gain or loss
            elif(total == 0):
                out.write("Zero\n")
            #there was a loss in selling
            else:
                out.write("Loss = " + str("{:.2f}".format(total)) + "\n")

            #add the correct heap back to the bst
            tempArr = q.inOrderReadToArray(arr[2])
            newTree = BST()
            #create new tree and add the array to it
            for i in tempArr:
                if(i.name == arr[2]):
                    newTree.insert(arr[2], mHeap.data)
                else:
                    newTree.insert(i.name, i.data)
            q = newTree

        #read in the next transaction
        line = s.readline()
    #perform final calculations
    gTotal = "{:.2f}".format(gTotal)
    out.write("Total = " + str(gTotal))
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

class  minTree(object):
    #minimum ordered

    def __init__(self, name):
        self.name = name
        self.heap = []
        self.size = 0

    def add(self, item):
        #adds item into the minimum ordered heap
        self.size += 1
        self.heap.append(item)
        curPos = len(self.heap) - 1
        while curPos > 0:
            parent = (curPos -1) //2
            parentItem = self.heap[parent]
            if(parentItem[1] <= item[1]):
                break
            else:
                self.heap[curPos] = self.heap[parent]
                self.heap[parent] = item
                curPos = parent

    def __repr__(self):
        strs = ""
        for i in self.heap:
            strs += str(i) + " -> " 
        return self.name + ": " + strs
            

    def pop(self):
        #removes the lowest priced stock
        self.size -= 1
        topItem = self.heap[0]
        bottomItem = self.heap.pop(len(self.heap) - 1)
        if (len(self.heap) == 0):
            return bottomItem
        self.heap[0] = bottomItem
        newTop = self.heap[0]
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
                if(leftItem < rightItem):
                    minChild = leftChild
                else:
                    minChild = rightChild
            minItem = self.heap[minChild]
            if (newTop[1] <= minItem[1]):
                break
            else:
                self.heap[curPos] = self.heap[minChild]
                self.heap[minChild] = bottomItem
                curPos = minChild
        return topItem

class  maxTree(object):
    #max ordered

    def __init__(self, name):
        self.name = name
        self.heap = []
        self.size = 0

    def add(self, item):
        #adds item according to max order
        self.size += 1
        self.heap.append(item)
        curPos = len(self.heap) - 1
        while curPos > 0:
            parent = (curPos -1) //2
            parentItem = self.heap[parent]
            if(parentItem[1] >= item[1]):
                break
            else:
                self.heap[curPos] = self.heap[parent]
                self.heap[parent] = item
                curPos = parent

    def __repr__(self):
        strs = ""
        for i in self.heap:
            strs += str(i) + " -> "
        return self.name + ": " + strs


    def pop(self):
        #removes the maximum priced stock
        self.size -= 1
        topItem = self.heap[0]
        bottomItem = self.heap.pop(len(self.heap) - 1)
        if (len(self.heap) == 0):
            return bottomItem
        self.heap[0] = bottomItem
        newTop = self.heap[0]
        lastIndex = len(self.heap) - 1
        curPos = 0
        while True:
            leftChild = 2 * curPos + 1
            rightChild = 2 * curPos + 2
            if(leftChild > lastIndex):
                break
            if(rightChild > lastIndex):
                maxChild = leftChild
            else:
                leftItem = self.heap[leftChild]
                rightItem = self.heap[rightChild]
                if (leftItem[1] > rightItem[1]):
                    maxChild = leftChild
                else:
                    maxChild = rightChild
            maxItem = self.heap[maxChild]
            if (newTop[1] >= maxItem[1]):
                break
            else:
                self.heap[curPos] = self.heap[maxChild]
                self.heap[maxChild] = bottomItem
                curPos = maxChild
        return topItem

class BSTNode:
    def __init__(self, name, data, L=None, R=None):
        self.name = name
        self.data = data
        self.left = L
        self.right = R
        
class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, name, data):
        def recurse(p):
            if(min(name,p.name) == name):
                if(p.left==None):
                    p.left = BSTNode(name, data)
                else:
                    recurse(p.left)
            else:
                if(p.right==None):
                    p.right = BSTNode(name, data)
                else:
                    recurse(p.right)
        if(self.root==None):
            self.root = BSTNode(name, data)
        else:
            recurse(self.root)

    def inOrderFind(self, toBeFound):
        #returns found node
        temp = None
        def recurse(node):
            if node != None:
                if(self.root.name == toBeFound):
                    foundNode = self.root
                    return foundNode
                if(node.left != None and node.left.name == toBeFound):
                    foundNode = node.left
                    return foundNode
                else:
                    foundNode = recurse(node.left)
                    if(foundNode != None):
                        return foundNode
                if(node.right != None and node.right.name == toBeFound):
                    foundNode = node.right
                    return foundNode
                else:
                    foundNode = recurse(node.right)
                    if(foundNode != None):
                        return foundNode
        temp = recurse(self.root)
        return temp

    def delete(self, toBeDeleted):
        #unimplemented delete method
        temp = self
        def recurse(node):
            if(node != None):
                if(node.left != None and node.left.name == toBeDeleted):
                    node.left = None
                    return node
                else:
                    recurse(node.left)
                if(node.right != None and node.right.name == toBeDeleted):
                    node.right = None
                    return node
                else:
                    recurse(node.right)
        recurse(self.root)
        return temp

    def inOrderPrint(self):
        #print("InOrder BST is:     ")
        def recurse(node):
            if(isinstance(node, str) == False and node != None):
                recurse(node.left)
                print(node.data)
                recurse(node.right)
        recurse(self.root)

    def inOrderReadToArray(self, x):
        # this will read the tree to array except for x
        #updated this will now read all tree nodes to the array
        arr = []
        def recurse(node):
            if(isinstance(node,str) == False and node != None):
                recurse(node.left)
                arr.append(node)
                recurse(node.right)
        recurse(self.root)

        return arr

main()
