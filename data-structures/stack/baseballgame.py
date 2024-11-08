class Solution:
   def calPoints(self, operations: list[str]) -> int:
      stack = []
      for i in operations:
            print(i)
            if i.isnumeric():
               stack.append(int(i))
            elif i=="C":
               stack.pop()
            elif i=="D":
               stack.append(stack[-1]*2)
            elif i=="+":
               stack.append(stack[-1]+stack[-2])
            elif i[0]=="-":
               stack.append(int(i))
      return sum(stack)

         

def main():
   input = ["5","2","C","D","+"]
   x = Solution()
   x.calPoints(input)

if __name__ == "__main__":
    main()