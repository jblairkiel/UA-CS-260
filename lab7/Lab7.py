###############################
# Blair Kiel
# Lab 7 3/25/2015
##############################

class QNode:
    def __init__ (self, x, p=None):
        self.data = x
        self.next = p

class Queue:
    def __init__ (self):
        self.front = None
        self.back = None

    def isEmpty(self):
        return self.front == None

    def enqueue (self, x):
        p = QNode (x)
        if self.isEmpty( ):
            self.front = p
        else:
            self.back.next = p
        self.back = p

    def dequeue (self):
        if self.isEmpty( ):
            raise KeyError ("Queue is empty.")
        x = self.front.data
        self.front = self.front.next
        if self.front == None:
            self.back == None
        return x

class BSTNode:
    def __init__ (self, x, L=None, R=None):
        self.data = x
        self.left = L
        self.right = R

    
class BST:
    def __init__ (self):
        self.root = None

    def insert (self, x):
        def recurse (p):
            if x<p.data:
                if p.left==None:
                    p.left = BSTNode (x)
                else:
                    recurse (p.left)
            else:
                if p.right==None:
                    p.right = BSTNode (x)
                else:
                    recurse (p.right)
        # body of insert method
        if self.root==None:
            self.root = BSTNode(x)
        else:
            recurse (self.root)

    def inOrder (self):
        #complete this method
        print("InOrder:    ", end="")
        def recurse (node):
            if node != None:
                recurse(node.left)
                print(node.data, end="  ")
                recurse(node.right)
        recurse(self.root)
        print( )

    def preOrder (self):
        # Complete this method.
        print ("PreOrder:   ", end="")
        def recurse (node):
            if node != None:
                #print data go left then right then to next
                print(node.data, end="  ")
                recurse(node.left)
                recurse(node.right)
        recurse (self.root)
        print( )

    def postOrder (self):
        print ("PostOrder:  ", end="")
        def recurse (node):
            if node != None:
                #go left go right then print data go to nex
                recurse(node.left)
                recurse(node.right)
                print(node.data, end="  ")
            # Complete this method.
        recurse (self.root)
        print( )

    def levelOrder (self):
        print ("LevelOrder: ", end="")
        Q = Queue( )
        Q.enqueue(self.root)
        while Q != None:
        #while the is a queue
            try:
                node=Q.dequeue()
            except:
                break
            # printing "inline" left to right then go up
            print(node.data, end= "  ")
            if(node.left != None):
                Q.enqueue(node.left)
            if(node.right != None):
                Q.enqueue(node.right) 
        print( )

        # Complete this method.


def main( ):
    T = BST( )
    L = eval (input ("Enter a Python list: "))
    for x in L:
        T.insert (x)
    T.inOrder( )
    T.preOrder( )
    T.postOrder( )
    T.levelOrder( )

if __name__ == '__main__':
    main( )

