
function searchForCharacter(string, char) {
	for (let i = 0; i < string.length; i++) {
		if (string[i] === char) {
			console.log(char + " exists at index " + i);
		}
	}
}

function reverseString(string) {
	let reverseString = "";

	for (let i = string.length - 1; i >= 0; i--) {
		reverseString += string[i];
	}

	console.log(reverseString);
}

function rotateStringLeft(string, indexToStartAt) {
	let temp = string.substring(indexToStartAt, string.length);
	let temp2 = string.substring(0, indexToStartAt);
	let temp3 = temp + temp2;
	console.log(temp);
	console.log(temp2);
	console.log(temp3);	
}

function rotateStringRight(string, indexToEndAt) {
	return rotateStringLeft(string, string.length - indexToEndAt);
}

//IMPORTANT: ASCII LOWERCASE 97 - 122,
//ASCII UPPERCASE 65 - 90
function sortString(charsAvailable, string) {
	let charArray = new Array(charsAvailable);
	charArray.fill(0);
	let lower = string.toLowerCase();

	for (let i = 0; i < lower.length; i++) {
		charArray[lower[i].charCodeAt() - 'a'.charCodeAt()]++;
	}
	
	for (let i = 0; i < charsAvailable; i++) {
		for (let j = 0; j < charArray[i]; j++) {
			console.log(String.fromCharCode(i + 'a'.charCodeAt()));
		}
	}

	console.log(charArray);
}

function countOccurrences (maxChars, string) {
	let charArray = new Array(maxChars);
	let lower = string.toLowerCase();
	charArray.fill(0);
	
	for (let i = 0; i < lower.length; i++) {
		charArray[lower[i].charCodeAt() - 'a'.charCodeAt()]++;
	}
		
	for (let i = 0; i < maxChars; i++) {
		if (charArray[i] === 0) {
			continue;
		}
		console.log(String.fromCharCode(i + 'a'.charCodeAt()) +""+ charArray[i]);
	}
}

function swapLetters (string, swaps, charactersForward, lengthOfString) {
	charactersForward = charactersForward % lengthOfString;

	if (charactersForward === 0) {
		return string;
	}

	//This is 0 unless swaps > lengthOfString.
	let f = Math.floor(swaps / lengthOfString);
	

	//First String: All characters 0 -> charactersForward (in this case 3)
	//Second String: In this case 8 % 4 = 2. 2 * f (in this case 0) = 0.
	//0 % 3 = 0;
	let p1 = rotateLeftForSwapLetters(string.substring(0, charactersForward),
		((lengthOfString % charactersForward) * f) % charactersForward);
	console.log("Main Function Substring1 " + string.substring(0, charactersForward));
	

	//First String: All characters after charactersForward -> length;
	//Second String: In this case 3 * 0 = 0. 0 % 8 - 3 (5 in this case) = 0.
	let p2 = rotateLeftForSwapLetters(string.substring(charactersForward), 
		((charactersForward * f) % (lengthOfString - charactersForward)));
	console.log("Main Function Substring2 " + string.substring(charactersForward));

	// in this case 4 % 8 = 4 because 4 < 8. If x & y && x < y answer = x
	let r = swaps % lengthOfString;
	
	//Combine strings after these processes.
	let a = (p1 + p2).split("");

	//Finish doing any swaps that are possible
	for (let i = 0; i < r; i++) {
		let temp = a[i];
		a[i] = a[(i + charactersForward) % lengthOfString];
		a[(i + charactersForward) % lengthOfString] = temp;
	}

	console.log(a.join(""));
}

function rotateLeftForSwapLetters (string, p) {
	console.log("string " + string);
	console.log("p " + p);
	let returnVal1 = string.substring(p);
	let returnVal2 = string.substring(0,p);

	let total = returnVal1 + returnVal2;
	console.log("Substring 1 " + returnVal1);
	console.log("Substring 2 " + returnVal2);
	console.log("Combined String " + total);
	return string.substring(p) + string.substring(0,p);	
}

function addCharacterToString(string, characterPositionToInsertChar) {
	let newString = "";

	let j = 0;

	for (let i = 0; i < string.length; i++) {
		//This will execute as long as j isn't longer than length of characterPositionToInsertChar.
		//And when i is the same as characterPositionToInsertChar[j]. So if i = 3,
		//i is the same as  characterPositionToInsertChar[0] (which is 3). Insert star if both true.
		if (j < characterPositionToInsertChar.length && i === characterPositionToInsertChar[j]) {
			newString += "*";
			j++;
		}
		newString += string[i];
	}

	console.log(newString);
}

function removeOccurences (string, removeChar) {
	let newString = "";

	for (let i = 0; i < string.length; i++) {
		if (removeChar !== string[i]) {
			newString += string[i];
		}
	}
	console.log(newString);
}

//Doesn't work for some reason?
function regexRemoveOccurences (string, pattern) {
	string = string.replace(pattern, '');
	
	console.log(string);
}

function rotateString(string, rotation) {
  let newString = string.substring(rotation) + string.substring(0, rotation);
  console.log(newString);
}

function rotateStringLeet(s, goal) {
    let rotateString = s;
    for (let i = 0; i < s.length; i++) { 
        rotateString = rotateStringLeftLeet(rotateString);
        if (rotateString == goal) {
            console.log(true)
        }
    }
    console.log(false)
};

function rotateStringLeftLeet (string) {
    let rotatedString = string.substring(1, string.length) + string.substring(0, 1) ;
    return rotatedString;
}

function main() {
	const string = "Iamastring";
	const char = "a"	
	searchForCharacter(string, char);
	reverseString(string);
	rotateStringLeft(string, 2);
	rotateStringRight(string, 2);
	let maxChar = 26;
	sortString(maxChar, string);
	countOccurrences(maxChar, string);
	let string2 = "ABCDEFGH";
	swapLetters(string2, 4, 3, string2.length)
	let charPositionsToAdd = [3, 5];
	addCharacterToString(string2, charPositionsToAdd);
	removeOccurences(string, "a");
	let c = /k/g;
	regexRemoveOccurences(string, c);
  rotateString(string, 2);
  
  let goal = "astringIam";
  rotateStringLeet(string, goal)
}

main();
