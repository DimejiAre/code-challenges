// Hackerrank
/*
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
*/

function minimumAbsoluteDifference(arr) {
    arr.sort()
    
    if (arr.length < 2) return null

    let minimumAbsDiff = Math.abs(arr[1] - arr[0])

    if (arr.length < 3) return minimumAbsDiff

    for(let i = 2; i < arr.length; i++){
        let absDiff = Math.abs(arr[i] - arr[i-1])
        minimumAbsDiff = Math.min(minimumAbsDiff, absDiff)
    }

    return minimumAbsDiff
}
