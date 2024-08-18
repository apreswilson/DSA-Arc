function convertToCamelCase(string) {
   let splitString = string.split(" ");
   let returnString = "";
   for (let i = 0; i < splitString.length; i++) {
      let firstChar = splitString[i].substring(0, 1).toUpperCase();
      let remainChar = splitString[i].substring(1, splitString[i].length).toLowerCase();
      returnString += firstChar + remainChar;
   }
   console.log(returnString);
}

function main() {
   let string = "I got intern at geeksforgeeks";

   convertToCamelCase(string);
}

main();