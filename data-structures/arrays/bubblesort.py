def bubbleSortArray(arr):
   n = len(arr)
   for i in range(n):
      swapped = False
      for j in range(0, n - i - 1):
         if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
      if (swapped == False):
         break

def main():
   arrayToSort = [5, 1, 7, 3, 8, 10]
   bubbleSortArray(arrayToSort)
   print(arrayToSort)

if __name__ == "__main__":
   main()