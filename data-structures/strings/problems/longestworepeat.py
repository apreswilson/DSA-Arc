# Iterate through string, increase count by 1 for each unique character. Increase count by 1 until it hits a duplicate value, if duplicate value, reset count to 0, 

# At each iteration we want to store the current length of the item. We then want a counter as well. 

class Solution:
   def lengthOfLongestSubstring(self, s: str) -> int:
      cursubstring = set()
      highest = 0
      count = 0
      count2 = 0
      while count < len(s):
         if s[count] not in cursubstring:
            cursubstring.add(s[count])
            count += 1
            highest = max(highest, count - count2)
         else:
            while s[count2] != s[count]:
               cursubstring.remove(s[count2])
            cursubstring.remove(s[count2])
            count2 += 1
      return highest
def main():
   string = "dvdf"
   new_solution = Solution()
   new_solution.lengthOfLongestSubstring(string)

if __name__ == "__main__":
   main()