#In plain english: Start from the bottom of the table, work way up. In other words, if given number 3750: 
# Subtract 1000 (M) until can't anymore
# Subtract 500 (D) until can't anymore
# Subtract 100 (C) until can't anymore

class Solution:
   def intToRoman(self, num: int) -> str:
      table = {
         1: "I",
         4: "IV",
         5: "V",
         9: "IX",
         10: "X",
         40: "XL",
         50: "L",
         90: "XC",
         100: "C",
         400: "CD",
         500: "D",
         900: "CM",
         1000: "M"
      }
      reverseList = reversed(table.keys())
      send_string = ""
      for number in reverseList:
         count = 3
         while num - number >= 0 and count != 0:
            send_string += table.get(number)
            num -= number
            count -= 1
      return send_string
         

def main():
   solution_instance = Solution()
   solution_instance.intToRoman(4000)

if __name__ == "__main__":
   main()