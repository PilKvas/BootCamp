"""Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.

"""

def what_century(year):
    century = int(year) // 100 + 1
    century = str(century)
    
    if year[-3:] == "000" or year[-2:] == "00":
        if year[1::-3] == "3":
            return str(int(century) - 1)  + "rd"
        elif year[1::-3] == "2":
            return str(int(century) - 1)  + "nd"
        elif year[1::-3] == "1":
            return str(int(century) - 1)  + "st"
        else:
            return str(int(century) - 1) + "th" 
    elif century == "11" or century == "12" or century == "13":
        return century + "th"
    elif century[-1] == "1":
        return century + "st"
    elif century[-1] == "2":
        return century + "nd"
    elif century[-1] == "3":
        return century + "rd"
    else: return century + "th" 