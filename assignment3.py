def yearDifference(year1, year2):
    
    if year1 > year2:
        difference = year1 - year2
    else:
        difference = year2 - year1
    return difference

year1 = int(input("year1: "))
year2 = int(input("year2: "))

difference = yearDifference(year1, year2)

print("Year 1: ")
print("Year 2: ")
print("difference: ")
