// Project Eulers
/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the nth prime number?
*/

function nthPrime(n) {
    let number = 2
    let primeCount = 0
    while(number > 1){
      if(isPrime(number)){
        primeCount++
      }
      if(primeCount === n){
        return number
      }
      number++
    }
}

function isPrime(num){
  if (num !== 2 && num % 2 === 0) return false
  for(let i = 3; i < num; i+= 2){
    if(num % i === 0){
      return false
    }
  }
  return true
}

nthPrime(10001);