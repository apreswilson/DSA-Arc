from typing import Optional

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
class Solution:
   def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      if not root:
         return True
      return self.isMirror(root.left, root.right) 
   def isMirror(self, tree1, tree2):
      if not tree1 and not tree2:
         return True
      if not tree1 or not tree2:
         return False
      return (tree1.val == tree2.val and self.isMirror(tree1.left, tree2.right)
              and self.isMirror(tree1.right, tree2.left))

def main():
   root = TreeNode(1)
   root.left = TreeNode(2)
   root.left.left = TreeNode(3)
   root.left.right = TreeNode(4)

   root.right = TreeNode(2)
   root.right.left = TreeNode(4)
   root.right.right = TreeNode(3)

   solution_instance = Solution()
   solution_instance.isSymmetric(root)

if __name__ == "__main__":
   main()