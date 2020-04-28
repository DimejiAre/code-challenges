#codewars

'''
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

Examples
ips_between("10.0.0.0", "10.0.0.50")  ==   50 
ips_between("10.0.0.0", "10.0.1.0")   ==  256 
ips_between("20.0.0.10", "20.0.1.0")  ==  246
'''

def ips_between(start, end):
    start = start.split('.')
    end = end.split('.')
    difference = [None] * 4
    
    octet_value = 16777216
    
    for i in range(4):
        difference[i] = (int(end[i]) - int(start[i])) * octet_value
        octet_value /= 256
    
    return sum(difference)