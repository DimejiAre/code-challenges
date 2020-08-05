"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""

def rotLeft(a, d):
    starting_index = d % len(a)
    rotated_array = []

    for i in range(0,len(a)):
        rotated_array.append(a[starting_index])
        starting_index += 1
        if starting_index >= len(a):
            starting_index = 0
    
    return rotated_array