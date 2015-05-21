####################
# Blair Kiel
# Project 5
# Due 3/27/2015
###################
from scanner import *
import re
import sys

def main():

    #encountered priority error so i created my own
    pri = {}
    pri["^"] = 3
    pri["/"] = 2
    pri["*"] = 2
    pri["-"] = 1
    pri["+"] = 1
    pri["("] = 0
    pri[")"] = 0
    
    #read in each line
    iN = sys.stdin
    iLine = iN.readline()
    env = environmentStack()

    #while there is a line
    while iLine:
        iLine = iLine.strip("\n")
        iLine = iLine.replace("\r","")
        iLine = iLine.replace(" ","")
        iLine = iLine.replace(",","")
        a = list(iLine)
        #print(a)
        #if there is a left brace
        if(a[0] == "{"):
            #create  a new environment stack and push it on old stack
            newEnv = environmentStack()
            env.push(newEnv)

        #elif c is a right brace
        elif(a[0] == "}"):
            #pop current scop from environment stack
            env.pop()

        #elif c is a @ symbol
        elif(a[0] == "@"):
            #read list of identifyers and add them to current stack on environment
            for i in range(1, len(a)):
                if(a[i] != "," and a[i] != ";"):
                    env.lyst.append((a[i], 0))
            peekedList = env.peek()
            #for i in range(0, len(peekedList)):
                #print("len(peekedList is " + str(len(peekedList)))
                #print(str(peekedList[i][0]) + " = " + str(peekedList[i][1]))

        #else if c is ?
        elif(a[0] == "?"):
            #read list of identifyers on current environment stack and display value
            peekedList = env.peek()
            for i in range(0, len(peekedList)):
                print(str(peekedList[i][0]) + " = " + str(peekedList[i][1]))

        #else if c is a lowercase letter
        elif(a[0].islower()):
            #exp = expressionStack(expression = None)
            exp = expressionStack(expression = [])
            var = a[0]
            postFix = []
            #print("a is " + str(a))
            #print("a len is " + str(len(a)))
            for i in range(2, len(a)):
                #print()
                #print("postFix is " + str(postFix))
                #print("a[i] is " + str(a[i]))
                #print("exp stack is " + str(exp))
                if(a[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                    temp = env
                    while(a[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                        lyst = temp.lyst
                        for j in lyst:
                            if(a[i] == lyst[j][0]):
                                a[i] = lyst[j][1]
                                break
                        temp = temp.prev
                    postFix.append(a[i])
                elif(a[i] in "0123456789"):
                    postFix.append(a[i])
                elif(a[i] == "("):
                    newExp = expressionStack(expression = a[i])
                    exp.expression.append(a[i])
                    #exp.push(newExp)
                elif(a[i] == ")"):
                    #top = exp.pop()
                    top = exp.expression.pop()
                    while(top != "("):
                        postFix.append(top)
                        #top = exp.pop()
                        top = exp.expression.pop()
                elif(a[i] == "^" or a[i] == "+" or a[i] == "-" or a[i] == "*" or a[i] == "/"):
                    #top = exp.peek()
                    #print("exp.expression is " + str(exp.expression))
                    if(exp.expression != []):
                        top = exp.expression[len(exp.expression)-1]
                        #print("top is " + str(top))
                        while(exp.expression != [] and pri[top] >= pri[a[i]]):
                            #top = exp.expression.pop()
                            postFix.append(top)
                            top = exp.expression[len(exp.expression)-1]
                            top = exp.expression.pop()
                            #postFix.append(exp.pop())
                            #top = exp.peek()
                            #print("top is " + str(top))
                    newExp = expressionStack(expression = a[i])
                    exp.expression.append(a[i])
                    #exp.push(newExp)

            while(exp.expression != []):
            #while(exp.isEmpty() != True):
                #top = exp.pop()
                top = exp.expression.pop()
                postFix.append(top)

            #print("postFix expression is " + str(postFix))
            #calculate
            arr = []
            tokenList = postFix
            for i in tokenList:
                if i in "0123456789":
                    arr.append(int(i))
                else:
                    op2 = arr.pop()
                    op1 = arr.pop()
                    if(i == "^"):
                        #print("op2 is " + str(op2))
                        #print("op1 is " + str(op1))
                        #res = pow(op2, op1)
                        res = op2 ^ op1
                        #print("result is " + str(res) + " = " + str(op2) + " ^" + str(op1))
                    elif(i == "*"):
                        res = op1 * op2
                    elif(i == "/"):
                        res = op1 / op2
                    elif(i == "+"):
                        res = op1 + op2
                    elif(i == "-"):
                        res = op1 - op2
                    arr.append(int(res))
            finalResult = arr.pop()

            #print("finalResult is " + str(finalResult))

            #return value to environment
            temp = env
            flag = False
            while(flag == False):
                lyst = temp.lyst
                for j in range(0,len(lyst)):
                    #print("len is " + str(len(lyst)))
                    #print(lyst[j][0])
                    #print(var)
                    if(var == lyst[j][0]):
                        #print("list " + str(lyst[j][0]))
                        lyst[j] = (var, finalResult)
                        #lyst[j][1] = finalResult
                        flag = True
                        break
                temp = temp.prev

                        
        iLine = iN.readline()

class environmentStack(object):
    #stack class for environment

    def __init__(self, Next = None, prev = None):
        self.lyst = []
        self.Next = self
        self.prev = self

    def __repr__(self):
        return repr(str(self.lyst))

    def push(self, item):
        temp = self
        self.Next = item
        self = item
        self.prev = temp

    def pop(self):
        temp = self.prev
        temp2 = self.lyst
        temp3 = self.Next
        self = temp
        return temp2

    def peek(self):
        return self.lyst

class expressionStack(object):
    #stack class for expression

    def __init__(self, expression, Next = None, prev = None):
        self.expression = []
        self.Next = self
        self.prev = self
        if(self.expression == None):
            self.size = 0
        else:
            self.size = 1

    def __repr__(self):
        return repr(str(self.expression))

    def push(self, item):
        item.prev = self
        self = item
        self.size += 1

    def pop(self):
        temp = self.prev
        self = temp
        self.size -= 1
        return temp

    def peek(self):
        return self.expression

    def isEmpty(self):
        if(self.expression == None):
            return True
        else:
            return False


main()
