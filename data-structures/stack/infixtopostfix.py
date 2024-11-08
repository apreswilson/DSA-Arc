def precedence(operator):
   if operator in ('+', "-"):
      return 1
   if operator in ('*','*'):
      return 2
   if operator in '^':
      return 3
   return 0

def solve(expression):
   postfix = ""
   stack=[]
   for char in expression:
      if char.isalnum(): 
         postfix += char 
      elif char == '(':
         stack.append(char)
      elif char == ')':
         while stack and stack[-1] != '(':
            postfix += stack.pop()
         stack.pop()
      else:
         while (stack and precedence(stack[-1]) >= precedence(char)):
            postfix += stack.pop()
         stack.append(char)
   while stack:
      postfix += stack.pop()
   print(postfix)

def main():
   expression = "a+b*(c^d-e)^(f+g*h)-1"
   solve(expression)


if __name__ == "__main__":
   main()