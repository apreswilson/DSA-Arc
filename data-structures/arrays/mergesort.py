def merge(left, right):
   print("Merging Now")
   result = []
   while left and right:
      if left[0] <= right[0]:
         print(f"Appended left {left[0]}")
         result.append(left[0])
         left = left[1:]
         print(f"In Left {left}")
      else:
         print(f"Appended right {right[0]}")
         result.append(right[0])
         right = right[1:]
         print(f"In Right {right}")
   while left:
      print(f"Append Remaining left {left[0]}")
      result.append(left[0])
      left = left[1:]
      print(f"Remaining Left {left}")
   while right:
      print(f"Append Remaining right {right[0]}")
      result.append(right[0])
      right = right[1:]
      print(f"Remaining Right: {right}")
   print(f"Result: {result}")
   return result

def mergeSort(arr):
   if len(arr) <= 1:
      return arr
   mid = len(arr) // 2
   left = arr[:mid]
   print(left)
   right = arr[mid:]
   print(right)
   left = mergeSort(left)
   right = mergeSort(right)
   return merge(left, right)


def main():
   arrayToSort = [1, 6, 7, 3, 8, 5, 10]
   sortedArray = mergeSort(arrayToSort)
   print(sortedArray)

if __name__ == "__main__":
   main()