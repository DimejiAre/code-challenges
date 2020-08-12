"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""

def checkMagazine(magazine, note):
    word_count = {}
    pair_count = 0

    for word in magazine:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    for word in note:
        if word in word_count:
            word_count[word] += 1
            if word_count[word] % 2 == 0:
                pair_count += 1
                del word_count[word]
        else:
            word_count[word] = 1
    
    print(pair_count, len(note))
    if pair_count == len(note):
        print('Yes')
    else:
        print('No')

print(checkMagazine(["apgo", "clm", "w", "lxkvg", "mwz", "elo", "bg", "elo", "lxkvg", "elo", "apgo", "apgo", "w", "elo", "bg"],["elo", "lxkvg", "bg", "mwz", "clm", "w",]))