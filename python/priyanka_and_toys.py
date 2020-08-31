"""
https://www.hackerrank.com/challenges/priyanka-and-toys/problem
"""

def toys(w):
    w.sort()
    limit = w[0] + 4
    container_count = 1

    for item in w:
        if item > limit:
            container_count += 1
            limit = item + 4
    
    return container_count