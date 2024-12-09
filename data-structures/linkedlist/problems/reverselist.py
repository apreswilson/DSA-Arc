class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
   def reverseList(self, head: ListNode) -> ListNode:
      prev = None
      while head:
         next = head.next
         head.next = prev
         prev = head
         head = next
      return prev

def printlist(head):
   current = head
   while current:
      print(current.val)
      current = current.next
   
   
def main():
   head = ListNode(1)
   head.next = ListNode(2)
   head.next.next = ListNode(3)
   head.next.next.next = ListNode(4)
   printlist(head)
   instance = Solution()
   prev = instance.reverseList(head)
   printlist(prev)

if __name__ == "__main__":
   main()