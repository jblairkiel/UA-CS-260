import sys
from scanner import *

def main():

    input1 = sys.argv[1]
    input2 = sys.argv[2]
    output3 = sys.argv[3]

    array1 = readToCSV(input1)
    array2 = readToCSV(input2)


    isSplit1 = False
    isSplit2 = False
    #for i in range(0, len(array2)):
    for i, e  in reversed(list(enumerate(array2))):
        curArray = array2[i].split(",")
        curCol = curArray[0]
        curDirection = curArray[1]
        curType = curArray[2]

        tempArray = array1
        tempArray1 = array1
        tempArray2 = []
        tempArray3 = []
        tempArray4 = []
        if (isinstance(tempArray[0], str) == True):
            headersArray = tempArray[0].split(",")
        #loops through the length of array1 header

        for j in range(0, len(headersArray)):
            #if found correct header
            array1Header = headersArray[j] 
            if (array1Header == curCol):
                #loop through the length of array1
                sortingArray = []
                #ensure the array is split
                for z in range(1, len(tempArray)):
                    if (isSplit1 == False):   
                        splitTempArray = tempArray[z].split(",")
                        tempArray2.append(splitTempArray)
                    else:
                        tempArray2.append(tempArray[z])
                for k in range(0, len(tempArray2)):
                    sortingRow = tempArray2[k] 
                    if(curType == "int"):
                        tUP = [k, int(sortingRow[j]), k]
                    elif(curType == "float"):
                        tUP = [k, float(sortingRow[j]), k]
                    else:
                        tUP = [k, sortingRow[j], k]
                    sortingArray.append(tUP)
                sortedArray = mergesort(sortingArray, curDirection)

                #create list with new order
                tempArray3.append(headersArray)
                for l in range(1, len(tempArray)):
                    if(isinstance(tempArray[l], str) == True): 
                        tempArray[l] = tempArray[l].split(",")
                for m in range(0, len(sortedArray)):
                    tempNum = int(sortedArray[m][0]) - 1
                    tempArray3.append(tempArray1[tempNum + 2])

                isSplit1 = True
                tempArray = tempArray3
                tempArray1 = tempArray3
                array1 = tempArray3
            
    out = open(output3,"w")
    for y in range(0, len(tempArray3)):
        a = ",".join(tempArray3[y])
        out.write(a + "\n")
    out.close()

def readToCSV(inputFile):

    s = Scanner(inputFile)
    items = []
    token = s.readtoken()
    while (token != ""):
        items.append(token)
        token = s.readtoken()
    s.close()
    return items

#[0, 30, 0]
#[1, 40, 1]

def mergesort(list,direction):
    if len(list) < 2:
        return list
    middle = len(list) // 2
    left = mergesort(list[:middle], direction)
    right = mergesort(list[middle:], direction)
    return merge(left, right, direction)

def merge(left, right, direction):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if(direction == "ascend"):
            if left[i][1] <= right[j][1]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            if left[i][1] >= right[j][1]:
                result.append(left[i])
                i +=1
            else:
                result.append(right[j])
                j += 1
    result += left[i:]
    result += right[j:]
    return result

main()
