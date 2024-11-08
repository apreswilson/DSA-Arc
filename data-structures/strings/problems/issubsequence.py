class Solution:
   def isSubsequence(self, s: str, t: str) -> bool:
      if len(s) == 0:
         return True
      clone = list(s)
      print(clone)
      for i in range(len(t)):
         if len(clone) > 0:
            if t[i] == clone[0]:
               clone.pop(0)
      return True if len(clone) == 0 else False 

def main():
   str1 = "b"
   str2 = "abc"
   instance = Solution()
   print(instance.isSubsequence(str1, str2))

if __name__ == "__main__":
   main()