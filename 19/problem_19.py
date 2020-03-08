"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
def main():
    print(sundays(1901, 2000))

def sundays(start, end):
    count = 0
    for year in range(start, end + 1):
        for month in range(1, 13):
            if zellers(1, month, year) == 1:
                count += 1
    return count

# Zeller's congruence
def zellers(day, month, year):
    if month in (1,2):
        year -= 1
    return (day + ((13 * (month + 1)) // 5) + year + (year // 4) + 5) % 7

if __name__ == '__main__':
    main()