"""
https://www.hackerrank.com/challenges/30-2d-arrays/problem
"""

def twod_arrays(arr):
    largest_sum = arr[0][1] + arr[0][0] + arr[0][2] + arr[1][1] + arr[2][1] + arr[2][0] + arr[2][2]

    for i in range(len(arr) - 2):
        for j in range(1, len(arr[i]) - 1):
            hour_glass_sum = arr[i][j] + arr[i][j-1] + arr[i][j+1] + arr[i+1][j] +                   arr[i+2][j] + arr[i+2][j-1] + arr[i+2][j+1]
            largest_sum = max(largest_sum, hour_glass_sum)
    
    print(largest_sum)

    