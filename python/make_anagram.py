"""
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

"""

def makeAnagram(a, b):
    a_count = {}
    b_count = {}
    removed_characters = 0

    for letter in a:
        if letter in a_count:
            a_count[letter] += 1
        else:
            a_count[letter] = 1

    for letter in b:
        if letter in b_count:
            b_count[letter] += 1 
        else:
            b_count[letter] = 1
    
    for key in a_count.keys():
        if key in b_count:
            difference = abs(a_count[key] - b_count[key])
            removed_characters += difference
        else:
            removed_characters += a_count[key]
    
    for key in b_count.keys():
        if key not in a_count:
            removed_characters += b_count[key]
    
    return removed_characters

print(makeAnagram("fcrxzwscanmligyxyvym","jxwtrhvujlmrpdoqbisbwhmgpmeoke")) #30
