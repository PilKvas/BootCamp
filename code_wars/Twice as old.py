"""Your function takes two arguments:

1. current father's age (years)
2. current age of his son (years)
Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).

"""

def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - (son_years_old * 2))