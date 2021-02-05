
Max = -99999
Min = 99999
 
def getMax_Min(arr,left,right):
    global Max,Min
    left = int(left)
    right = int(right)
    if right - left <=1:
        if(arr[left] < arr[right]):
            if Max < arr[right]:
                Max = arr[right]
            if Min > arr[left]:
                Min = arr[left]
        else:
            if Max < arr[left]:
                Max = arr[left]
            if Min > arr[right]:
                Min = arr[right]
    else:
        mid  = (right - left)/2 + left
        getMax_Min(arr,left,mid)
        getMax_Min(arr,mid,right)

def fixedArr(arr,left,right):

	getMax_Min(arr,left,right)
	print(Min)
	arr.remove(Min)
	print(arr)
	return Min
def findXthElemenet(arr,a,b,x,count):
	global Min
	if(count>x):
		return arr[x]
	Min = 99999
	aMinVal=fixedArr(a,0,len(a)-1)
	Min = 99999
	bMinVal=fixedArr(b,0,len(b)-1)
	
	arr.append(bMinVal)
	arr.append(aMinVal)
	count=count+2
	
	print(arr)
	findXthElemenet(arr,a,b,x,count)

def X(arr,a,b,x):
	global Max
	findXthElemenet(arr,a,b,x,0)

	
	print("arr " + str(arr))
	Max = -99999
	getMax_Min(arr,0,len(arr)-1)
	print(Max)

a=[ 21, 11, 7,  9, 2, 1 ,7 ,6,4]
b=[ 22, 23, 12, 3,29, 2, 1 ,6,5]
arr=[]
x=17

X(arr,a,b,x)

