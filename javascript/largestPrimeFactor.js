// Project Eulers
/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the given number?
*/

function largestPrimeFactor(number) {
    if(isPrime(number)) return number
  
    let sqrt = Math.floor(Math.sqrt(number))
    
    sqrt = sqrt % 2 === 0 ? sqrt + 1 : sqrt
  
    for( let i = sqrt; i >= 1; i-= 2){
      if(((number % i) === 0) && isPrime(i)){
        return i
      }
    }
  }
  
  function isPrime(number){
    if(number % 2 === 0 && number !== 2) return false 
    
    for(let i = 3; i < Math.sqrt(number); i+=2){
      if((number % i) === 0){
        return false
      }
    }
    return true
  }
  
  largestPrimeFactor(13195);