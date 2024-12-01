from typing import List

class Solution:
   def searchRange(self, nums: List[int], target: int) -> List[int]:
      if target not in nums: 
         return [-1, -1]
      start = end = 0
      flag = False
      for i in range(len(nums)):
         if nums[i] == target and not flag:
            start = end = i
            flag = True
         elif nums[i] == target and flag:
            end += 1
         else: 
            flag = False
      return [start, end] 

            
def main():
   nums = [5, 7, 7, 8, 8, 10]
   target = 8
   solution_instance = Solution()
   solution_instance.searchRange(nums, target)

if __name__ == "__main__":
   main()
        