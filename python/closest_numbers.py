"""
https://www.hackerrank.com/challenges/closest-numbers/problem
"""

def closestNumbers(arr):
    arr.sort()
    pairs = []
    absDiff = abs(arr[0] - arr[1])
    for num in range(len(arr) - 1):
        newAbsDiff = abs(arr[num] - arr[num + 1])
        if newAbsDiff < absDiff:
            pairs = [arr[num], arr[num + 1]]
            absDiff = newAbsDiff
        elif newAbsDiff == absDiff:
            pairs.append(arr[num])
            pairs.append(arr[num + 1])
    
    return pairs