"""The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.

"""

def century(year):
    century = year // 100 
    if year % 100 == 0:
        return century
    return century + 1