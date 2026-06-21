const accountId = 123445443
let accountEmail = "pyal@gmail.com"
var accountpassword = "123"
accountcity = "jaipur"
let accountstate;

// accountId = 2 // not allowed :: once constant created can't changed 
// let is used when there is chance of changing data or value

accountEmail = "fdf@gmail.com"
accountpassword = "2121"
accountcity = "bengaluru"

console.log(accountId);
console.log(accountEmail);

/*
prefer not to use var
bcz of issue in block scope and functional scope
*/

console.table([accountId,accountEmail,accountpassword,accountcity,accountstate])
