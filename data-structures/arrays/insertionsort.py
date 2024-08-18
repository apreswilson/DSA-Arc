def insertionSort(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      j = i - 1

      while j >= 0 and key < arr[j]:
         arr[j + 1] = arr[j]
         j -= 1
      arr[j + 1] = key

def main():
   arrayToSort = [1, 6, 7, 3, 8, 5, 10]
   insertionSort(arrayToSort)
   print(arrayToSort)

if __name__ == "__main__":
   main()