//Project Eulers
/*
Work out the first ten digits of the sum of the following 50-digit numbers.
const testNums = [
  '37107287533902102798797998220837590246510135740250',
  '46376937677490009712648124896970078050417018260538'
]

*/

function largeSum(arr) {
    let sum = BigInt(0)
    for(let num of arr){
      sum += BigInt(num)
    }
    return +sum.toString().slice(0,10);
  }
  
  const testNums = [
    '37107287533902102798797998220837590246510135740250',
    '46376937677490009712648124896970078050417018260538'
  ];
  
  console.log(largeSum(testNums));
  