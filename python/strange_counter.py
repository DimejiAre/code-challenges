"""
https://www.hackerrank.com/challenges/strange-code/problem
"""

def strangeCounter(t):
    start_num = 1
    block_size = 3

    while start_num <= t:
        diff = t - start_num
        value = block_size - diff
        start_num += block_size
        block_size *= 2

    return value