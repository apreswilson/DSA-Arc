class Solution:
   def isPalindrome(self, s: str) -> bool:
      product = ""
      for letter in s:
         if letter.isalnum():
            product += letter
      print(product[::-1].lower())
      print(True if product.lower() == product[::-1].lower() else False)

def main():
   string = "0P"
   solutioninstance = Solution()
   solutioninstance.isPalindrome(string)

if __name__ == "__main__":
   main()     