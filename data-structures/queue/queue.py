# Use queue as array, it is just a FIFO structure.
# Enqueue (add element to read)
# Dequeue (removes and returns element from front of queue)
# Head (first element)
#Tail (last element)

def main():
   queue = []
   queue.append("a")
   queue.append("b")
   queue.append("c")
   print(queue)
   queue.pop(0)
   queue.pop(0)
   print(queue)

if __name__ == "__main__":
   main()