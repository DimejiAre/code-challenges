"""
https://www.hackerrank.com/challenges/the-grid-search/problem
"""

def gridSearch(G, P):
    p_start = P[0][0]
    p_row_length = len(P)
    p_col_length = len(P[0])
    for row in range(len(G) - p_row_length + 1):
        for col in range(len(G[row]) - p_col_length + 1):
            if G[row][col] == p_start:
                g_pattern = G[row][col:col + p_col_length]
                if g_pattern == P[0]:
                    for i in range(1,len(P)):
                        if G[row + i][col:col + p_col_length] != P[i]:
                            break
                        if i == len(P) - 1:
                            return 'YES'
    return 'NO'