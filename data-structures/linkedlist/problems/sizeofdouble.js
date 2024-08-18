class Node {
	constructor(data) {
		this.data = data;
		this.prev = null;	
		this.next = null;
	}
}

function printList(head) {
	let current = head;
	let count = 0;

	while (current !== null) {
		count++;
		console.log(current.data);
		current = current.next;
	}
}

function deleteGivenNode(head, nodeToDelete) {
	let current = head;

	while (current != null) {
		if (current.data === nodeToDelete) {
			current.prev.next = current.next;
			current.next.prev = current.prev;
			current = null;
			break;
		}
		current = current.next;
	}
}

function main() {
	const head = new Node(1);
	const second = new Node(2);
	const third = new Node(3);

	head.next = second;
	second.prev = head;
	second.next = third;
	third.prev = second;

	printList(head);

	deleteGivenNode(head, 2);

	printList(head);
}

main();
