# Not sure if this is 100% right, the geeksforgeeks page was pretty all over the place on this algorithm.

def isOperator(arg):
   if arg in "+-/*":
      return True
   else:
      return False

def postfix_to_prefix(postfix):
   stack = []
   for i in range(len(postfix)):
      print(stack)
      if isOperator(postfix[i]):
         oper1 = stack[-1]
         stack.pop()
         oper2 = stack[-1]
         stack.pop()
         temp = postfix[i] + oper2 + oper1
         stack.append(temp)
      else: 
         stack.append(postfix[i])
   return stack[0]

def main():
   postfix = "ABC/-AK/L-*AB+CD-*"
   print(postfix_to_prefix(postfix))

if __name__ == "__main__":
   main()