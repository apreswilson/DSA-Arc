class Solution:
   def isPalindrome(self, x: int) -> bool:
      y = str(x)[::-1]
      if "-" in y:
         return False
      elif int(y) == x:
         return True
      else:
         return False
def main():
   intInput = -121
   solution_instance = Solution();
   solution_instance.isPalindrome(intInput)

if __name__ == "__main__":
   main()