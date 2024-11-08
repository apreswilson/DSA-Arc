from collections import deque
from queue import Queue

class TreeNode:
   def __init__(self, data) -> None:
      self.data = data
      self.children = []

   def add_child(self, child_node):
      self.children.append(child_node)

   def display(self, level=0):
      print (' ' * level * 2 + str(self.data))
      for child in self.children:
         child.display(level + 1)

   #root, left, right
   def preorder(self):
      print(self.data)
      for child in self.children:
         child.preorder()

   #left, right, root
   def postorder(self):
      for child in self.children:
         child.postorder()
      print(self.data)

   #left, root, right
   def inorder(self):
      mid = len(self.children) // 2
      for child in self.children[:mid]:
         child.inorder()
      print(self.data)
      for child in self.children[mid:]:
         child.inorder()

   #level order traversal
   def bfs(self):
      queue = deque([self])
      while queue:
         current = queue.popleft()
         print(current.data)
         for child in current.children:
            queue.append(child)
   
   def find_max(self):
      if self is None:
         return float('-inf')

      q = Queue()
      max_val = float('-inf')
      q.put(self)

      while not q.empty():
         current = q.get()
         max_val = max(max_val, current.data)
         for child in current.children:
            q.put(child)
      return max_val

   def find_element(self, data):
      if self is None:
         return False

      queue = [self]
      while queue:
         node = queue.pop(0)
         if node.data == data:
            return True
         for child in node.children:
            queue.append(child)

   def reverse_tree(self):
      if self is None:
         return
      
      queue = [self]
      stack = []
      
      while queue:
         temp = queue.pop(0)
         stack.append(temp.data)
         for child in temp.children:
            queue.append(child)

      while stack:
         print(stack.pop())

   def height(self):
      if self is None:
         return 0

      max_child_height = 0
      for child in self.children:
         max_child_height = max(max_child_height, child.height())
      return max_child_height + 1

   def deepest(self):
      if self is None: 
         return None
      
      queue = [self]
      deepest_node = self
      while queue:
         current = queue.pop(0)
         deepest_node = current
         for child in current.children:
            queue.append(child)
      return deepest_node.data

   def delete_node(self, value):
      if self.data == value:
         return None
      
      new_children = []
      for child in self.children:
         updated_child = child.delete_node(value)
         if updated_child is not None:
            new_children.append(updated_child)
      
      self.children = new_children
      return self

def main():
   root = TreeNode(1)
   child1 = TreeNode(2)
   child2 = TreeNode(3)
   child3 = TreeNode(4)
   child4 = TreeNode(5)
   child5 = TreeNode(6)
   child6 = TreeNode(7)

   root.add_child(child1)
   root.add_child(child2)
   child1.add_child(child3)
   child1.add_child(child4)
   child2.add_child(child5)
   child2.add_child(child6)

   root.display()
   print("------")
   root.preorder()
   print("------")
   root.postorder()
   print("------")
   root.bfs()
   print("------")
   root.inorder()
   print("------")
   print(root.find_max())
   print("------")
   print(root.find_element(5))
   print("------")
   print(root.height())
   print("------")
   print(root.deepest())
   print("------")
   print(root.delete_node(2))
   print("------")
   root.display()
if __name__ == "__main__":
   main()