def countLeaders(arr):
   maxFromRight = arr[len(arr) - 1]
   i = len(arr) - 2
   outcome = [arr[len(arr) - 1]]
   while i >= 0:
      if maxFromRight < arr[i]:
         maxFromRight = arr[i]
         outcome.append(arr[i]) 
      i -= 1
   print(outcome)

def main():
   array = [16, 17, 4, 3, 5, 2]
   countLeaders(array)

if __name__ == "__main__":
   main()