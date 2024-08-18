def majorityElement(arr, element):
   i = 0
   count = 0
   while i < len(arr):
      if arr[i] == element:
         count += 1
      i += 1
   
   if count > (len(arr) // 2):
      print("True, x appears more than n/2 times")
   else:
      print("False, x does not appear more than n/2 times") 


def main():
   arrayToSearch = [1, 1, 2, 4, 4, 4, 6, 6]
   majorityNumber = 4
   majorityElement(arrayToSearch, majorityNumber)

if __name__ == "__main__":
   main()