class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
   def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      first = 0
      second = 0
      digit = 1
      seconddigit = 1
      while l1 is not None:
         first += l1.val * digit
         digit *= 10
         l1 = l1.next
      while l2 is not None:
         second += l2.val * seconddigit
         seconddigit *= 10
         l2 = l2.next
      returnlist = [int(digit) for digit in str(first + second)]
      dummy = ListNode(0)
      current = dummy
      for i in range(len(returnlist)):
         current.next = ListNode(returnlist.pop())
         current = current.next
      return dummy.next

      

def listToLinedList(arr):
   dummy = ListNode(0)
   current = dummy
   for number in arr:
      current.next = ListNode(number)
      current = current.next
   return dummy.next

def main():
   l1 = listToLinedList([2, 4, 3]) 
   l2 = listToLinedList([5, 6, 4]) 
   instance = Solution()
   instance.addTwoNumbers(l1, l2)
if __name__ == "__main__":
    main()