class Node:
   def __init__(self, val):
      self.val= val 
      self.right = None
      self.left = None

class Solution:
   def mySolution(self, root: Node):
      if not root:
         return
      #Print has right
      if root.right:
         print("Has right", root.val)
      #Print has left
      if root.left:
         print("Has left:", root.val)
      #Print only if left leaf
      if root.left and not root.left.left and not root.left.right:
         print("Left only leaf", root.left.val)
      #Print only if right leaf
      if root.right and not root.right.right and not root.right.left:
         print("Right only leaf", root.right.val)
      #Print only if parent
      if root.right and root.left:
         print("Has left and right", root.val)
      self.mySolution(root.left)
      self.mySolution(root.right)

def main():
   root = Node(1)
   root.left = Node(2)
   root.right = Node(3)
   root.left.left = Node(4)
   root.left.right = Node(5)
   root.right.left = Node(6)
   root.right.right = Node(7)

   solution_instance = Solution()
   solution_instance.mySolution(root)

if __name__ == "__main__":
   main()