class Solution:
   def countSegments(self, s: str) -> int:
      split = s.split()
      num = 0
      for word in split:
         if word != " ":
            num += 1
      print(num)


def main():
   string = "Hello,%!#@! my name is John"
   instance = Solution()
   instance.countSegments(string)

if __name__ == "__main__":
   main()     