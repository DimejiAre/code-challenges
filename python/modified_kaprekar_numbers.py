"""
https://www.hackerrank.com/challenges/kaprekar-numbers/problem
"""

def kaprekarNumbers(p, q):
    kaprekar = []
    for num in range(p,q + 1):
        square = str(num ** 2)
        num_len = len(str(num))
        new_nums = [square[:(len(square) - num_len)], square[- num_len :]]
        new_nums = [int(i) for i in new_nums if i.isdigit()]
        if sum(new_nums) == num:
            kaprekar.append(num)

    if len(kaprekar) == 0:
        print('INVALID RANGE')
    else:
        for i in kaprekar:
            print(i, end=' ')