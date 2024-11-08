class Solution:
   def maxProfit(self, prices: list[int]) -> int:
      profit = 0
      temp = prices[0]
      for p in prices[1:]:
         if temp > p:
            temp = p
         profit = max(profit, p - temp)
      print(profit)

def main():
   prices = [7, 1, 5, 3, 6, 4]
   instance = Solution()
   instance.maxProfit(prices)

if __name__ == "__main__":
   main()