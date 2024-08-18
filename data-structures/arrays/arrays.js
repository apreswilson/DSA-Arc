function insertElementAtPosition(array, indexToInsertAt, valueToInsert, position) {
   let i = indexToInsertAt - 1;
   for (i; i >= position; i--) {
      array[i + 1] = array[i];
   }
   array[position] = valueToInsert;
}

function insertAtEnd(arr, capacity, indexToInsertAt, valueToInsert) {
   if (indexToInsertAt >= capacity) {
      return indexToInsertAt;
   }

   arr[indexToInsertAt] = valueToInsert;
   return (indexToInsertAt + 1);
}

function linearSearch(array, item) {
   for (let i = 0; i < array.length; i++) {
      if (array[i] === item) {
         console.log("Item Found (Linear Search): " + item);
         return;
      }
   }
   console.log("Item Not Found");
}

function binarySearch(array, low, high, item) {
   while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      if (array[mid] === item) {
         console.log("Item Found (Binary Search): " + item);
         return;
      } else if (array[mid] < item) {
         low = mid + 1;
      } else {
         high = mid - 1;
      }
   }

   console.log("Item Not Found");
}

function deleteElement(array, length, deleteValue) {
   let curposition = 0;
   //Find Element
   for (let i = 0; i < length; i++) {
      if (array[i] === deleteValue) {
         curposition = i;
      }
   }

   for (; curposition < length - 1; curposition++) {
      array[curposition] = array[curposition + 1];
   }
   return length - 1;
}

function main() {
   let array = new Array(10).fill(0);
   //Populate first five elements
   for (let i = 0; i <= 5; i++) {
      array[i] = i;
   }
   console.log(array);

   let capacity = array.length;
   let indexToInsertAt = 6;
   let valueToInsert = 6;
   indexToInsertAt = insertAtEnd(array, capacity, indexToInsertAt, valueToInsert);
   console.log(array);

   let position = 2;
   indexToInsertAt++;
   valueToInsert++;

   insertElementAtPosition(array, indexToInsertAt, valueToInsert, position);
   console.log(array);

   let elementToFind = 6;
   linearSearch(array, elementToFind);

   let low = 0;
   let high = array.length - 1;
   binarySearch(array, low, high, elementToFind);

   let deleteValue = 4;
   let numsLength = 7; //Current length of actual present integers
   numsLength = deleteElement(array, numsLength, deleteValue);
   for (let i = 0; i < numsLength; i++) {
      console.log(array[i]);
   }
}

main();