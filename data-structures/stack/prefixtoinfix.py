def isOperator(arg):
   operators = ["*","+","-","/","^","(",")"]
   if arg in operators:
      return True
   else:
      return False

def prefix_to_infix(prefix):
   stack = []
   i = len(prefix) - 1
   while i >= 0:
      print(stack)
      if not isOperator(prefix[i]):
         stack.append(prefix[i]) 
         i -= 1
      else:
         str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
         stack.append(str)
         i -= 1
   return stack.pop()

def main():
   prefix = "*-A/BC-/AKL"
   print(prefix_to_infix(prefix))

if __name__ == "__main__":
   main()
