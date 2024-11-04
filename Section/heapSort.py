# Python program for implementation of heap Sort

def heapify(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1 # left = 2*i + 1
	r = 2 * i + 2 # right = 2*i + 2
 
# See if left child of root exists and is greater than root
	if l < n and arr[i] < arr[l]:
		largest = l

# See if right child of root exists and is greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r

# Change root, if isn't a largest 
	if largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i]) # swap

# Heapify the root.
		heapify(arr, n, largest)


# The main function to sort an array of given size

def heapSort(arr):
	n = len(arr)

# Build a maxheap.
# Since last parent will be at (n//2) we can start at that location.
	for i in range(n // 2, -1, -1):     # => stop if we didn't have left and right child (-1 , -1)
		heapify(arr, n, i)

# One by one extract elements
	for i in range(n - 1, 0, -1): # we stoped in index 0 because when we reach to index 0 all items will be sorted 
		(arr[i], arr[0]) = (arr[0], arr[i]) # swap
		heapify(arr, i, 0)


#  test code

arr = [12, 11, 13, 5, 6, 20 , 7 ]
heapSort(arr)
n = len(arr)
print('Sorted array is : ')
for i in range(n):
	print(arr[i])
