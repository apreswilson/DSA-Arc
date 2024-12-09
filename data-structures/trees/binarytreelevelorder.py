from typing import List, Optional


class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Solution:
   def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      if not root:
         return
      sendarr = []
      queue = [root]
      while queue:
         size = len(queue)
         temp = []
         for _ in range(size):
            node = queue.pop(0)
            if node.left:
               queue.append(node.left)
            if node.right:
               queue.append(node.right)
            temp.append(node.val)
         sendarr.append(temp)
      print(sendarr) 

def main():
   root = TreeNode(3)
   
   root.left = TreeNode(9)

   root.right = TreeNode(20)
   root.right.left = TreeNode(15)
   root.right.right = TreeNode(7)
   instance = Solution()
   instance.levelOrder(root)

if __name__ == "__main__":
   main()