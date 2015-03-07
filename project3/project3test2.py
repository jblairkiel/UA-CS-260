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
    head.prev = head
    probe = head
    
    for i in range(1,int(n) + 1):
        j = i
        while j > 0 and probe.Next != head:
            prev = probe
            probe = probe.Next
            j -= 1 
        temp = TwoWayNode(data = i, prev = probe, Next = probe.Next)
        probe.Next.prev = temp 
        probe.Next = temp
        last = temp

    while probe.data != 1:
        probe = probe.Next
    probe = probe.prev
    probe.prev = temp

    for j in range(0, int(n)+1):
        probe.count += 1

    loopingSequence(n, f, b, s, probe)
    #print(probe.data)
    #print(probe.Next)
    #print(probe.Next.Next)
    #print(probe.Next.Next.Next)
    #print(probe.Next.Next.Next.Next)
    #print(probe.Next.Next.Next.Next.Next)

def loopingSequence(n, f, b, s, probe):
    count = 0
    n = n
    f = f
    b = b
    s = s
    probe = probe
    sequence = list(s)
    increment = 0
    while(probe.Next != None and probe.prev !=None):
        count += 1
        action = s[increment]
        increment += 1
        if (increment == len(s)):
           increment = 0 
        #print("   " + action)
        if(action == "t" or action == "T"): #Toggle Direction
            if(probe.reverse == False): 
                probe.reverse = True
            else:
                probe.reverse = False
        elif(action == "m" or action == "M"): #Move Direction FIX next.data and prev.data
            reverse = probe.reverse
            if(probe.reverse == False):
                count = probe.count
                for i in range(0, int(f)):
                    probe = probe.Next
                    #point = probe.prev
                    #temp = TwoWayNode(probe.Next.data, probe.Next.Next, probe)
                    #temp.count = probe.count
                    #temp.reverse = probe.reverse
                    #probe = temp
                probe.reverse = reverse
                probe.count = count
            else:
                count = probe.count
                for i in range(0, int(b)):
                    probe = probe.prev
                    #temp = TwoWayNode(probe.prev.data, probe, probe.prev.prev)
                    #temp.count = probe.count
                    #temp.reverse = probe.reverse
                    #probe = temp
                probe.reverse = reverse
                probe.count = count
            #probe.move
        elif(action == "i" or action == "I"): #Increment current node value
            num = str(probe.data)
            num1 = int(num)
            num2 = (int(num1) + 1) % int(n)
            #print("num1 is: " + str(num1))
            #print("n is: " + str(n))
            #print("probe.count is: " + str(probe.count))
            #print("num2 is: (num1 + 1) % n: " + str(num2))
            count = probe.count
            reverse = probe.reverse
            
            #implement
            if(probe.Next == probe and probe.prev == probe):
                temp = TwoWayNode(num2, None, None)
                temp.Next = temp
                temp.prev = temp
            else:
                temp = TwoWayNode(num2, probe.Next, probe.prev)
                probe = temp
                probe.Next.prev = probe
                probe.prev.Next = probe
            probe = temp
            probe.count = count
            probe.reverse = reverse
            #probe.increment

        elif(action == "d" or action == "D"): #Decrement current node value
            num = str(probe.data)
            num1 = int(num)
            num2 = (num1 - 1) % (int(n))
            #print("num1 is: " + str(num1))
            #print("n is: " + str(n))
            #print("probe.count is: " + str(probe.count))
            #print("num2 is: (num1 - 1) % n: " + str(num2))
            count = probe.count
            reverse = probe.reverse

            #implement
            if(probe.Next == probe and probe.prev == probe):
                temp = TwoWayNode(num2, None, None)
                temp.Next = temp
                temp.prev = temp
            else:
                temp = TwoWayNode(num2, probe.Next, probe.prev)
                probe = temp
                probe.Next.prev = probe
                probe.prev.Next = probe
            probe = temp
            probe.count = count
            probe.reverse = reverse
            #probe.decrement

        elif(action == "c" or action == "C"): #copy node value either in front or behind ENDED HERE
            if(probe.reverse == False):
                num = probe.data
                probe.insert()
            else:
                num = probe.data
                probe.insert()
            #probe.copy
        elif(action == "r" or action == "R"): #remove current node and print that node if list is empty| move to previous node if going forward and opposite
            if(probe.Next == probe and probe.prev == probe):
                print(probe)
                break
            if(probe.reverse == False):
                count = probe.count
                reverse = probe.reverse

                #print("prior probe.prev is: " + str(probe.prev))
                #print("prior probe is: " + str(probe))
                #print("prior probe.Next is: " + str(probe.Next))

                #next
                probe.Next.prev = probe.prev
                #print("probe.Next.prev is: " + str(probe.prev))
                #prev
                probe.prev.Next = probe.Next
                #print("probe.prev.Next is: " + str(probe.Next))

                removed = probe.data
                probe = probe.prev
                probe.count = count - 1
                probe.reverse = reverse

                #print("new probe.prev is: " + str(probe.prev))
                #print("new probe is: " + str(probe))
                #print("new probe.Next is: " + str(probe.Next))
            else:

                count = probe.count
                reverse = probe.reverse

                #next
                probe.Next.prev = probe.prev
                #prev
                probe.prev.Next = probe.Next

                removed = probe.data
                probe = probe.Next
                probe.count = count - 1
                probe.reverse = reverse
                #print(probe.data)
                #print(probe.Next)
                #print(probe.Next.Next)
            
               
        #probe.remove

        #print("probe.reverse is: " + str(probe.reverse))
        #print("probe.count is: " + str(probe.count))
        #print("reverse is: " + str(probe.reverse))
        #print("probe.prev is: " + str(probe.prev))
        #print(probe.data)
        #print(probe.Next)
        #print(probe.Next.Next)
        #print(probe.Next.Next.Next)
        #print(probe.Next.Next.Next.Next)
        #print(probe.Next.Next.Next.Next.Next)
        #print(probe.Next.Next.Next.Next.Next.Next)
        #print(probe.Next.Next.Next.Next.Next.Next.Next)
        #print(probe.Next.Next.Next.Next.Next.Next.Next.Next)
        #print(probe.Next.Next.Next.Next.Next.Next.Next.Next.Next)
        #print(probe.Next.Next.Next.Next.Next.Next.Next.Next.Next.Next)
        #print(probe.Next.Next.Next.Next.Next.Next.Next.Next.Next.Next.Next)
    #print(removed)
    #print(probe)
    #print(probe.Next)
    print(count)

class TwoWayNode(object):
    
    def __init__(self, data, Next = None, prev = None):
        self.data = data
        self.Next = Next
        self.prev = prev
        self.count = 0
        self.reverse = False

    def __repr__(self):
        return repr(int(self.data))

    def insert(self):
        num = self.data
        if(self.reverse == False):
            temp1 = TwoWayNode(num, self, self.prev)
            self.prev = temp1
            self.prev.prev.Next = temp1
        else:
            temp1 = TwoWayNode(num, self.Next, self)
            self.Next.prev = temp1
            self.Next = temp1
        reverse = self.reverse
        self.count = self.count + 1
        count = self.count
        temp1.reverse = reverse
        temp1.count = count
        #print("self.prev.prev is: " + str(self.prev.prev))
        #print("self.prev.prev.Next is: " + str(self.prev.prev.Next))
        #print("self.prev is: " + str(self.prev))
        #print("self is: " + str(self))
        #print("self.Next is: " + str(self.Next))
        #print("self.Next.Next is: " + str(self.Next.Next))
        #print("self.Next.Next.Next is: " + str(self.Next.Next.Next))
        #print("self.Next.Next.Next.Next is: " + str(self.Next.Next.Next.Next))
        #print("self.Next.Next.Next.Next.Next is: " + str(self.Next.Next.Next.Next))

main()
        
