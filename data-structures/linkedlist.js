class Node {
	constructor(new_data) {
		this.data = new_data;
		this.next = null;
	}
}

function insertNewNode(head, key, newData) {
	let curr = head;

	while (curr !== null) {
		if (curr.data === key) {
			break;
		}
		curr = curr.next;
	}

	let newNode = new Node(newData);

	newNode.next = curr.next;

	curr.next = newNode;

	return head;
}


function searchForNode(head, key) {
	let curr = head;

	while (curr !== null) {
		if (curr.data === key) {
			console.log("Found " + key);
			return;
		}
		curr = curr.next;
	}
	console.log("Not found");
}

function printList(head) {
	while (head !== null) {
		console.log(head.data + "->");

		head = head.next;
	}
	console.log("null");
}

function getLengthOfList(head) {
	let count = 0;
	let curr = head;

	while (curr !== null) {
		count++;
		curr = curr.next;
	}

	console.log("Length of list: " + count);
}

function reverseList(head) {
	let curr = head;
	let prev = null;
	let next;

	while (curr !== null) {
		next = curr.next;

		curr.next = prev;

		prev = curr;
		curr = next;
	}
	return prev;
}

function deleteNode(head, position) {
	let temp = head;
	let prev = null;

	if (temp === null) {
		return head;
	}

	if (position === 1) {
		head = temp.next;
		return head;
	}

	for (let i = 1; temp !== null && i < position; i++) {
		prev = temp;
		temp = temp.next;
	}

	if (temp !== null) {
		prev.next = temp.next;
	} else {
		console.log("Data not found");
	}

	return head;
}

function deleteList(head) {
	head = null;
	return head;
}

function nthFromEnd(head, n) {
	let length = 0;
	let curr = head;

	while (curr !== null) {
		curr = curr.next;
		length++;
	}

	if (length < n) {
		return -1;
	}

	curr = head;

	for (let i = 1; i < length - n + 1; i++) {
		curr = curr.next;
	}

	return curr.data;
}

function main() {
	let head = new Node(2);
	head.next = new Node(3);
	head.next.next = new Node(5);
	head.next.next.next = new Node(6);


	printList(head);

	let key = 3, newData = 4;

	head = insertNewNode(head, key, newData);
	printList(head);

	let keyToFind = 4;

	searchForNode(head, keyToFind);

	getLengthOfList(head);

	head = reverseList(head);
	printList(head);

	let position = 2;
	head = deleteNode(head, position);

	printList(head);

	printList(head);
	console.log(nthFromEnd(head, 2));

	console.log(head);
	head = null;
	console.log(head);
}

main();
