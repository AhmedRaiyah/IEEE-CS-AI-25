day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

day += 7
if(day > 30):
    day -= 30
    month += 1
if(month > 12):
    month -= 12
    year += 1

print(f"Day: {day}, Month: {month}, Year: {year}")