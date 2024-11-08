#This is a linked list stack
class StackNode:
   def __init__(self, data) -> None:
      self.data = data
      self.next = None

class Stack:
   def __init__(self) -> None:
      self.root = None

   def isEmpty(self):
      return True if self.root is None else False
   
   def push(self, data):
      newNode = StackNode(data)
      newNode.next = self.root
      self.root = newNode

   def pop(self):
      if (self.isEmpty()):
         return float("-inf")
      temp = self.root
      self.root = self.root.next
      popped = temp.data
      return popped 
   
   def peek(self):
      if self.isEmpty():
         return float("-inf")
      return self.root.data

#This is a functional stack   
def createStack():
   new = []
   return new

def fisEmpty(newstack):
   return len(newstack) == 0

def fpush(newstack, item):
   newstack.append(item)
   print(f"{item} Added")

def fpop(newstack):
   if (fisEmpty(newstack)):
      print("Stack is empty")
      return
   return newstack.pop()

def fpeek(newstack):
   if fisEmpty(newstack):
      print("Stack is empty")
      return
   return newstack[len(newstack) - 1]

def main():
   stack = Stack()
   stack.push(20)
   stack.push(30)
   stack.push(40)
   print(stack.peek())

   fstack = createStack()
   fpush(fstack, 10)
   fpush(fstack, 20)
   fpush(fstack, 30)
   print(fstack)
   fpop(fstack)
   print(fstack)

if __name__ == "__main__":
   main()   