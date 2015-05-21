
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
        print ("InOrder:    ", end="")
        queue = Queue()
        def recurse (p):
            # Complete this method.
            if self.left:
                for i in inOrder(self.left):
                    print(i.data)
                    queue.enqueue(i.data)
            queue.enqueue(self.data)
            if searchT.right:
                for i in inOrder(self.right):
                    print(i.data)
                    queue.enqueue(i.data)
        recurse (self.root)

    def preOrder (self):
        print ("PreOrder:   ", end="")
        def recurse (p):
            print( )
            # Complete this method.
        recurse (self.root)
        print( )

    def postOrder (self):
        print ("PostOrder:  ", end="")
        def recurse (p):
            print( )
            # Complete this method.
        recurse (self.root)
        print( )

    def levelOrder (self):
        print ("LevelOrder: ", end="")
        Q = Queue( )
        if self.root!=None:
            Q.enqueue (self.root)
        # Complete this method.
        print( )

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

