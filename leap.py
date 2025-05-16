year=int(input())
if year %100 and year%400 or year %4:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")