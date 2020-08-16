"""
https://www.hackerrank.com/challenges/angry-professor/problem
"""

def angryProfessor(k, a):
    a.sort()
    early_count = 0

    for i in a:
        if i <= 0:
            early_count += 1
        else:
            break

    answer = 'NO' if early_count >=k else 'YES'
    return answer

