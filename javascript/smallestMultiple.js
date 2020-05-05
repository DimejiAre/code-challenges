// Project Eulers
/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?
*/

function smallestMult(n) {
    let multiple = 1
    for (let i = 1; i <= n; i++){
      if(multiple % i !== 0){
        multiple += 1
        i = 0
        continue
      }
    }
    return multiple
  }
  
  smallestMult(20);