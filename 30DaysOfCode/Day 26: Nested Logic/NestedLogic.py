# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import date

returned = list(map(int, input().split()))
expected = list(map(int, input().split()))

actual_date = date(day=returned[0], month =returned[1], year=returned[2])
expected_date = date(day=expected[0], month =expected[1], year=expected[2])

fine = 0

if actual_date > expected_date:
    if actual_date.year == expected_date.year:
        if actual_date.month == expected_date.month:
            fine = 15 * (actual_date.day - expected_date.day)
        else:
            fine = 500 * (actual_date.month - expected_date.month)

    else:
        fine = 10000

print (fine)
