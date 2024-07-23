# Write your solution here
import datetime
day = int(input('Day: '))
month = int(input('Month: '))
year = int(input('Year: '))
dob = datetime.datetime(year, month, day)
mil = datetime.datetime(1999, 12, 31)
diff = mil - dob
if diff.days > 0:
    print(f'You were {diff.days} days old on the eve of the new millennium.')
else:
    print("You weren't born yet on the eve of the new millennium.")