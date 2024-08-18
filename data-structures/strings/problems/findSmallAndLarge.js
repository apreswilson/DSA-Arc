function findSmallAndLarge(string) {
   let splitString = string.split(" ");
   let leastLength = splitString[0];
   let maxLength = "";

   for (let i = 0; i < splitString.length; i++) {
      if (leastLength.length > splitString[i].length && splitString[i].length < maxLength.length) {
         leastLength = splitString[i];
      }

      if (maxLength.length < splitString[i].length) {
         maxLength = splitString[i];
      }
   }

   console.log(leastLength, maxLength);
}

function main() {
   let string = "GeeksforGeeks A computer Science portal for Geeks";
   
   findSmallAndLarge(string)
}

main();