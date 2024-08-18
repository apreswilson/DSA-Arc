def majorityElement(arr):
   storageDict = {}
   i = 0;
   while i < len(arr):
      if arr[i] not in storageDict:
         storageDict.update({arr[i]: 1})
      else:
         x = storageDict.get(arr[i])
         storageDict.update({arr[i]: x + 1})
      i+= 1
   print(storageDict)

def main():
   arr = [3, 9, 2, 9, 2, 9, 9]
   majorityElement(arr)

if __name__ == "__main__":
   main()