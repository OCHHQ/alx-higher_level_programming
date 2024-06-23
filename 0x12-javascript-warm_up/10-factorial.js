#!/usr/bin/node

function factorial(n) {
  if (isNaN(n) || n < 0) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    let result = 1;
    for (let i = 1; i <= n; i++) {
      result *= i;
    }
    return result;
  }
}

const arg = parseInt(process.argv[2]);
console.log(factorial(arg));

