import random

stack = [ ]

def quicksort(left, right):
    if (left<right):
        position = random.randint(left, right)
        tup = (left,position-1)
        stack.append(tup)
        print(stack)
        quicksort(left, position-1)
        print(stack)
        quicksort(position+1, right)
        stack.pop()
        print(stack)

def main( ):
	n = eval(input("Enter length of list: "))
	print("Tracing stack of recursive calls for Quicksort:")
	quicksort(0, n-1)

if __name__ == '__main__':
	main( )

