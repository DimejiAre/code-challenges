"""
https://www.hackerrank.com/challenges/cut-the-sticks/problem
"""

def cutTheSticks(arr):
    arr.sort()
    stick_count = [len(arr)]
    
    while len(arr) > 0:
        smallest = arr[0]
        remove_count = 0
        
        for i in range(len(arr)):
            if arr[i] == smallest:
                remove_count += 1
            else:
                arr[i] -= smallest

        arr = arr[remove_count:]
        
        stick_count.append(len(arr))

    
    return stick_count[:-1]

