// Hackerrank
/*
https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
*/

function luckBalance(k, contests) {
    // loop through contests, create 2 arrays using the important factors
        // important and unimportant
    let important = []
    let unimportant = []

    contests.forEach(contest => {
        if(contest[1] === 1){
            important.push(contest[0])
        } else {
            unimportant.push(contest[0])
        }
    })

    // sort the important array
    important.sort(function(a,b){
        return a - b
    })
    // create wins variable which is importantSet.length - k
    let winsNum = important.length - k
    let wins = []
    // loop through sorted important array and remove the wins into a wins array
    for(let i = 0; i < winsNum; i++){
        wins.push(important.shift())
    }
    // then add all values of important array and unimportant, then subtract wins array

    let losses = important.concat(unimportant)

    let sumLosses = losses.reduce((a,b) => a + b, 0)

    let sumWins = wins.reduce((a,b) => a + b, 0)

    return sumLosses - sumWins
}