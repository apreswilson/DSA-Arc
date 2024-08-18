def quick_sort(arr, low, high):
   if low < high:
      p = partition(arr, low, high)
      print("quicksort high is p - 1")
      quick_sort(arr, low, p - 1)
      print("quicksort low is p + 1")
      quick_sort(arr, p + 1, high)

def partition(arr, low, high):   
   pivot = arr[high]
   print(f"pivot {pivot}")
   i = low
   for j in range(low, high):
      if arr[j] <= pivot:
         print(f"{arr[i]} swapping with {arr[j]}")
         arr[i], arr[j] = arr[j], arr[i]
         i += 1
   print(f"swapping {arr[i]} with {arr[high]}")
   arr[i], arr[high] = arr[high], arr[i]
   return i

def main():
   arrayToSort = [1, 6, 3, 87, 4, 8, 10, 13]
   # pivot 13[1, 6, 3, 4, 8, 10, 13, 87]
   # pivot 10, and 8 all numbers left of them are less than them
   # pivot 4 [1, 3, 4, 6, 8, 10, 13, 87]
   #after pivot 4 it is in ascending order.
   quick_sort(arrayToSort, 0, len(arrayToSort) - 1)
   print(arrayToSort)  
if __name__ == "__main__":
    main()