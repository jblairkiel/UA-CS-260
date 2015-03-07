######################################## 
#   Blair Kiel
#   Project 3, CS260
#   1/23/2014 
#######################################

from scanner import *
import sys

def main():

    argv = sys.stdin
    lizt = []
    char = argv.readline()
    while char:
        if char not in " \t\n\r":
            char = char.rstrip() 
            lizt.append(char)
        char = argv.readline()
    n = lizt[0]
    f = lizt[1]
    b = lizt[2]
    s = lizt[3]

    head = TwoWayNode(data = 0)
    head.Next = head
    probe = head
    
    for i in range(1,int(n) + 1):
        #print("N is: " + str(n))
        #print("head is: " + str(head))
        #print("i is: " + str(i))
        j = i
        while j > 0 and probe.Next != head:
            prev = probe
            probe = probe.Next
            probe.prev = prev
            print("Probe loop probe is: " + str(probe))
            j += 1 
        temp = TwoWayNode(data = i)
        probe.Next = temp
        probe.Next.prev = probe 
        probe.Next.Next = head
        #print("Probe is: " + str(probe)) 
        #print("Probe.Next is: " + str(probe.Next))
        #print("Probe.prev is: " + str(probe.prev))
        #print("Probe.Next.Next is: " + str(probe.Next.Next))

    while probe.data != 0:
        probe = probe.Next
    
    sequence = list(s)
    for action in sequence:
        print(action)
        if(action == "t"): #Toggle Direction
            if(head.reverse == False): 
                probe.reverse == True
            else:
                probe.reverse == False
        elif(action == "m"): #Move Direction 
            probe.move
            print(probe)
        elif(action == "i"): #Increment current node value
            probe.increment
            print(probe)
        elif(action == "d"): #Decrement current node value
            probe.decrement
            print(probe)
        elif(action == "c"): #copy node value either in front or behind
            probe.copy
            print(probe)
        elif(action == "r"): #remove current node and print that node if list is empty| move to previous node if going forward and opposite
            probe.remove
            print(probe)
    print(probe)
    print(probe.Next)

class TwoWayNode(object):
    
    def __init__(self, data, Next = None, prev = None):
        self.data = data
        self.Next = Next
        self.prev = prev
        self.reverse = False

    def __repr__(self):
        return repr(int(self.data))


    def show(self):
        print(int(self.data))
        print(int(self.Next))
        print(int(self.prev))
        return
    
    def move(self): #move forward #
        if(self.reverse == False):
            for i in range(0,f):
                temp = TwoWayNode(self.Next, self.prev, self)
                print(temp)
                self = temp
        else:
            for i in range (0,b):
                temp = TwoWayNode(self.prev, self, self.Next)
                self = temps
        return self

    def increment(self):
        num = int(self)
        num = num + 1
        temp = TwoWayNode(num, self.Next, self.prev)
        self = temp
        return self 

    def decrement(self):
        num = int(self)
        num = num - 1
        temp = TwoWayNode(num, self.Next, self.prev)
        self = temp
        return self

    def copy(self):
        if(self.reverse == False):
            num = int(self)
            temp = TwoWayNode(num, num, self.prev)
            self = temp
            return self
        else:
            num = int(self)
            temp = TwoWayNode(num, self.Next, num)
            self = temp
            return self

    def remove(self):
        if(self.Next == None and self.prev == None):
            repr(int(self))
            return self
        if(a.reverse == False):
            temp = TwoWayNode(self.prev, self.Next, self.prev.prev)
            self = temp
        else:
            temp = TwoWayNode(self.Next, self.prev, self.prev.prev)
            self = temp
        return self

main()
        
