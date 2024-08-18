function findKthNonRepeat(string, k) {
   let hashMap = new Map();

   for (let i = 0; i < string.length; i++) {
      hashMap.set(string[i], (hashMap.get(string[i]) || 0) + 1);
   }

   let nthNotRepeat = 0;
   for (let i = 0; i < string.length; i++) {
      if (hashMap.get(string[i]) === 1) {
         nthNotRepeat++;
      }

      if (nthNotRepeat === k) {
         console.log(string[i]);
      }
   }
}

function main() {
   let string = "geeksforgeeks";
   let repeatingCharacter = 2;

   findKthNonRepeat(string, repeatingCharacter);
}

main();