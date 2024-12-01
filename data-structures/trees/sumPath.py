class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
class Solution:
   def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
      def pathsum(root, targetSum):
         if not root:
            return False
         targetSum -= root.val
         if not root.right and not root.left and targetSum == 0:
            return True
         return pathsum(root.left, targetSum) or pathsum(root.right, targetSum)
      truthy = pathsum(root, targetSum)
      return truthy
      

def main():
   root = TreeNode(5)

   root.left = TreeNode(4)
   root.left.left = TreeNode(11)
   root.left.left.left = TreeNode(7)
   root.left.left.right = TreeNode(2)

   root.right = TreeNode(8)
   root.right.left = TreeNode(13)
   root.right.right = TreeNode(4)
   root.right.right.right = TreeNode(1)

   target = 22

   solution_instance = Solution()
   solution_instance.hasPathSum(root, target)
if __name__ == "__main__":
   main()     