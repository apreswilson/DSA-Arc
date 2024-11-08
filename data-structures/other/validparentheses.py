#loop through input, step by 2 characters because we're only comparing pairs. At each iteration, compare if the current value to the value from table of the value 1 index ahead.

#THIS WAS BAD
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
         j = 0
         matchingString = ""
         for i in range(len(haystack)):
            print(haystack[i])

         return -1
    
def main():
   haystack = "mississippi"
   needle = "issip"
   solution_instance = Solution()
   print(solution_instance.strStr(haystack, needle))

if __name__ == "__main__":
   main()