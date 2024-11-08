class Solution:
   def plusOne(self, digits: list[int]) -> list[int]:
      for i in range(len(digits) - 1, -1, -1):
         if digits[i] + 1 != 10:
            digits[i] += 1
            return digits
         digits[i] = 0
         if i == 0:
            return [1] + digits

def main():
   digits = [9, 9]
   solution_instance = Solution()
   solution_instance.plusOne(digits)

if __name__ == "__main__":
   main()