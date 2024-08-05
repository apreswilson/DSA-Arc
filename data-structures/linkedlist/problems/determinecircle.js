class Node{ 
    constructor(data){ 
        this.data = data; 
        this.next = null; 
    } 
} 
let head = null; 
function addToFront(data){ 
    let newNode = new Node(data); 
    newNode.next = head; 
    head = newNode; 
} 
  
function isCircular(){ 
    if(head == null) return false; 
    let slow = head; 
    let fast = head.next; 
    while(fast != null && fast.next != null){ 
        if(slow == fast) return true; 
        slow = slow.next; 
        fast = fast.next.next; 
    } 
    return false; 
} 
  
// driver function 
addToFront(1); 
addToFront(2); 
addToFront(3); 
addToFront(4); 
  
console.log(isCircular()); 
