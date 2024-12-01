from queue import Queue
from collections import deque

class Node: 
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

#Left, root, right. Its literally put in that order in the code.
def in_order_dfs(root):
   if root is None:
      return
   in_order_dfs(root.left)
   print(root.data)
   in_order_dfs(root.right)

#Root, left, right
def pre_order_dfs(root):
   if root is None:
      return
   print(root.data)
   pre_order_dfs(root.left)
   pre_order_dfs(root.right)

#Left, right, root
def post_order_dfs(root):
   if root is None:
      return
   post_order_dfs(root.left)
   post_order_dfs(root.right)
   print(root.data)

#Level order traversal, left to right each level
def bfs(root):
   if root is None:
      return
   queue = [root]
   while queue:
      node = queue.pop(0)
      print(node.data)
      if node.left:
         queue.append(node.left)
      if node.right:
         queue.append(node.right)

def find_max_element(root):
   if root is None:
      return float("-inf")
   max_value = float("-inf")
   q = Queue()
   q.put(root) 
   while not q.empty():
      node = q.get() 
      max_value = max(max_value, node.data)
      if node.left:
         q.put(node.left)
      if node.right:
         q.put(node.right)
   print(max_value)

def find_element(root, number):
   if root is None:
     print("False") 
   queue = []
   queue.append(root)
   while queue:
      node = queue.pop(0)
      if node.data == number:
         print("True") 
      if node.left:
         queue.append(node.left)
      if node.right:
         queue.append(node.right)

def find_depth(root):
   if not root:
      return 0
   depth = 0
   q = deque()
   q.append(root)
   q.append(None)
   while q:
      current = q.popleft()
      if current is None:
         depth += 1
         if q:
            q.append(None)
      else:
         if current.left:
            q.append(current.left)
         if current.right:
            q.append(current.right)
   print(depth)

def h_and_d_of_node(root, value):
   if root is None:
      return
   depth = -1
   height = -1
   queue = [root]
   level = 0
   while queue:
      n = len(queue)
      for i in range(n):
         front = queue.pop(0)
         if front.data == value:
            depth = level
         if front.left:
            queue.append(front.left)
         if front.right:
            queue.append(front.right)
      level +=1
   height = level - depth - 1
   print("Depth: ", depth)
   print("Height: ", height)

def level_of_node(root, target, level):
   if root is None:
      return -1
   if root.data == target:
      print(level)
   leftLevel = level_of_node(root.left, target, level + 1)
   if leftLevel != -1:
      return leftLevel
   return level_of_node(root.right, target, level + 1)

def insert_element(root, number):
   if root is None:
      root = Node(number)
      return root
   q = deque()
   q.append(root)
   while q:
      current = q.popleft()
      if current.left:
         q.append(current.left)
      else: 
         current.left = Node(number)
         return root 
      if current.right:
         q.append(current.right)
      else:
         current.right = Node(number)
         return root

#Used in delete_node
def delete_deepest(root, delNode):
   queue = [root]
   while queue:
      curr = queue.pop(0)
      if curr == delNode:
         curr = None
         del delNode
         return
      if curr.right:
         if curr.right == delNode:
            curr.right = None
            del delNode
            return
         queue.append(curr.right)
      if curr.left:
         if curr.left == delNode:
            curr.left = None
            del delNode
            return
         queue.append(curr.left)

def delete_node(root, value):
   if root is None:
      return None
   if root.left is None and root.right is None:
      if root.data == value:
         return None
      else:
         return root
   queue = [root]
   curr = None
   keyNode = None
   while queue:
      curr = queue.pop(0)
      if curr.data == value:
         keyNode = curr
      if curr.left:
         queue.append(curr.left)
      if curr.right:
         queue.append(curr.right)
   
   if keyNode is not None:
      x = curr.data
      keyNode.data = x
      delete_deepest(root, curr)
      return root

def leafs_of_tree(root):
   if not root:
      return
   if not root.left and not root.right:
      print(root.data)
   if root.left:
      leafs_of_tree(root.left)
   if root.right:
      leafs_of_tree(root.right)

def main():
   root = Node(5)
   root.left = Node(10)
   root.right = Node(15)
   root.left.left = Node(20)
   root.left.right = Node(25)
   root.left.right.right = Node(45)
   root.right.left = Node(30)
   root.right.right = Node(35)

   print("In order: left, root, right")
   in_order_dfs(root)

   print("Pre order: root, left, right")
   pre_order_dfs(root)

   print("Post order: left, right, root")
   post_order_dfs(root)

   print("BFS")
   bfs(root)

   print("Find max value")
   find_max_element(root)

   print("Find specific element")
   find_element(root, 30)

   print("Find Depth")
   find_depth(root)

   print("Find height and depth of node")
   h_and_d_of_node(root, 25)

   print("Find level of node")
   level_of_node(root, 45, 1)

   print("Insert new element")
   insert_element(root, 50)
   in_order_dfs(root)

   print("Delete element")
   delete_node(root, 45)
   in_order_dfs(root)

   print("Print all leafs")
   leafs_of_tree(root)

if __name__ == "__main__":
   main()
