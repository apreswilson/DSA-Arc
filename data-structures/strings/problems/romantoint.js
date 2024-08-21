function romanToInt(s) {
   let arr = s.split("");
   let totalValue = 0;
   for (let i = 0; i < arr.length; i++) {

      if (arr[i] === "I" && arr[i + 1] === "V") {
         arr[i] = "IV";
         arr[i + 1] = null;
      } else if (arr[i] === "I" && arr[i + 1] === "X") {
         arr[i] = "IX";
         arr[i + 1] = null;
      }

      if (arr[i] === "X" && arr[i + 1] === "L") {
         arr[i] = "XL";
         arr[i + 1] = null;
      } else if (arr[i] === "X" && arr[i + 1] === "C") {
         arr[i] = "XC";
         arr[i + 1] = null;
      }

      if (arr[i] === "C" && arr[i + 1] === "D") {
         arr[i] = "CD";
         arr[i + 1] = null;
      } else if (arr[i] === "C" && arr[i + 1] === "M") {
         arr[i] = "CM";
         arr[i + 1] = null;
      }

      switch (arr[i]) {
         case "IV":
            totalValue += 4;
            break;
         case "IX":
            totalValue += 9;
            break;
         case "XL":
            totalValue += 40;
            break;
         case "XC":
            totalValue += 90;
            break;
         case "CD":
            totalValue += 400;
            break;
         case "CM":
            totalValue += 900;
            break;
         case "I":
            totalValue += 1;
            break;
         case "V":
            totalValue += 5;
            break;
         case "X":
            totalValue += 10;
            break;
         case "L":
            totalValue += 50;
            break;
         case "C":
            totalValue += 100;
            break;
         case "D":
            totalValue += 500;
            break;
         case "M":
            totalValue += 1000;
            break;
         default:
            totalValue += 0;
            break;
      }
   }
   console.log(totalValue);
};

romanToInt("MCMXCIV");
