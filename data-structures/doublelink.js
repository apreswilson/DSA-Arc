class Node {
	constructor(data) {
		this.data = data;
		this.prev = null;
		this.next = null;
	}
}

function insertAtBeginning(head, node) {
	const addedNode = new Node(node);
	addedNode.next = head;

	if (head !== null) {
		head.prev = addedNode;
	}
	return addedNode;
}

function insertAtSelectedPosition(head, node, position) {
	let prevNode = head;

	for (let i = 0; i < position - 1; i++) {
		if (prevNode === null) {
			return head;
		}
		prevNode = prevNode.next;
	}

	const temp = new Node(node);
	temp.next = prevNode.next;
	temp.prev = prevNode;
	if (prevNode.next !== null) {
		prevNode.next.prev = temp;
	}
	prevNode.next = temp;
	return head;
}

function deleteAtSelectedPosition(head, position) {
 // If the list is empty
    if (head === null) {
        return head;
    }

    let curr = head;

    // Traverse to the node at the given position
    for (let i = 1; curr !== null && i < position; ++i) {
        curr = curr.next;
    }

    // If the position is out of range
    if (curr === null) {
        return head;
    }

    // Update the previous node's next pointer
    if (curr.prev !== null) {
        curr.prev.next = curr.next;
    }

    // Update the next node's prev pointer
    if (curr.next !== null) {
        curr.next.prev = curr.prev;
    }

    // If the node to be deleted is the head node
    if (head === curr) {
        head = curr.next;
    }

    // Deallocate memory for the deleted
    // node (JavaScript handles garbage collection)
    curr = null;

    return head;
}

function reverseList(head) {
	let temp = null;
	let current = head;

	while (current !== null) {
		temp = current.prev;
		current.prev = current.next;
		current.next = temp;
		current = current.prev;
	}

	if (temp != null) {
		head = temp.prev;
	}

	return head;
}

function printList(head) {
	let current = head;
	while (current !== null) {
		console.log(current.data);
		current = current.next;
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
	console.log("-----");
	head = insertAtBeginning(head, 0);
	printList(head);
	console.log("-----");
	head = insertAtSelectedPosition(head, 3.5, 4);
	printList(head);
	console.log("-----");
	head = deleteAtSelectedPosition(head, 4);
	printList(head);
	console.log("-----");
	head = reverseList(head);
	printList(head);
}

main();
