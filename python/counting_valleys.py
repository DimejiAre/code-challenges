"""
Hackerank
Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

For example, if Gary's path is s=[DDUUUUDD], he first enters a valley 2 units deep. Then he climbs out an up onto a mountain 2 units high. Finally, he returns to sea level and ends his hike.

Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed.

https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen
"""

def countingValleys(n, s):
    #[UDDDUDUU]
    path = []
    level = 0
    valley_count = 0

    for i in s:
        path.append(i)
        if i == 'U':
            level += 1
        else:
            level -= 1
        if level == 0:
            if path[0] == 'D':
                valley_count += 1
            path = []
    
    return valley_count

print(countingValleys(8,['U','D','D','D','U','D','U','U']))