"""
https://www.hackerrank.com/challenges/equality-in-a-array/problem
"""

def equalizeArray(arr):
    count = {}
    largest = 0
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
        largest = max(count[i], largest)

    return (len(arr) - largest)

