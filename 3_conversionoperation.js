
//***********conversion*************//


let score = "33"; //undefined => NaN ( not a number),null => 0 , true => 1 , string =>Nan
//console.log(typeof score);

let valueInNumber = Number(score)
console.log(typeof valueInNumber);
// "33" => 33  string to number
// "33abc" => NaN
// false => 0

let isLoggedIn = "0"
let booleanIsLoggedIn = Boolean(isLoggedIn)
console.log(booleanIsLoggedIn);

// 1 => true; 0 => false
// "" => false
// "payal" => true

let someNumber = 33
let stringNumber = String(someNumber)
console.log(stringNumber);



//****************operation************//
let value = 3
let negValue = -value
console.log(negValue);

console.log(2+2);
console.log(2-2);
console.log(2*2);
console.log(2**2);
console.log(2/2);
console.log(2%2);
console.log(2**3);

let str1 = "hello"
let str2 = " payal" // space is taken so two string doesnot attach
let str3 = str1+str2
console.log(str3);

console.log("1" + 2);
console.log(1 + "2");
console.log("1" + 2 + 2);
console.log(1 + 2 + "2");

console.log(true);
console.log(+true);
console.log(+"");

