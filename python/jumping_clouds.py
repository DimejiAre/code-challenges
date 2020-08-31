"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Basically avoid the 1's, you can move maximum of 2 steps
"""
def jumpingOnClouds(c):
    index = 0
    steps = 0
    while index < len(c) - 1:
        if index+2 < len(c) and c[index + 2] == 0:
            index += 2
            steps += 1
        elif index+1 < len(c):
            index += 1
            steps += 1

    return steps

print(jumpingOnClouds([0,0,1,0,0,1,0]))