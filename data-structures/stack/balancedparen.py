def check_for_balanced(stringpassed):
   stack = []
   for i in stringpassed:
      if i in "({[":
         stack.append(i)
      else:
         if not stack:
            return False
         
         pulled = stack.pop()
         if pulled == "(":
            if i != ")":
               return False
         if pulled == "{":
            if i != "}":
               return False
         if pulled == "[":
            if i != "]":
               return False
   if stack:
      return False
   return True
      

def main():
   evaluatedstring = "{()}[]"
   print(check_for_balanced(evaluatedstring))

if __name__ == "__main__":
   main()