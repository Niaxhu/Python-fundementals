#Given a list of birth years, calculate each person's age in a given reference year (e.g. 2025)
#Input: a list of birth years,Give reference year: e.g. 2025, Process: age = reference_year - birth_year, for each year,Output: a list of ages

current_year = 2025
years = [1995, 2001, 1988, 2010, 1975]

#method 1
#ages = []

#for y in years:
    #ages.append(current_year - y)

#print(ages)


#method 2
ages = [current_year - y for y in years]

print(ages)