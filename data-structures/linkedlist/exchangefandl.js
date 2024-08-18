// javascript program to exchange
// first and last node in
// circular linked list    

//THIS IS NOT MY ORIGINAL CODE, IT WAS COPIED BECAUSE
// I DIDNT UNDERSTAND HOW MY CODE WASNT WORKING
class Node {
    constructor() {
        this.data = 0;
        this.next = null;
    }
}
    function addToEmpty(head , data) {
        // This function is only
        // for empty list
        if (head != null)
            return head;
 
        // Creating a node dynamically.
        var temp = new Node();
 
        // Assigning the data.
        temp.data = data;
        head = temp;
 
        // Creating the link.
        head.next = head;
 
        return head;
    }
 
    function addBegin(head , data) {
        if (head == null)
            return addToEmpty(head, data);
 
        var temp = new Node();
 
        temp.data = data;
        temp.next = head.next;
        head.next = temp;
 
        return head;
    }
 
    // function for traversing the list
    function traverse(head) {
    var p;
 
        // If list is empty, return.
        if (head == null) {
            console.log("List is empty.");
            return;
        }
 
        // Pointing to first
        // Node of the list.
        p = head;
 
        // Traversing the list.
        do {
            console.log(p.data + " ");
            p = p.next;
 
        } while (p != head);
    }
 
    // Function to exchange
    // first and last node
    function exchangeNodes(head) {
 
        // If list is of length 2
        if (head.next.next == head) {
            head = head.next;
            return head;
        }
        // Find pointer to previous
        // of last node
        var p = head;
        while (p.next.next != head)
            p = p.next;
 
        // Exchange first and last
        // nodes using head and p
        p.next.next = head.next;
        head.next = p.next;
        p.next = head;
        head = head.next;
 
        return head;
    }
 
    // Driver Code
     
        var i;
        var head = null;
        head = addToEmpty(head, 6);
 
        for (i = 5; i > 0; i--)
            head = addBegin(head, i);
       
        traverse(head);
       
 
        
        head = exchangeNodes(head);
        traverse(head);
 
// This code is contributed by umadevi9616 
