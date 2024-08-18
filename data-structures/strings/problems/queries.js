function queryFunction(string, firstChar, endChar) {
   firstChar %= string.length;
   endChar %= string.length;

   if (string[firstChar] === string[endChar]) {
      console.log("true");
   } else {
      console.log(false);
   }
}

function main() {
   let string = "geeksforgeeks";

   queryFunction(string, 0, 8)
}

main() 