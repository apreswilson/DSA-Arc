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

function main() {
	const head = new Node(1);
	const second = new Node(2);
	const third = new Node(3);
	
	head.prev = third;
	head.next = second;
	second.prev = head;
	second.next = third;
	third.prev = second;
	third.next = head;

	printList(head);
}

main();
