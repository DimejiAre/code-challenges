/*
https://leetcode.com/problems/search-a-2d-matrix/submissions/

*/

var searchMatrix = function(matrix, target) {
    for(let i = 0; i < matrix.length; i++){
        if(matrix[i][0] <= target && target <= matrix[i][matrix[i].length - 1]){
            for(let j = 0; j < matrix[i].length; j++){
                if(matrix[i][j] === target){
                    return true
                }
            }
            return false
        }
    }
    return false
};

