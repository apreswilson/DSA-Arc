# go through each word in the array, append any non-unique characters to the string. If 

class Solution:
   def longestCommonPrefix(self, strs: list[str]) -> str:
      sendString = ""
      strs=sorted(strs)
      first = strs[0]
      last = strs[-1]
      for i in range(min(len(first),len(last))):
         if first[i] != last[i]:
            return sendString
         sendString += first[i]

def main():
   string = ["flower", "flow", "flight"]
   new_instance = Solution()
   new_instance.longestCommonPrefix(string)

main()