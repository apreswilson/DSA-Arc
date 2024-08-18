def equillibrium(arr): 
   left = 0
   pivot = 0
   right = sum(arr[1:])

   while pivot < len(arr) - 1 and right != left:
      pivot += 1
      print( pivot)
      right -= arr[pivot]
      print( right)
      left += arr[pivot - 1]
      print( left)
   print(pivot + 1 if left == right else -1)

def main():
   arr = [-7, 1, 5, 2, -4, 3, 0]
   equillibrium(arr)

if __name__ == "__main__":
   main()