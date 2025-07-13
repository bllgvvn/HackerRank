# Given a year, determine whether it is a leap year.
# If it is a leap year, return the boolean True, otherwise return False.
# Three conditions determine whether a year is a leap year:
# 1. The year can be evenly divided by 4, is not a century year
# 2. The year can be evenly divided by 100, is not a leap year
# 3. The year can be evenly divided by 400, is a leap year  

def leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
year = int(input("Enter a year: "))
print("Is the year a leap year?", leap_year(year))