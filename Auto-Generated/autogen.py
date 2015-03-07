import random

def main():

    print("What type of data do you want to generate?")
    print("1: Array")
    inPrompt = input()

    if(inPrompt == "1"):

        print("Upper Bound?:")
        uBound = int(input())
        print("Lower Bound?:")
        lBound = int(input())
        print("Length of Array?:")
        length = int(input())
        randArray(lBound, uBound, length)

    else:

        return

def randArray(lBound, uBound, length):

    arr = []
    for i in range(0, length):
        rand = random.randint(lBound, uBound)
        arr.append(rand)

    print(arr)
main()
