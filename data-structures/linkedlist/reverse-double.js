class Node {
	constructor(data) {
		this.data = data;
		this.prev = null;
		this.next = null;
	}
}

function printList(head) {
	let current = head;
	while (current !== null) {
		console.log(current.data);
		current = current.next;
	}
}

function reverseList(head) {
			var temp = null;
	var current = head;
        /*
         * swap next and prev for all nodes of doubly linked list
         */
        while (current != null) {
            temp = current.prev;
            current.prev = current.next;
            current.next = temp;
            current = current.prev;
        }
 
        /*
         * Before changing head, check for the cases like empty list and list with only
         * one node
         */
        if (temp != null) {
            head = temp.prev;
        }
    }


function main() {

	let head = new Node(1);
	let second = new Node(2);
	let third = new Node(3);
	let fourth = new Node(4);
	let fifth = new Node(5);

	head.next = second;
	second.prev = head;
	second.next = third;
	third.prev = second;
	third.next = fourth;
	fourth.prev = third;
	fourth.next = fifth;
	fifth.prev = fourth;

	printList(head);
	reverseList(head)
	printList(head);
}

main();
