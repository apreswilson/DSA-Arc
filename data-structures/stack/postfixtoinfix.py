def isOperand(arg):
   return ((arg >= 'a' and arg <= 'z') or (arg >= 'A' and arg <= 'Z'))

def postfix_to_infix(postfix):
   stack = []
   for i in postfix:
      print(stack)
      if isOperand(i):
         stack.insert(0, i)
      else:
         op1 = stack[0]
         stack.pop(0)
         op2 = stack[0]
         stack.pop(0)
         stack.insert(0, "(" + op2 + i + op1 + ")")
   return stack[0]

def main():
   postfix = "ab*c+"
   print(postfix_to_infix(postfix))

if __name__ == "__main__":
   main()