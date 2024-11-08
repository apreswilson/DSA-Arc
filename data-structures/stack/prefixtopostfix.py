def prefix_to_postfix(prefix):
   stack = []
   operators = set(["+", "-", "*", "/", "^"])
   prefix = prefix[::-1] #This reverses order of array, remember this
   for i in prefix:
      print(stack)
      if i in operators:
         a = stack.pop()
         b = stack.pop()
         temp = a + b + i
         stack.append(temp)
      else:
         stack.append(i)
   return stack.pop()


def main():
   prefix = "*-A/BC-/AKL"
   print(prefix_to_postfix(prefix))

if __name__ == "__main__":
   main()