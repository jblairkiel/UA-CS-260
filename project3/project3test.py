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
        #print("N is: " + str(n))
        #print("head is: " + str(head))
        #print("i is: " + str(i))
        j = i
        while j > 0 and probe.Next != head:
            prev = probe
            probe = probe.Next
            j -= 1 
        temp = TwoWayNode(data = i, prev = probe, Next = probe.Next)
        #probe.next = temp
        probe.Next.prev = temp 
        probe.Next = temp
        #print("Probe is: " + str(probe)) 
        #print("Probe.Next is: " + str(probe.Next))
        #print("Probe.prev is: " + str(probe.prev))
        #print("Probe.Next.Next is: " + str(probe.Next.Next))

    while probe.data != 1:
        probe = probe.Next
    probe = probe.prev

    for j in range(0, int(n)):
        probe.count += 1

    #print(probe.data)
    #print(probe.Next)
    #print(probe.Next.Next)
    #print(probe.Next.Next.Next)
    #print(probe.Next.Next.Next.Next)
    #print(probe.Next.Next.Next.Next.Next)

    

    
    sequence = list(s)
    for action in sequence:
        print(" " + action)
        if(action == "t"): #Toggle Direction
            if(probe.reverse == False): 
                probe.reverse == True
            else:
                probe.reverse == False
        elif(action == "m"): #Move Direction 
            if(probe.reverse == False):
                for i in range(0, int(f)):
                    temp = TwoWayNode(probe.Next, probe.Next.Next, probe)
                    temp.count = probe.count
                    temp.reverse = probe.reverse
                    probe = temp
            else:
                for i in range(0, int(b)):
                    temp = TwoWayNode(probe.prev, probe, probe.prev.prev)
                    temp.count = probe.count
                    temp.reverse = probe.reverse
                    probe = temp
            #probe.move
        elif(action == "i"): #Increment current node value
            num = str(probe.data)
            num1 = int(num)
            num1 += 1
            count = probe.count
            reverse = probe.reverse
            tempArray = []

            for i in range(0, int(count)):
                tempArray.append(int(probe.data))
                probe = probe.Next
            print("tempArray is: " + str(tempArray))


            #probe.next block
            #temp1 = TwoWayNode(num1, probe.Next, probe.prev)
            #probe.Next.data = probe.Next.data
            #probe.Next.Next = probe.Next.Next
            #probe.Next = TwoWayNode(probe.Next.data, probe.Next.Next, temp1)
            #probe.prev block
            #probe.prev.data = probe.prev.data
            #probe.prev.Next = probe.prev.Next
            #probe.prev = TwoWayNode(probe.prev.data, temp1, probe.prev.prev)

            temp = TwoWayNode(num1, probe.Next, probe.prev)
            probe = temp
            #probe.increment
        elif(action == "d"): #Decrement current node value
            num = str(probe.data)
            num1 = int(num)
            num1 -= 1
            temp = TwoWayNode(num1, probe.Next, probe.prev)
            probe = temp
            #probe.decrement
        elif(action == "c"): #copy node value either in front or behind
            if(probe.reverse == False):
                num = probe.data
                temp = TwoWayNode(num, num, probe.prev)
                probe = temp 
            else:
                num = probe.data
                temp = TwoWayNode(num, probe.Next, num)
                probe = temp
            #probe.copy
        elif(action == "r"): #remove current node and print that node if list is empty| move to previous node if going forward and opposite
            if(probe.Next == None and probe.prev == None):
                print(probe)
            if(probe.reverse == False):
                tempArray = []
                prev = str(probe.prev.data)
                Next = str(probe.Next.data)
                count = probe.count
                reverse = probe.reverse
                tempArray.append(int(prev))
                tempArray.append(int(Next))
                probe = probe.Next
                probe.count = count
                probe.reverse = reverse
                for i in range(0, int(probe.count)-2):
                    probe = probe.Next
                    tempArray.append(int(probe.data))
                probe.count -= 1 
                count = probe.count
                reverse = probe.reverse

                head = TwoWayNode(data = tempArray[0])
                head.count = count
                head.reverse = reverse
                head.Next = head
                head.prev = head
                probe = head
 
                for i in range(1,len(tempArray)):
                    j = i
                    while j > 0 and probe.Next != head:
                        prev = probe
                        probe = probe.Next
                        probe.count = count
                        probe.reverse = reverse
                        j -= 1 
                    temp = TwoWayNode(data = tempArray[i], prev = probe, Next = probe.Next)
                    probe.Next.prev = temp 
                    probe.Next = temp
        
                while probe.data != head.data:
                    probe = probe.Next

               
                #print(probe.data)
                #print(probe.Next)
                #print(probe.Next.Next.Next)
                #print(probe.Next.Next.Next.Next)
                #print(probe.Next.Next.Next.Next.Next)



                #probe.Next.prev = probe.prev
                #probe.prev.Next = probe.Next
                #probe = probe.prev

                #target = probe.prev
                #probe.Next.prev = probe.prev
                #secondNode = probe.Next
                #Next = probe.Next
                #probe = probe.prev
                #probe.Next = Next
                #for i in range(1, int(probe.count) - 1):
                #    Next = probe
                #    probe = probe.prev
                #temp = TwoWayNode(data = probe.prev, prev = probe.prev.prev, Next = Next) #stopped here
                ##probe.next = temp
                #probe.Next.prev = temp 
                #probe.Next = temp
                #probe.count = probe.count - 1
     
                #temp1 = TwoWayNode(probe.prev.data, probe.Next, probe.prev.prev)
                #temp = TwoWayNode(temp1.data, probe.Next.Next, probe.prev.prev)
                #probe = temp
            else:
                tempArray = []
                prev = str(probe.prev.data)
                Next = str(probe.Next.data)
                count = probe.count
                reverse = probe.reverse
                tempArray.append(int(prev))
                probe = probe.Next
                probe.count = count
                probe.reverse = reverse
                for i in range(0, int(probe.count)-2):
                    probe = probe.Next
                    tempArray.append(int(probe.data))
                tempArray.append(int(Next))
                print("tempArray is: " + str(tempArray))
                probe.count -= 1 


                head = TwoWayNode(data = tempArray[0])
                head.Next = head
                head.prev = head
                probe = head
 
                for i in range(1,len(tempArray)):
                    j = i
                    while j > 0 and probe.Next != head:
                        prev = probe
                        probe = probe.Next
                        j -= 1 
                    temp = TwoWayNode(data = tempArray[i], prev = probe, Next = probe.Next)
                    probe.Next.prev = temp 
                    probe.Next = temp
        
                while probe.data != head.data:
                    probe = probe.Next

               
                #print(probe.data)
                #print(probe.Next)
                #print(probe.Next.Next)
               
        #probe.remove

        print(probe.data)
        print(probe.Next)
        print(probe.Next.Next)
        print(probe.Next.Next.Next)
        print(probe.Next.Next.Next.Next)
        print(probe.Next.Next.Next.Next.Next)

        print("reverse")
        print(probe.data)
        print(str(probe.prev))
        print(probe.prev.prev)
        print(probe.prev.prev.prev) 
        print(probe.prev.prev.prev.prev)

class TwoWayNode(object):
    
    def __init__(self, data, Next = None, prev = None):
        self.data = data
        self.Next = Next
        self.prev = prev
        self.count = 0
        self.reverse = False

    def __repr__(self):
        return repr(int(self.data))

    def count(self):    
        self.count = self.count + 1

    def show(self):
        print(int(self.data))
        print(int(self.Next))
        print(int(self.prev))
        return
    
    def move(self): #move forward #
        if(self.reverse == False):
            for i in range(0,f):
                temp = TwoWayNode(self.Next, self.prev, self)
                self = temp
        else:
            for i in range (0,b):
                temp = TwoWayNode(self.prev, self, self.Next)
                self = temp

    def increment(self):
        num = int(self)
        num = num + 1
        self = TwoWayNode(num, self.Next, self.prev)

    def decrement(self):
        num = int(self)
        num = num - 1
        self = TwoWayNode(num, self.Next, self.prev)

    def copy(self):
        if(self.reverse == False):
            num = int(self)
            self = TwoWayNode(num, num, self.prev)
        else:
            num = int(self)
            self = TwoWayNode(num, self.Next, num)


main()
        
