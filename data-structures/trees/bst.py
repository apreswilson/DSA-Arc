class Node:
   def __init__(self, data):
      self.data = data
      self.right = None
      self.left = None

def in_dfs(root):
   if not root:
      return
   print(root.data)
   in_dfs(root.left)
   in_dfs(root.right)

def insert(root, data):
   if not root:
      return Node(data)
   else:
      if data < root.data:
         root.left = insert(root.left, data)
      elif data > root.data:
         root.right = insert(root.right, data)
   return root

def find(root, target):
   if not root:
      print("Didn't find:", target)
      return None
   elif root.data == target:
      print("Found:", target)
      return root
   elif target < root.data:
      return find(root.left, target)
   else:
      return find(root.right, target)

def main():
   root = Node(50)
   insert(root, 30)

   print("In-order Display Tree") 
   in_dfs(root)

   print("\nFind element")
   num_to_find = 30
   find(root, num_to_find)

   print("\nRemove Element")


if __name__ == "__main__":
   main()