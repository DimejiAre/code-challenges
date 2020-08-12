"""
https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup
"""

def repeatedString(s, n):
    #find length of s
    #find number of a's in s
    # do integer division of n / len of s to get repitions
    # multiply a count by repitions
    # use remainder to slice s
    # count number of a's in sliced s
    # add number of a's in sliced s to original number of s
    string_length = len(s)
    a_count = 0
    for char in s:
        if char == 'a':
            a_count += 1

    repititions = n // string_length
    a_count *= repititions

    num_char_left = n % string_length
    string_left = s[:num_char_left]

    sub_a_count = 0
    for char in string_left:
        if char == 'a':
            sub_a_count += 1
    
    a_count += sub_a_count
    return a_count

print(repeatedString('abc',10))