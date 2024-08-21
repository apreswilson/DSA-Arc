class Solution:
   def twoSum(self, nums: list[int], target: int) -> list[int]:
      for i in range(len(nums)):
         for j in range (i + 1, len(nums)):
            if nums[i] + nums[j] == target:
               return[i, j]
def main():
   nums = [3,3]
   target = 6
   soltuion_instance = Solution()
   soltuion_instance.twoSum(nums, target)


if __name__ == "__main__":
   main()