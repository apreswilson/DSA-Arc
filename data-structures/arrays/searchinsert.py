class Solution:
   def searchInsert(self, nums: list[int], target: int) -> int:
      if nums[len(nums) - 1] < target:
         nums.append(target)
      elif nums[0] > target:
         return 0

      for i in range(len(nums)):
         if target == nums[i]:
            return i
         elif target < nums[i]:
            return i

def main():
   nums = [1, 3, 5]
   target = 4
   instance = Solution()
   print(instance.searchInsert(nums, target))


if __name__ == "__main__":
   main()