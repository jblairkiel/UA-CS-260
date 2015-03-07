from scanner import *
import sys

def main():

    inputFile = sys.argv[1]
    s = Scanner(inputFile)
    inArr = []
    record = s.readtoken()
    while (record != ""):
        inArr.append(int(record))
        record = s.readtoken()
    s.close()

    print("The length of the array is: " + str(len(inArr)))
    quicksort(inArr)

def quicksort(lyst):
    global swaps
    swaps = 0
    print("The list unsorted is: " + str(lyst))
    print()
    quicksortHelper(lyst, 0, len(lyst) - 1)
    print("The reordered list is: " + str(lyst))
    print("The number of swaps made was: " + str(swaps))
    
def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation - 1)
        quicksortHelper(lyst, pivotLocation + 1, right)

def partition(lyst, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
            # Exchange the pivot item and the boundary item
    swap (lyst, right, boundary)
    return boundary

def swap(lyst, i, j):
    """Exchanges the items at positions i and j."""
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    global swaps
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
    swaps = swaps + 1

main()
