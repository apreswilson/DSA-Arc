class Solution:
   def summaryRanges(self, nums: list[int]) -> list[str]:
      if nums == []:
         return []
      output = []
      i = 0
      while i < len(nums):
         start = nums[i]
         while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
            i += 1
         if start == nums[i]:
            output.append(f"{start}")
         else:
            output.append(f"{start}->{nums[i]}")
         i += 1
      return output

def main():
   nums = [0, 1, 2, 4, 5, 7]
   instance = Solution()
   instance.summaryRanges(nums)

if __name__ == "__main__":
   main()