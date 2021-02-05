def myDecreaseAndConquerFunc (arr):
    print(arr)
    if(len(arr)==1):
        print("different " + str(arr))
        return 0
    median=len(arr)//3
    print(len(arr))
    print(median)
    median=int(median)
    print("median " + str(median))
    l=arr[:median]
    m=arr[median:2*median]
    r=arr[2*median:len(arr)]
    left=right=med=0
    print(l)
    print(m)
    print(r) 
    if len(l) != 0:
        left=sum(l)/len(l)
    if len(m) != 0:
        med=sum(m)/len(m)
    if len(r) != 0:
        right=sum(r)/len(r)
  

    if(left==right):
        myDecreaseAndConquerFunc(m)
    elif(left==med):
        myDecreaseAndConquerFunc(r)
    else:
        myDecreaseAndConquerFunc(l)

arr = [ 2, 2,  -1,2,2, 2 ,2,2,2,2]
flag=[-1]
myDecreaseAndConquerFunc(arr)
