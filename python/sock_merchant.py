"""
Hackerank
Count the number of pairs of socks. Passed in as an array, each number represents a color of socks.

https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""

def sock_merchant(ar):
    count_dict = {}
    pair_count = 0
    for i in ar:
        if i in count_dict.keys():
            count_dict[i] += 1
            if count_dict[i] == 2:
                pair_count += 1
                count_dict[i] = 0
        else:
            count_dict[i] = 1
    
    return pair_count

print(sock_merchant([10,10,10,20,30,20,30,20]))