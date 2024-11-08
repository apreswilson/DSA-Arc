class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
      j = 0
      i = 0
      combined = []
      while i < len(nums1) and j < len(nums2):
         if nums1[i] < nums2[j]:
               combined.append(nums1[i])
               i += 1
         else:
               combined.append(nums2[j])
               j += 1
      combined += nums1[i:]
      combined += nums2[j:]
      
      if len(combined) % 2 != 0:
         mid = (0 + len(combined)) // 2
         return combined[mid]
      else:
         mid = (0 + len(combined) - 1) // 2
         median = (combined[mid] + combined[mid + 1]) / 2
         return median
      
def main():
   digits = [1,3]
   digits2 = [2]
   instanceofthing = Solution()
   print(instanceofthing.findMedianSortedArrays(digits, digits2)) 

if __name__ == "__main__":
   main()