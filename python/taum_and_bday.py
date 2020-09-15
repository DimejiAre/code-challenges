"""
https://www.hackerrank.com/challenges/taum-and-bday/problem
"""

def taumBday(b, w, bc, wc, z):
    if (bc + z) < wc:
        return (b * bc) + (w * bc) + (z * w)
    elif (wc + z) < bc:
        return (b * wc) + (w * wc) + (z * b)
    else:
        return (b * bc) + (w * wc)