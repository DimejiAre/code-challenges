//project Eulers

/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below n.
*/

function primeSummation(n) {

    function isPrime(num) {
      if ((num % 2 === 0) && num !== 2) return false
      for (let i = 3; i <= Math.sqrt(num); i += 2) {
        if (num % i === 0) return false
      }
      return true
    }
  
    let sum = 0
    for (let i = 2; i < n; i++) {
      if (isPrime(i)) {
        sum += i
      }
    }
    return sum
  }
  
  primeSummation(2000000);
  