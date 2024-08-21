def prefixSum(array):
   prefixSum = []
   accumulateValue = 0
   for index in range(len(array)):
      accumulateValue += array[index]
      prefixSum.append(accumulateValue)
   return prefixSum

def sumOfPrefix(prefixArr, queries):
   for i in range(len(queries)):
      left = queries[i][0]
      right = queries[i][1]
      if left > 1:
         print(prefixArr[right] - prefixArr[left - 1])
      else:
         print(prefixArr[right])

def main():
   normalArray = [3, 6, 2, 8, 9, 2]
   prefixArray = prefixSum(normalArray)
   print(prefixArray)

   queries = [[2, 3], [4, 5], [1, 5], [3, 5]]
   sumOfPrefix(prefixArray, queries)

if __name__ == "__main__":
   main()