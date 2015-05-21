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
    pri[";"] = 0
    
    #read in each line
    iN = sys.stdin
    iLine = iN.readline()
    env = environmentStack()

    #while there is a line
    while iLine:
        iLine = iLine.strip("\n")
        iLine = iLine.strip("\t")
        iLine = iLine.replace("\r","")
        iLine = iLine.replace(" ","")
        iLine = iLine.replace(",","")
        a = list(iLine)
        #print("read line is " + str(a))
        #if there is a left brace
        if(a[0] == "{"):
            #print("a is " + str(a))
            #create  a new environment stack and push it on old stack
            newEnv = environmentStack()
            env = env.push(newEnv)
            if (a[1] == "@"):
                for i in range(2, len(a)):
                    if(a[i] != "," and a[i] != ";"):
                        env.lyst.append((a[i], 0))
                peekedList = env.peek()
                #for i in range(0, len(peekedList)):
                    #print("len(peekedList is " + str(len(peekedlist))
                    #print(str(peekedList[i][0]) + " = " + str(peekedList[i][1])) 
                #print("new environment is " + str(env.lyst))

        #elif c is a right brace
        elif(a[0] == "}"):
            #pop current scop from environment stack
            temp = env.pop()
            env = temp

        #elif c is a @ symbol
        elif(a[0] == "@"):
            #read list of identifyers and add them to current stack on environment
            for i in range(1, len(a)):
                if(a[i] != "," and a[i] != ";"):
                    env.lyst.append((a[i], 0))
            #peekedList = env.peek()
            #for i in range(0, len(peekedList)):
                #print("len(peekedList is " + str(len(peekedList)))
                #print(str(peekedList[i][0]) + " = " + str(peekedList[i][1]))

        #else if c is ?
        elif(a[0] == "?"):
            #read list of identifyers on current environment stack and display value
            #peekedList = env.peek()
            #print("peekedList is " + str(peekedList))
            for i in range(1, len(a)-1):
                temp = env
                foundFlag = False
                while(foundFlag == False):
                    peekedList = temp.peek()
                    for j in range(0, len(peekedList)):
                        if(a[i] == peekedList[j][0]):
                            print(str(peekedList[j][0]) + " = " + str(peekedList[j][1]))
                            foundFlag = True
                    temp = temp.prev
                
                
                #peekedList = temp.peek()
                #for j in range(0, len(peekedList)):
                #    if(a[i] == peekedList[j][0]):
                #        print(str(peekedList[j][0]) + " = " + str(peekedList[j][1]))

        #else if c is a lowercase letter
        elif(a[0].islower()):

            #evaluates vars before evaluating the expression
            for i in range(2, len(a)-1):
                if a[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
                    a[i] = lookUpVariable(a[i], env)

            exp = expressionStack(expression = [])
            var = a[0]
            arr = []
            #print("a is " + str(a))
            #print("a len is " + str(len(a)))
            i = 2
            while(i <= len(a)-1):
            #for i in range(2, len(a)):
                #print("expression stack is " + str(exp.expression))
                #print()
                #print("postFix is " + str(postFix))
                #print("i is " + str(i))
                #print("a[i] is " + str(a[i]))
                #print("exp stack is " + str(exp))
                if(isNumeric(a[i])):
                    #print("this is an integer " + str(a[i]))
                    exp.expression.append(a[i])
                    if(exp.operators != []):    
                        if(exp.operators[len(exp.operators)-1] == "^" and a[i+1] != "^"):#handles exponent case
                            newNum = compute(exp) 
                            exp.expression.append(newNum)
                elif(a[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
                    a[i] = lookUpVariable(a[i], env)
                    exp.expression.append(a[i])
                    #print("expression stack is " + str(exp.expression))
                elif(a[i] == "("):
                    newExp = expressionStack(expression = a[i])
                    exp.expression.append(a[i])
                    #exp.push(newExp)
                elif(a[i] == ")"):
                    top = exp.expression[len(exp.expression)-1]
                    if(exp.expression[len(exp.expression)-2] != "("):
                        while(top != "(" ):
                            #postFix.append(top)
                            #top = exp.pop()
                            newNum = compute(exp)
                            exp.expression.append(newNum)
                            if(len(exp.expression) > 1):
                                top = exp.expression[len(exp.expression)-2]
                                #print("top is " + str(top))
                                temp = exp.expression.pop()
                                exp.expression.pop()
                                exp.expression.append(temp)
                            else:
                                break
                                #print("expression is " + str(exp.expression[len(exp.expression)-1]))
                    #print("expression is " + str(exp.expression))
                elif(a[i] == "^" or a[i] == "+" or a[i] == "-" or a[i] == "*" or a[i] == "/"):
                    exp.expression.append(a[i])
                    #print("a[i] is " + str(a[i]))
                    #print("a[i+2] is " + str(a[i+2]))
                    #print("the env is " + str(env))
                    #print(pri[a[i+2]])
                    #print(pri[a[i]])
                    if(a[i] == "^" and a[i+2] == "^"):
                        exp.operators.append(a[i])
                    #elif(a[i] == "^"):
                    #    tempNum1 = exp.expression.pop()
                    #    tempNum2 = a[i+1]
                    #    tempExp = expressionStack()
                    elif(a[i+2]==";" or a[i+2] in "0123456789" or a[i+2] in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
                        exp.operators.append(a[i])
                    elif((isinstance(lookUpVariable(a[i+2],env), int) != True) and (pri[lookUpVariable(a[i+2], env)] <= pri[lookUpVariable(a[i], env)])): 
                        exp.expression.append(a[i+1])
                        exp.operators.append(a[i])
                        #print("expression stack is " + str(exp.expression))
                        i += 1
                        while(exp.operators != [] and pri[exp.operators[len(exp.operators)-1]] >= pri[a[i+1]]):
                        #while(exp.operators != []):
                                #print("operators is " + str(exp.operators))
                                #print("a[i+2] is " + str(a[i+1]))
                                #print("expression is " + str(exp.expression))
                                newNum = compute(exp)
                                exp.expression.append(newNum) 
                                exp.operators.pop()
                    else:
                        exp.operators.append(a[i])
                    #top = exp.peek()
                    #print("exp.expression is " + str(exp.expression))
                    #if(exp.expression != []):
                    #    top = exp.expression[len(exp.expression)-1]
                    #    #print("top is " + str(top))
                    #    while(exp.expression != [] and pri[top] >= pri[a[i]]):
                    #        #top = exp.expression.pop()
                    #        postFix.append(top)
                    #        top = exp.expression[len(exp.expression)-1]
                    #        top = exp.expression.pop()
                    #        #postFix.append(exp.pop())
                    #        #top = exp.peek()
                    #        #print("top is " + str(top))
                    #newExp = expressionStack(expression = a[i])
                    #exp.expression.append(a[i])
                    #exp.push(newExp)
                elif(a[i] == ";"):
                    j = len(exp.expression)
                    #print("len is " + str(j))
                    while(j > 1):
                        newNum = compute(exp)
                        exp.expression.append(newNum)
                        j = len(exp.expression) 
                    finalResult = exp.expression[0]
                i += 1
                    
            #print("final result is " + str(exp.expression[0]))

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
            #print("new env is " + str(env.lyst))

                        
        iLine = iN.readline()

def isNumeric(num):
    try:
        i = float(num)
        return True
    except (ValueError, TypeError):
        return False

def lookUpVariable(var, env):
    temp = env
    if(var in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
        #print("var is " + str(var))
        while(isinstance(var,int) == False):
            lyst = temp.lyst
            for j in lyst:
                if(var == j[0]):
                    var = j[1]
                    #print("var is now " + str(var))
                    return var
                    break
            temp = temp.prev
    else:
        var = var
    return var


def compute(exp):
    #print("expression list is " + str(exp.expression))
    num2 = exp.expression.pop()
    #print("num2 " + str(num2))
    op = exp.expression.pop()
    if(op not in "^*/+-"):
        return num2
    #print("op " + str(op))
    num1 = exp.expression.pop()
    if(num1 == "("):
        return num2
    num2 = int(num2)
    num1 = int(num1)
    #print("num1 " + str(num1))
    if(op == "^"):
        res = pow(num1, num2)
    elif(op == "*"):
        res = num1 * num2
    elif(op == "/"):
        res = num1 / num2
    elif(op == "+"):
        res = num1 + num2
    elif(op == "-"):
        res = num1 - num2
    #print("result is " + str(res) + " = " + str(num2) + " " + str(op) + " " + str(num1))
    return res


class environmentStack(object):
    #stack class for environment

    def __init__(self, Next = None, prev = None):
        self.lyst = []
        self.Next = self
        self.prev = self

    def __repr__(self):
        return repr(str(self.lyst))

    def push(self, item):
        item.prev = self
        self.Next = item
        self = item
        return self

    def pop(self):
        temp = self.prev
        temp2 = self.lyst
        temp3 = self.Next
        self = temp
        return temp

    def peek(self):
        return self.lyst

class expressionStack(object):
    #stack class for expression

    def __init__(self, expression, Next = None, prev = None):
        self.expression = []
        self.operators = []
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
