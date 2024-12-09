#Splitting function
def mergeSort(arr):
	#Exit condition where the array is only 1 element
	if len(arr) <= 1:
		return arr
		
	#Define our mid point to split array in half
	mid = len(arr) // 2
	
	#Initialize first half and second half to variables
	leftHalf = arr[:mid]
	rightHalf = arr[mid:]

	#Initialize two variables that recursively split each half
	sortedLeft = mergeSort(leftHalf)
	sortedRight = mergeSort(rightHalf)

	#Return the merged array back up the call chain
	return merge(sortedLeft, sortedRight)

#Merging function
def merge(left, right):
	#Initialize an empty return array
	result = []

	#Initialize two pointers to zero
	i = j = 0

	#Iterate while i < length of left array and j < length of right
	while i < len(left) and j < len(right):
		#If left number at index i is less than right number at index j
		if left[i] < right[j]:
			#Append lesser number to the return array
			result.append(left[i])
			#Increment i by 1
			i += 1
		else:
		#Otherwise append the right number to the return array
			result.append(right[j])
			#Increment j by 1
			j += 1
	#Append any remaining values to return array
	result.extend(left[i:])
	result.extend(right[j:])
	
	#Return resulting array
	return result

def main():
	unsortedArr = [3, 7, 6, -10]
	sortedArr = mergeSort(unsortedArr)
	print(sortedArr)

if __name__ == "__main__":
	main()