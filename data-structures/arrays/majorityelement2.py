class Solution:
   def majorityElement(self, nums: list[int]) -> int:
      table = {}
      for i in range(len(nums)):
         if nums[i] not in table:
            table.update({nums[i]: 1})
         else:
            x = table.get(nums[i])
            table.update({nums[i]: x + 1})
      maxnum = max(table.values())
      print(maxnum)
      for i in table.keys():
         if table.get(i) == maxnum:
            print(i) 

def main():
   nums = [2,2,1,1,1,2,2]
   instance = Solution()
   instance.majorityElement(nums)

if __name__ == "__main__":
   main()
