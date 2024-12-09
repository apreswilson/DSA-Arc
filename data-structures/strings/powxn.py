class Solution:
   def myPow(self, x: float, n: int) -> float:
      return x ** n
def main():
   num1 = 0
   num2 = 3
   instance = Solution()
   print(instance.myPow(num1, num2))

if __name__ == "__main__":
   main()