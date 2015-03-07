##################
# Lab 6
# Blair Kiel
# 3/4/15
#################

class Deck:
    def __init__(self, cap):
        self.cap = cap
        self.array = [0]*cap
        self.front = 0
        self.back = cap-1
        self.n = 0
    def pushBack(self,x):
        if self.isFull(): return
        self.back = (self.back+1) % self.cap
        self.array[self.back] = x
        self.n += 1 
    def pushFront(self, x):
        # Modify this method.
        if self.isFull(): return
        self.front = (self.front-1) % self.cap
        self.array[self.front] = x
        self.n += 1
    def popFront(self):
        if self.isEmpty(): return None
        x = self.array[self.front]
        self.front = (self.front+1) % self.cap
        self.n -= 1
        return x
    def popBack(self):
        # Modify this method.
        if self.isEmpty(): return None
        x = self.array[self.back]
        self.back = (self.back-1) % self.cap   
        self.n -= 1
        return x
    def isEmpty(self):
        return self.n==0
    def isFull(self):   
        return self.n==self.cap

def main( ):
    cap = eval(input("Enter maximum capacity of deck: "))
    deck = Deck(cap)
    x=1
    while not deck.isFull( ):
        if x%5==3 or x%5==4:
            print(deck.popFront( ))
        else:
            deck.pushBack(x)
        x += 1
    x=1
    while not deck.isEmpty( ):
        if x%5==3 or x%5==4:
            deck.pushFront(x)
        else:
            print(deck.popBack( ))
        x += 1

if __name__ == '__main__':
    main( )

