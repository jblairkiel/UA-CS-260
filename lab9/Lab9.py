######################################
# Blair Kiel    
# Lab 7.py
#
#####################################
class BSTNode:
    def __init__(self, x, L=None, R=None):
        self.data = x
        self.left = L
        self.right = R
		
class BST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        def recurse(p):
            if(x<p.data):
                if(p.left==None):
                    p.left = BSTNode(x)
                else:
                    recurse(p.left)
            else:
                if(p.right==None):
                    p.right = BSTNode(x)
                else:
                    recurse(p.right)
        if(self.root==None):
            self.root = BSTNode(x)
        else:
            recurse(self.root)

    def find(self, x):
        def recurse(p):
            if(p==None):
                return False
            elif(x<p.data):
                return recurse(p.left)
            elif(x>p.data):
                return recurse(p.right)
            else:
                return True
        return recurse(self.root)

    def display(self):
        def recurse(p, rightChild=False):
            if(p==None):return
            if(rightChild):print(" ", end="")
            print("(", end="")
            recurse(p.left)
            print(p.data, end="")
            recurse(p.right, True)
            print(")", end="")
            if(not rightChild): print(" ", end="")
        recurse(self.root)
        print( )

    def remove(self, x):
        def recurse(p):
            if (p==None):return p
            elif (x<p.data):return recurse(p.left)
            elif (x>p.data):return recurse(p.right)
            elif (p.left==None and p.right==None):
                #case1
                return p
                #temp = p
                #return temp
            elif (p.right==None):#
                #case2
                p = p.left
                return p
                #p = p.left
                #return p
                #return recurse(p.left)
            elif(p.left==None):
                #case3
                p = p.right
                return p
                #return recurse(p.right)
            else:
                #case4 there are two childs
                #locate p's sucessor node q (so q is the node that follows p in an in-order traversal
                #swap the data in nodes p and q

                temp = p.data
                
                if(p.data < p.right.data):
                    p.data = p.right.data
                    p.right.data = temp
                    recurse(p.right) 
                else:
                    p.data = p.left.data
                    p.left.data = temp
                    recurse(p.left)
                #recursively remove x from p's right subtree (this removes node q using case 1, 2, or 3)
                #self.remove(p.left.data)
                #not sure if this description works
                return p
        self.root = recurse(self.root)

def main( ):
    T = BST( )
    L = eval(input("Enter a Python list: "))
    for x in L:
        print("Insert " + str(x) + ": ", end="")
        T.insert(x)
        T.display( )
    for x in L:
        print("Removing " + str(x) + ": ", end="")
        T.remove(x)
        T.display( ) 

if __name__ == "__main__":
    main( )
