from scanner import *
import re
import sys

def main():

    iN = sys.stdin #need to change to sys.stdin
    iLine = iN.readline()
    env = environmentStack()
    exp = expressionStack(None)
    evaluateNext = False
    i = 0
    while iLine:
        iLine = iLine.strip("\r\n")
        a = list(iLine)

        ## if a is a space we need to find the actual first variable
        while(a[0] == " "):
            a.pop(0)

        ## if a is left brace
        if(a[0] == "{"):
            #print("a is " + str(a))
            newEnv = environmentStack()
            newEnv.prev = env
            env.Next = newEnv
            env = newEnv
            
            
        ##else if c is right brace
        if(a[0] == "}"):
            env.pop()
            
        ##else if c is @ symbol
        if(a[0] == "@"):
            for i in range(1, len(a)):
                if(a[i] != "," and a[i] != ";"):
                    env.lyst.append((a[i], 0))
            peekedList = env.peek()
            for i in range(0, len(peekedList)):
                print(str(peekedList[i][0]) + " = " + str(peekedList[i][1]))

        ##else if c is a question mark
        if(a[0] == "?"):
            peekedList = env.peek()
            for i in range(0, len(peekedList)):
                print(str(peekedList[i][0]) + " = " + str(peekedList[i][1]))

        ##else if c is a lowercase letter
        if(a[0].islower()):
            var = a[0]
            for i in range(4, len(a)):
                ## if c is (
                if(a[i] == "("):
                    #try to do nothing
                    newExp = expressionStack(a[i])
                    exp.push

                ##if c is )
                if(a[i] == ")"):
                    exp.evaluate

                ##if c is int
                elif(isinstance(a[i], int)):
                    newExp = expressionStack(a[i])
                    exp.push(newExp)
                    if(evaluateNext == True): 
                        exp.evaluate()
                        evaluateNext = False
                    
                ##if c is var we must search current environment and get the current value
                elif(a[i].islower()):
                    peekedList = env.peek()
                    var1 = ""
                    j = len(peekedList) - 1
                    while(j > -1 and var1 == ""):
                        if(a[i] == peekedList[j][0]):
                            var1 = peekedList[j][0] 
                            print("var1 is " + str(var1))
                            j = -1
                        else:
                            print("a[i] is now " + str(peekedList[j][0]) + " looking for " + str(a[i]))
                            j -= 1
                    newExp = expressionStack(var1)
                    exp.push(newExp) 
                    var1 = ""

                ##if c is an operand
                elif(a[i] == "^"):
                    #high priority
                    evaluateNext = True
                    newExp = expressionStack(int(a[i]))
                    exp.push(newExp)

                elif(a[i] == "*" or "/" or "+" or "-"):
                    print("a[i] is: " + str(a[i]))
                    newExp = expressionStack(a[i])
                    exp.push(newExp)
                    #low priority


            print(a[0])
            print("exp is " + str(exp))
            print("env is " + str(env))

        iLine = iN.readline()


class environmentStack(object):
    #stack class for enviroment

    def __init__(self, Next = None, prev = None):
        self.lyst = []
        self.Next = self
        self.prev = self

    def __repr__(self):
        return repr(str(self.lyst))

    def push(self, item):
        temp = self
        self = item
        self.prev = temp
        self.prev.Next = self

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
    #stack class for expressions

    def __init__(self, expression, Next = None, prev = None):
        self.expression = expression
        self.highestPriority = None
        self.evalNext = "no"
        self.Next = self
        self.prev = self
        self.size = 1

    def __repr__(self):
        return repr(str(self.expression))

    def push(self, item):
        temp = self
        self = item
        self.prev = temp
        self.prev.Next = self
        self.size += 1

    def pop(self):
        temp = self.prev
        temp2 = self.shares
        temp3 = self.price
        self = temp
        self.size -= 1
        return self.expression

    def peek(self):
        temp = self.prev
        temp2 = self.shares
        temp3 = self.price
        return self.expression

    def size(self):
        return self.size

    def evaluate(self):
        #determine priority of operand

        #evaluate
        c = 1
        sString = ""
        while(self.size > 0):
            #loop through expressions
            a = self.pop()
            sString = sString + str(a)
        num = eval(sString)
        print(num)
            
    def stupid(self):
        if(isinstance(a, int)):
            b = self.pop()
            if(b == "*"):
                temp = self.pop()
                c = temp*a
            elif(b == "/"):
                temp = self.pop()
                c = temp/a
            elif(b == "+"):
                temp = self.pop()
                c = temp+a

                

        elif(a == ")"):
            temp = self.pop()
            while(temp != "("):
                print("stupid")
        
        #if a is )
        elif(a == ")"):

            #if b is )
            if(b == ")"):

                #if c is int
                if(c == ")"):
                #if(isinstance(c, int)):
                    print("stupid")
                #else it is )

            #if b is int
            elif(isinstance(b, int)):
                print("stupid")

                #c is operand
        

        #if a is int
        elif(isinstance(a, int)):


            #if c is )
            if(c == ")"):
                print("stupid")
        
            #if c is operand
            elif(c == "("):
                print("stupid")

            else:
                print("stupid")

        
        #put calculated expression in environment stack
        #create new expression stack



main()



