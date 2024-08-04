// Solves findAmountOf instances of a specific number;
class Node {
   constructor(new_data) {
      this.data = new_data;
      this.next = null;
   }
}

function findAmountOfInts(head, intToLookFor) {
   let current = head;
   let count = 0;

   while (current !== null) {
      if (current.data === intToLookFor) {
         count++;
      }
      current = current.next;
   }
   return count;
}

function main() {
   let head = new Node(2);
   head.next = new Node(3);
   head.next.next = new Node(4);
   head.next.next.next = new Node(5);
   head.next.next.next.next = new Node(5);
   console.log(head);

   let intToSeek = 5;
   console.log(findAmountOfInts(head, intToSeek));
}

main();