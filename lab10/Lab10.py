class AdjListsGraph:

    def __init__(self, n):
        self.size = n
        self.array = [None]*n
        for k in range(n):
            self.array[k] = [ ]

    def insert(self, v, w):
        L = self.array[v]
        if L.count(w) == 1:
            return
        for k in range(len(L)):
            if L[k] > w:
                L.insert(k, w)
                return
        L.append(w)

    def remove(self, v, w):
        L = self.array[v]
        if L.count(w) == 0:
            return
        L.remove(w)

    def display(self):
        #Complete this
        for j in range(len(self.array)):
            string = ""
            for k in range(len(self.array[j])):
                string += str(self.array[j][k]) + ","
            print(str(j) + ": " + string)

        print()
        for i in range(len(self.array)):
            string = ""
            inc2 = 0
            if(self.array[i] == []):
                print(str(i) + ": ")
            else:
                for l in range(0, 9):
                    if(inc2 > len(self.array[len(self.array[i])])):
                        string += str(0)
                    elif(self.array[i][inc2] == l):
                        string += str(1)
                        inc2 += 1
                        inc = self.array[inc2]
                    else:
                        string += str(0)
                print(str(i) + ": " + string)

class AdjMatrixGraph:

    def __init__(self, n):
        self.size = n
        self.array = [None]*n
        for k in range(n):
            self.array[k] = [0]*n

    def insert(self, v, w):
        self.array[v][w] = 1

    def remove(self, v, w):
        self.array[v][w] = 0

    def display(self):
        # Complete this
        for j in range(len(self.array)):
            string = ""
            for k in range(len(self.array[j])):
                if self.array[j][k] == 1:
                    string += str(k) + ","
            print(str(j) + ": " + string)

        print()
        for i in range(len(self.array)):
            string = ""
            for l in range(len(self.array[i])):
                string += str(self.array[i][l])
            print(str(i) + ": " + string)

def main():

    #n = eval(input("Enter number of vertices: "))
    n = input("enter number of vertices: ")
    G1 = AdjListsGraph(n)
    G2 = AdjMatrixGraph(n)
    G1.display()
    print()
    G2.display()
    print()
    for v in range(n):
        for w in range(n):
            if abs(v - w) > n // 4:
                G1.insert(v, w)
                G2.insert(v, w)
    print("After insertion operations:")
    G1.display()
    print()
    G2.display()
    for v in range(n):
        for w in range(n):
            if v % 3 == w % 3:
                G1.remove(v, w)
                G2.remove(v, w)
    print("After remove operations:")
    G1.display()
    print()
    G2.display()

if __name__ == "__main":
    main()

main()
