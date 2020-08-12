"""
https://www.hackerrank.com/challenges/picking-numbers/problem
"""

def pickingNumbers(a):
    a.sort()

    start_num = a[0]
    sub_arr = [start_num]
    big_arr = []

    for i in range(1,len(a)):
        if a[i] - start_num <= 1:
            sub_arr.append(a[i])
        else:
            big_arr.append(sub_arr)
            start_num = a[i]
            sub_arr = [start_num]
    
    if len(big_arr) == 0:
        return len(sub_arr)
    
    longest = 0
    for arr in big_arr:
        longest = max(len(arr), longest)
    
    return longest