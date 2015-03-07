######################################## 
#   Blair Kiel
#   Project 3, CS260
#   2/22/2014 
#######################################

from scanner import *
import sys

def main():

    #initilizing project and reading input
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
    
    #initilizing the circular doubly linked list
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

    #shifting list until 0 is at the head
    while probe.data != 1:
        probe = probe.Next
    probe = probe.prev
    probe.prev = temp

    #counting the starting length of the list
    for j in range(0, int(n)+1):
        probe.count += 1

    loopingSequence(n, f, b, s, probe)

def loopingSequence(n, f, b, s, probe):
    n = n
    f = f
    b = b
    s = s
    probe = probe
    sequence = list(s)
    increment = 0

    #this will loop until the list is length 1 
    while(probe.Next != None and probe.prev !=None):
        action = s[increment]
        increment += 1

        #prevents the increment from growling longer than the input sequence
        if (increment == len(s)):
           increment = 0 

        #main logic
        if(action == "t" or action == "T"): #Toggle Direction
            if(probe.reverse == False): 
                probe.reverse = True
            else:
                probe.reverse = False
        elif(action == "m" or action == "M"): #Move | shifts list forward either f times or b times according to direction of list
            reverse = probe.reverse
            if(probe.reverse == False):
                count = probe.count
                for i in range(0, int(f)):
                    probe = probe.Next
                probe.reverse = reverse
                probe.count = count
            else:
                count = probe.count
                for i in range(0, int(b)):
                    probe = probe.prev
                probe.reverse = reverse
                probe.count = count
        elif(action == "i" or action == "I"): #Increment current node value with a modulus calculation to prevent the increment from going out of range ([0,n])
            num = str(probe.data)
            num1 = int(num)
            num2 = (int(num1) + 1) % int(n)
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

        elif(action == "d" or action == "D"): #Decrement current node value with a modulus calculation to prevent the increment from going out of range ([0,n])
            num = str(probe.data)
            num1 = int(num)
            num2 = (num1 - 1) % (int(n))
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

        elif(action == "c" or action == "C"): #copy node value either in front or behind
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

                #next
                probe.Next.prev = probe.prev
                #prev
                probe.prev.Next = probe.Next

                removed = probe.data
                probe = probe.prev
                probe.count = count - 1
                probe.reverse = reverse

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
            
               
class TwoWayNode(object):
    #this is the class that will construct the circular doubly linked list
    
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

main()
        
