#About
def binarygap(num):
    binaryForm="{0:b}".format(num)
    indices = [i for i, x in enumerate(binaryForm) if x == "1"]
    if(len(indices)<=1):
        return 0
    else:
        currentLargestGap=0
        largestGap=0
        for index, obj in enumerate(indices):
            try:
                largestGap=indices[index+1]-obj
                if(largestGap>currentLargestGap):
                    currentLargestGap=largestGap
            except IndexError:
                pass
        return currentLargestGap-1

print(binarygap(9)) #2
print(binarygap(529)) #4
print(binarygap(20))
print(binarygap(32)) 
print(binarygap(1041))
print(binarygap(15))