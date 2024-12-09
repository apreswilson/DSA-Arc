from typing import Optional

class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
   def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
      dummy = ListNode(0)
      dummy.next = head
      current = dummy
      while current.next:
         if current.next.val == val:
            current.next = current.next.next
         else:
            current = current.next
      return dummy.next

def printlist(head):
   current = head
   while current:
      print(current.val)
      current = current.next
   
   
def main():
   head = ListNode(1)
   head.next = ListNode(2)
   head.next.next = ListNode(6)
   head.next.next.next = ListNode(3)
   head.next.next.next.next = ListNode(4)
   head.next.next.next.next.next = ListNode(5)
   head.next.next.next.next.next.next = ListNode(6)
   instance = Solution()
   modified = instance.removeElements(head, 6)
   printlist(modified)
if __name__ == "__main__":
   main()