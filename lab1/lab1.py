from sys import stdin
def main():

    inLine1 = stdin.readline()
    arrLine1 = inLine1.split(" ")
    if(len(arrLine1) <= 1):
        inLine2 = stdin.readline()
        num1 = inLine1
        num2 = inLine2
    else:
        num1 = arrLine1[0]
        num2 = arrLine1[1] 

    nSum = addNums(num1, num2)
    nProduct = productNums(num1, num2)
    print("sum = " + str(nSum)) 
    print("product = " + str(nProduct))

def addNums(num1, num2):

    numSum = int(num1) + int(num2)
    return numSum

def productNums(num1, num2):

    numProduct = int(num1) * int(num2)
    return numProduct
    
main()

