class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
class Solution:
   def minDepth(self, root: TreeNode) -> int:
      def traverse(root, minNum) -> int:
         if not root:
            return float('inf')
         minNum += 1
         if not root.left and not root.right:
            return minNum
         return min(traverse(root.left, minNum), traverse(root.right, minNum))
      if not root:
         return 0
      minNum = 0
      outcome = traverse(root, minNum)
      return outcome
      

def main():
   root = TreeNode(3)
   root.right = TreeNode(3)
   root.right.right = TreeNode(4)
   root.right.right.right = TreeNode(5)
   root.right.right.right.right = TreeNode(6)

   solution_instance = Solution()
   solution_instance.minDepth(root)
if __name__ == "__main__":
   main()   