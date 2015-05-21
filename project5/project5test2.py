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
    i = 0
    #while there is a line
    while iLine:
        iLine = iLine.strip("\n")
        iLine = iLine.replace("\r","")
        print("removing r " + str(iLine))
        iLine = iLine.replace(" ","")
        iLine = iLine.replace(",","")
        a = list(iLine)
        print(a)

        #if a is a left brace
        if(a[0] == "{"):
            #create a new environment stack and push it on it the old stack

            #print("a[0] is " + str(a))
            newEnv = environmentStack()
            env.push(newEnv)

        #else if c is right brace
        elif(a[0] == "}"):
            #pop current scope from environment stack
            env.pop()

        #else if c is @ symbol
        elif(a[0] == "@"):  
            #read list of identifyers and add them to current stack on environment
            for i in range(1, len(a)):
                if(a[i] != "," and a[i] != ";"):
                    env.lyst.append((a[i], 0))
            peekedList = env.peek()
            for i in range(0, len(peekedList)):
                print(str(peekedList[i][0]) + " = " + str(peekedList[i][1]))

        #else if c is ? 
        elif(a[0] == "?"):
            #read list of identifyers on current environment stack and display their values
            peekedList = env.peek()
            for i in range(0, len(peekedList)):
                print(str(peekedList[i][0]) + " = " + str(peekedList[i][1]))

        #else if c is a lowercase letter
        elif(a[0].islower()):
            #c must be left side of assignment statement
            var = a[0]
            exp = expressionStack(expression = "")
            postFix = []
            dar = []
            print("a is " + str(a))
            print("a len is " + str(len(a)))
            for i in range(2, len(a)):
                print()
                print("postFix is " + str(postFix))
                print("a[i] is " + str(a[i]))
                if(a[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                    #print("works")
                    #find the corresponding variable
                    temp = env
                    while(a[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                        lyst = temp.lyst
                        for j in lyst:
                            if(a[i] == lyst[j][0]):
                                print("a[i] was " + str(a[i]))
                                a[i] = lyst[j][1] 
                                print("a[i] is now " + str(a[i]))
                                break
                        temp = temp.prev
                    postFix.append(a[i])
                elif(a[i] in "0123456789"):
                    postFix.append(a[i])
                #if(a[i] == "*" or a[i] == "/" or a[i] == "-" or a[i] == "+" or a[i] == "^"):
                #    print("operand is " + str(a[i]))
                #    postFix.append(a[i])
                elif(a[i] == "("):
                    newExp = expressionStack(expression = a[i])
                    exp.push(newExp)
                elif(a[i] == ")"):
                    top = exp.pop()
                    print("top is " + str(top))
                    #while(top != "("):
                    while(top != "("):
                        #dar.append(top)
                        postFix.append(top)
                        print("postfix is " + str(postFix))
                        print("top is " + str(top))
                        print("exp is " + str(exp))
                        top = exp.pop()
                elif(a[i] == "^" or a[i] == "+" or a[i] == "-" or a[i] == "*" or a[i] == "/"): #
                    #print()
                    #print("postFix is " + str(postFix))
                    #print("lenth is " + str(len(postFix)))
                    #print("a[i] is " + str(a[i]))
                    print("exp is " + str(exp))
                    #print("postFix priority is " + str(postFix[len(postFix)-1].getPriority()))
                    #print("top is " + str(top))
                    #print("top is " + str(top))
                    #print("top priority is " + str(top.getPriority()))
                    #print("expPriority is " + str(exp.peek().getPriority()))
                    #a[i].getPriority()
                    #print(a[i].getPriority())
                    top = exp.peek()
                    while((exp.size != 0) and pri[top] >= pri[a[i]]):
                    #while(exp.expression != None  and pri[top] >= pri[a[i]]):
                        #top = exp.pop()
                        #print("operator at top is " + str(top))
                        postFix.append(exp.pop())
                        top = exp.peek()
                    newExp = expressionStack(expression = a[i])
                    print("newExp is " + str(newExp))
                    exp.push(newExp)
                    exp.expression = a[i]
                    print("exp is " + str(exp))

            print("this is something " + str(postFix))
            while(exp.isEmpty() != True):
                postFix.append(exp.pop())
                exp = exp.prev

            #calculate term
            
            print("postFix expression is" + str(postFix))
                        
                    

            #read the right side of the assignment statement

            #evaluate the right side of the assignemnt statement using expression stack

            #update the value on the left side in the current environment scope

    #read in next line
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
        temp = self.prev
        temp2 = self.lyst
        temp3 = self.Next
        return temp2
    
class expressionStack(object):
    #stack class for expression

    def __init__(self, expression = None,Next = None, prev = None):
        self.expression = expression
        self.Next = self
        self.prev = self
        if(self.expression == None):
            self.size = 0
        else:
            self.size = 1

    def __repr__(self):
        return repr(str(self.expression))

    def push(self, item):
        temp = self
        self = item
        self.prev = temp
        self.size += 1

    def pop(self):
        temp = self.prev
        temp1 = self.expression
        temp2 = self
        self = temp
        if(temp2 == None):
            self.size -=1
        else:
            #self.size = temp2.size
            self.size -= 1
        return temp1

    def peek(self):
        print("peeking " + str(self.expression))
        return self.expression

    def isEmpty(self):
        if(self.expression == None):
            return True
        else:
            return False

    def evaluate(self):
        #evaluate
        print("stuff")
main()
