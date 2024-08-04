class Node {
	constructor(new_data) {
		this.data = new_data;
		this.next = null;
	}
}

function findMiddleIndex (head) {
	let valueArray = [];
	let current = head;

	while (current !== null) {
		valueArray.push(current.data);
		current = current.next;
	}
	let middleIndex = Math.floor(valueArray.length / 2);	
	return valueArray[middleIndex];
}

function main() {
	let head = new Node(1);
	head.next = new Node(2);
	head.next.next = new Node(3);
	head.next.next.next = new Node(4);

	findMiddleIndex(head);
}

main();
