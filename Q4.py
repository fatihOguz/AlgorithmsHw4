 
def insertionSort(arr,count): 

	for i in range(1, len(arr)): 
		key = arr[i] 
		j = i-1
		while j >= 0 and key < arr[j] : 
				arr[j + 1] = arr[j] 
				j -= 1
				count=count+1
		arr[j + 1] = key 
	return count	

def partition(arr,low,high,count): 
	i = ( low-1 )		 
	pivot = arr[high]	 

	for j in range(low , high): 

		if arr[j] < pivot: 
		
			
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 
			count[0]=count[0]+1
			

	count[0]=count[0]+1
	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

def quickSort(arr,low,high,count): 
	if low < high: 
		pi = partition(arr,low,high,count) 
		quickSort(arr, low, pi-1,count) 
		quickSort(arr, pi+1, high,count) 



####################################################################################
b= [1,2,3,4,5,6,7,8,9,10]
n = len(b) 
count = [0]
print(b)
quickSort(b,0,n-1,count) 
print("quick sort : number of swap count " + str (count))
print(b)
print()





b= [1,2,3,4,5,6,7,8,9,10]
print(b)
print("insertion sort : number of swap " + str (insertionSort(b,0)))
print(b)
print()



print("######################################################################################")
w=[10,9,8,7,6,5,4,3,2,1]
count = [0]
n = len(w) 
print(w)
quickSort(w,0,n-1,count) 
print("quick sort : number of swap count " + str (count))
print(w)
print()


w=[10,9,8,7,6,5,4,3,2,1]
print(w)
print("insertion sort : number of swap " + str (insertionSort(w,0)))
print(w)
print()


print("##########################################################################################")







arr = [3, 7, 6, 9, 1, 8, 10, 4, 2, 5]
count = [0]
n = len(arr) 
print("size " + str(n))
print(arr)
quickSort(arr,0,n-1,count) 
print("quick sort : number of swap count " + str (count))
print(arr)
print()


arr = [3, 7, 6, 9, 1, 8, 10, 4, 2, 5]
print(arr)
print("insertion sort : number of swap " + str (insertionSort(arr,0)))
print(arr)
print()


print("##########################################################################################")

a=[1,2,3,8,4,5,13,55,6,7,8,0,89]
count = [0]
n = len(a) 
print("size " + str(n))
print(a)
quickSort(a,0,n-1,count) 
print("quick sort : number of swap count " + str (count))
print(a)
print()






a=[1,2,3,8,4,5,13,55,6,7,8,0,89]
print(a)
print("insertion sort : number of swap " + str (insertionSort(a,0)))
print(a)
print()

print("##########################################################################################")

average1=[5,7,0,9,3,64,989,13,46,15,9,13]

count = [0]
n = len(average1) 
print("size " + str(n))
print(average1)
quickSort(average1,0,n-1,count) 
print("quick sort number of swap count " + str (count))
print(average1)
print()
average1=[5,7,0,9,3,64,989,13,46,15,9,13]
print(average1)
print("insertion sort number of swap " + str (insertionSort(average1,0)))
print(average1)
print()


print("##########################################################################################")

average2=[11,98,655,19,73,49,64,17,19,13,14,16,468,12,17,46,12,8,75,23,16,9,78,123,4,46]

count = [0]
n = len(average2) 
print("size " + str(n))
print(average2)
quickSort(average2,0,n-1,count) 
print("quick sort : number of swap count " + str (count))
print(average2)
print()
average2=[11,98,655,19,73,49,64,17,19,13,14,16,468,12,17,46,12,8,75,23,16,9,78,123,4,46]

print(average2)
print("insertion sort : number of swap " + str (insertionSort(average2,0)))
print(average2)
print()

print("##########################################################################################")

average3=[45,1,147,5,49,78,16,45,79,15,
79,4,578,19,28,79,5,789,6,79,133,13,15,
23,11,98,655,19,73,49,64,17,19,13,14,16,
468,12,17,46,12,8,75,23,16,9,78,123,4,46,
79,75,18,46,8,24,6,789,47,15,70,20,5,0]




count = [0]
n = len(average3) 
print("size " + str(n))
print(average3)
quickSort(average3,0,n-1,count) 
print("quick sort : number of swap count " + str (count))
print(average3)
print()

average3=[45,1,147,5,49,78,16,45,79,15,
79,4,578,19,28,79,5,789,6,79,133,13,15,
23,11,98,655,19,73,49,64,17,19,13,14,16,
468,12,17,46,12,8,75,23,16,9,78,123,4,46,
79,75,18,46,8,24,6,789,47,15,70,20,5,0]




print(average3)
print("insertion sort : number of swap " + str (insertionSort(average3,0)))
print(average3)
print()

#################################################################################################

