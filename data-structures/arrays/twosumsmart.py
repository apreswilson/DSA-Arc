class Solution:
   def twoSum(self, nums: list[int], target: int) -> list[int]:
      table = {}
      for number in range(len(nums)):
         table[nums[number]] = number
      
      for i in range(len(nums)):
         complement = target - nums[i]
         if complement in table:
            return [i, table[complement]]

def main():
   nums = [2,7,11,15]
   target = 9
   soltuion_instance = Solution()
   soltuion_instance.twoSum(nums, target)


if __name__ == "__main__":
   main()