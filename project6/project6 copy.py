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
            #print()
            #print("buying: " + str(arr[1]) + " of " + str(arr[2]) + " for " + str(arr[3]))
            if(q == None):
            #    print("there is no tree")
                q = BST()
                temp = minTree(arr[2])
                temp.add((int(arr[1]),float(arr[3])))
            #    print(temp)
                q.insert(arr[2], temp)
            #else add a leaf to the binary tree
            #find the correct stock
            else:
                temp = q.inOrderFind(arr[2])
                if temp == None:
            #        print("Creating new heap")
                    temp = minTree(name = arr[2])
                    temp.add((int(arr[1]),float(arr[3])))
            #        print()
                    #print("temp.data " + str(temp.data))
                    q.insert(arr[2], temp)
            #        print("after adding new heap, " + str(q.inOrderPrint()))
                elif temp.name == arr[2]:
            #        print("Found a heap in the tree")
                    #temp = minTree(name = arr[2])
                    tempArr = q.inOrderReadToArray(arr[2])
                    newTree = BST()
                    #create new tree and add the array to it
                    #tempArr.append(int(arr[1]), float(arr[3]))
                    #tempArr[0].heap.append((int(arr[1]), float(arr[3])))
                    for i in tempArr:
                        if(i.name == arr[2]):
                            i.data.add((int(arr[1]), float(arr[3])))
                            i.data.size += 1
                            newTree.insert(i.name, i.data)
                        else:
                            newTree.insert(i.name, i.data)
                    #print("arr is " + str(arr))
                    #temp.data.add((int(arr[1]),float(arr[3])))
            #        print(temp.data)
                    #working to this point
                    #print("tree before is " + str(q))
                    q = newTree
            #        print("tree after is " + str(newTree.inOrderPrint()))
                    #q.insert(arr[2], temp)
                    #print(q)
                    #q.insert(arr[2], temp)
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
                #repr(b)
                b = c.pop()
                bShare = int(b[0])
                bPrice = float(b[1])
                dif = bShare - sShare
                #if bShare < compShare
                if(bShare < compShare):
                    bRem = compShare - bShare
                    bBoughtPrice = bShare * bPrice
                    sSum += bBoughtPrice
                    # added this
                    compShare -=bShare

                #elif bShare > compShare
                elif(bShare > compShare):
                    bRem = compShare
                    bRemainder = bShare - compShare
                    bBoughtPrice = bRem * bPrice
                    sSum += bBoughtPrice
                    #t = mHeap.heap[0] # this may be the issue
                    #tShare = t[0]
                    #tPrice = t[1]
                    #added this
                    newData = (int(bRemainder), float(bPrice))
                    mHeap.data.add(newData)
                    #mHeap.heap[0][0] = bRemainder
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
                out.write("Gain = " + str("{:.2f}".format(total)) + "\n")
                #print("Gain = " + str(total))

            #elif total == 0 print zero
            elif(total == 0):
                out.write("Zero\n")
                #print("Zero")

            #else: Loss
            else:
                out.write("Loss = " + str("{:.2f}".format(total)) + "\n")
                #print("Lost = " + str(total))

            #add the correct heap back to the bst
            tempArr = q.inOrderReadToArray(arr[2])
            newTree = BST()
            #create new tree and add the array to it
            for i in tempArr:
                if(i.name == arr[2]):
                    newTree.insert(arr[2], mHeap.data)
                else:
                    newTree.insert(i.name, i.data)
            #print(temp.data)
            q = newTree

        #q.inOrderPrint()    
        line = s.readline()
    gTotal = "{:.2f}".format(gTotal)
    out.write("Total = " + str(gTotal))
    #print("Total = " + str(gTotal))
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
            #print()
            #print("buying: " + str(arr[1]) + " of " + str(arr[2]) + " for " + str(arr[3]))
            if(q == None):
            #    print("there is no tree")
                q = BST()
                temp = maxTree(arr[2])
                temp.add((int(arr[1]),float(arr[3])))
            #    print(temp)
                q.insert(arr[2], temp)
            #else add a leaf to the binary tree
            #find the correct stock
            else:
                temp = q.inOrderFind(arr[2])
                if temp == None:
            #        print("Creating new heap")
                    temp = maxTree(name = arr[2])
                    temp.add((int(arr[1]),float(arr[3])))
            #        print()
                    #print("temp.data " + str(temp.data))
                    q.insert(arr[2], temp)
            #        print("after adding new heap, " + str(q.inOrderPrint()))
                elif temp.name == arr[2]:
            #        print("Found a heap in the tree")
                    #temp = minTree(name = arr[2])
                    tempArr = q.inOrderReadToArray(arr[2])
                    newTree = BST()
                    #create new tree and add the array to it
                    #tempArr.append(int(arr[1]), float(arr[3]))
                    #tempArr[0].heap.append((int(arr[1]), float(arr[3])))
                    for i in tempArr:
                        if(i.name == arr[2]):
                            i.data.add((int(arr[1]), float(arr[3])))
                            i.data.size += 1
                            newTree.insert(i.name, i.data)
                        else:
                            newTree.insert(i.name, i.data)
                    #print("arr is " + str(arr))
                    #temp.data.add((int(arr[1]),float(arr[3])))
            #        print(temp.data)
                    #working to this point
                    #print("tree before is " + str(q))
                    q = newTree
                    #print("tree after is " + str(newTree.inOrderPrint()))
                    #q.insert(arr[2], temp)
                    #print(q)
                    #q.insert(arr[2], temp)
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
                #repr(b)
                b = c.pop()
                bShare = int(b[0])
                bPrice = float(b[1])
                dif = bShare - sShare
                #if bShare < compShare
                if(bShare < compShare):
                    bRem = compShare - bShare
                    bBoughtPrice = bShare * bPrice
                    sSum += bBoughtPrice
                    # added this
                    compShare -=bShare

                #elif bShare > compShare
                elif(bShare > compShare):
                    bRem = compShare
                    bRemainder = bShare - compShare
                    bBoughtPrice = bRem * bPrice
                    sSum += bBoughtPrice
                    #t = mHeap.heap[0] # this may be the issue
                    #tShare = t[0]
                    #tPrice = t[1]
                    #added this
                    newData = (int(bRemainder), float(bPrice))
                    mHeap.data.add(newData)
                    #mHeap.heap[0][0] = bRemainder
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
                out.write("Gain = " + str("{:.2f}".format(total)) + "\n")
                #print("Gain = " + str(total))

            #elif total == 0 print zero
            elif(total == 0):
                out.write("Zero\n")
                #print("Zero")

            #else: Loss
            else:
                out.write("Loss = " + str("{:.2f}".format(total)) + "\n")
                #print("Lost = " + str(total))

            #add the correct heap back to the bst
            tempArr = q.inOrderReadToArray(arr[2])
            newTree = BST()
            #create new tree and add the array to it
            for i in tempArr:
                if(i.name == arr[2]):
                    newTree.insert(arr[2], mHeap.data)
                else:
                    newTree.insert(i.name, i.data)
            #print(temp.data)
            q = newTree

        #q.inOrderPrint()
        line = s.readline()
    gTotal = "{:.2f}".format(gTotal)
    out.write("Total = " + str(gTotal))
    #print("Total = " + str(gTotal))
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

        #parent = (curPos - 1) // 2

        #while(curPos > 0 and self.heap[parent][1] > item[1]):
        #    self.heap[curPos] = self.heap[parent]
        #    curPos = parent
        #    parent = (curPos - 1) //2
        #self.heap[curPos] = item
    
    def __repr__(self):
        strs = ""
        for i in self.heap:
            strs += str(i) + " -> " 
        return self.name + ": " + strs
            

    def pop(self):
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
            #if(leftChild > lastIndex):
            if(leftChild > lastIndex):
                break
            #if(rightChild > lastIndex):
            if(rightChild > lastIndex):
                minChild = leftChild
            else:
                leftItem = self.heap[leftChild]
                rightItem = self.heap[rightChild]
                #if (leftItem < rightItem):
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
    #minimum ordered

    def __init__(self, name):
        self.name = name
        self.heap = []
        self.size = 0

    def add(self, item):
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

        #parent = (curPos - 1) // 2

        #while(curPos > 0 and self.heap[parent][1] > item[1]):
        #    self.heap[curPos] = self.heap[parent]
        #    curPos = parent
        #    parent = (curPos - 1) //2
        #self.heap[curPos] = item

    def __repr__(self):
        strs = ""
        for i in self.heap:
            strs += str(i) + " -> "
        return self.name + ": " + strs


    def pop(self):
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
            #if(name<p.name):
            #self.inOrderPrint()
            #print("name is " + str(name))
            #print("pname is " + str(p.name))
            #if name < p.name
            if(min(name,p.name) == name):
                if(p.left==None):
                    p.left = BSTNode(name, data)
                else:
                    #print("we are recursing left to " + str(p.left.name))
                    #print("p.left is " + str(p.left))
                    recurse(p.left)
            else:
                if(p.right==None):
                    p.right = BSTNode(name, data)
                else:
                    #print("we are recursing right to " + str(p.right.name))
                    #print("p.right is " + str(p.right))
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
                    #print("found temp " + str(temp))
                    return foundNode
                else:
                    foundNode = recurse(node.left)
                    if(foundNode != None):
                        return foundNode
                if(node.right != None and node.right.name == toBeFound):
                    foundNode = node.right
                    #print("found temp " + str(temp))
                    return foundNode
                else:
                    foundNode = recurse(node.right)
                    if(foundNode != None):
                        return foundNode
        temp = recurse(self.root)
        ##self.root = None
        return temp

    def delete(self, toBeDeleted):
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
        #print()
        #print("InOrder BST is:     ")
        def recurse(node):
            if(isinstance(node, str) == False and node != None):
                recurse(node.left)
                #print(node)
                print(node.data)
                #repr(node.data)
                recurse(node.right)
        recurse(self.root)
        #print( )

    def inOrderReadToArray(self, x):
        # this will read the tree to array except for x
        arr = []
        def recurse(node):
            if(isinstance(node,str) == False and node != None):
                recurse(node.left)
                #print("x is " + str(x))
                #print("node.data.name is " + str(node.data.name))
                #print("node.data is " + str(node.data))
                #print("node.data is " + str(node.data))
                #print("node.data is " + str(node.data))
                arr.append(node)
                recurse(node.right)
        recurse(self.root)
        #print("arr is " + str(arr))

        return arr

main()
