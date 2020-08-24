"""
https://www.hackerrank.com/challenges/flatland-space-stations/problem
"""
# not passing all tests, times out

def flatlandSpaceStations(n, c):

    max_distance = 0
    for city in range(n):
        distance = abs(city - c[0])
        for station in c:
            distance = min( abs(city - station), distance)
        max_distance = max(max_distance, distance)
    
    return max_distance