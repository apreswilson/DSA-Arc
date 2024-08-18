class Node {
	constructor(data) {
		this.data = data;
		this.next = null;
	}
}

function countNodes (head) {
	let stopNode = head;
	let currentNode = head;
	let count = 1;

	while (currentNode.next != stopNode) {
		count++;
		currentNode = currentNode.next;
	}

	console.log(count);
}

function main() {
	let headNode = new Node(1);
	headNode.next = new Node(2);
	headNode.next.next = new Node(3);
	headNode.next.next.next = new Node(4);
	headNode.next.next.next.next = headNode;
	countNodes(headNode);
}

main();
