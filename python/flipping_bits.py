"""
https://www.hackerrank.com/challenges/flipping-bits/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous
"""

def flippingBits(n):
    binary_string = '{0:032b}'.format(n)

    flipped_string = ""
    for i in binary_string:
        if i == '0':
            flipped_string += "1"
        else:
            flipped_string += '0'

    return (int(flipped_string, 2))