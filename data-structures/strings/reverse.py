from typing import List


class Solution:
   def reverseString(self, s: List[str]) -> None:
      #More complex solution

      # left, right = 0, len(s) - 1
      # while left < right:
      #    s[left], s[right] = s[right], s[left]
      #    left += 1
      #    right -= 1

      #Easier solution
      s[:] = s[::-1]


def main():
   word = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
   instance = Solution()
   instance.reverseString(word)
   print(word)

if __name__ == "__main__":
   main()