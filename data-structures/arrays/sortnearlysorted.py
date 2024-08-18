def sortK(arr, k):
   for index in range(1, len(arr)):
      key = arr[index]
      j = index - 1
      while j >= max(0, index - k) and key < arr[j]:
         arr[j + 1] = arr[j]
         j -= 1
      arr[j + 1] = key

def main():
   array = [6, 5, 3, 2, 8, 10, 9]
   #iter 1[5, 6, 3, 2, 8, 10, 9]
   #iter 2[5, 3, 6, 2, 8, 10, 9]
   #iter 3[6, 3, 5, 2, 8, 10, 9]
   #iter 4[2, 3, 5, 6, 8, 10, 9]
   #iter 5[2, 3, 6, 5, 8, 10, 9]
   #iter 6[2, 5, 6, 3, 8, 10, 9]
   #iter 7[]
   k = 3
   sortK(array, k)
   print(array)

if __name__ == "__main__":
   main()