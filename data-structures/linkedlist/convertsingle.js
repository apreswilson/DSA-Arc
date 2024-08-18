class Node {
	constructor(data) {
		this.data = data;
		this.next = null;
	}
}

function convertSingle (head) {
	let currentNode = head;

	while (currentNode.next !== null) {
			currentNode = currentNode.next;
	}

	currentNode.next = head;

	return head;
}

function printList(head) {
	let currentNode = head;

	while (currentNode !== null)  {
		console.log(currentNode.data);
		currentNode = currentNode.next
	}

	return head;
}

function main() {
	let head = new Node(1);
	head.next = new Node(2);

	printList(head);

	convertSingle(head)

	console.log(head)
}

main();
