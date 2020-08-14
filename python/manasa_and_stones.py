"""
https://www.hackerrank.com/challenges/manasa-and-stones/problem
"""

def stones(n, a, b):
    arr = []
    for i in range(0,n):
        j = (n-1) - i
        solution = (i * a) + (j * b)
        arr.append(solution)
    
    arr = set(arr)
    arr = list(arr)
    arr.sort()
    return arr