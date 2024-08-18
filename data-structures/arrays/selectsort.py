def selectionSortArray(array):
   for i in range(len(array) - 1):
      minimum_index = i
      for j in range(i + 1, len(array)):
         if array[minimum_index] > array[j]:
            minimum_index = j
      array[i], array[minimum_index] = array[minimum_index], array[i]

def main():
   arrayToSort = [64, 25, 12, 22, 11]
   selectionSortArray(arrayToSort)
   print(arrayToSort)

if __name__ == "__main__":
   main()