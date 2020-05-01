// Project Eulers
/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two n-digit numbers.
*/

function largestPalindromeProduct(n) {
    let number = +Array(n).fill(9).join('')
  
    let palindromes = []
    let product = 1
    
    for(let i = number; i >= 1; i--){
      for(let j = number; j >= 1; j--){
        product = i * j
        if(isPalindrome(product)) palindromes.push(product)
      }
    }
  
    return Math.max(...palindromes)
  }
  
  function isPalindrome(number){
    return number.toString() === number.toString().split('').reverse().join('')
  }
  
  largestPalindromeProduct(3);