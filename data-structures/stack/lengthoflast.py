class Solution:
   def lengthOfLastWord(self, s: str) -> int:
      formatted = s.strip().split(" ")
      return len(formatted[len(formatted) - 1])


def main():
   string = "hello world "
   soltuioninstance = Solution()
   soltuioninstance.lengthOfLastWord(string)

if __name__ == "__main__":
   main()