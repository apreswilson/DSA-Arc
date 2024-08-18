def countSwaps(arr):
   count = 0
   num_unplaced_zero = 0;
   for i in range(len(arr) - 1, -1, -1):
      if arr[i] == 0:
         num_unplaced_zero += 1
      else:
         count += num_unplaced_zero
   print(count)
def main():
  array= [0, 0, 1, 0, 1, 0, 1, 1]
  countSwaps(array)

if __name__ == "__main__":
   main()