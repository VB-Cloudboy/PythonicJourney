from datetime import date

date.today
print(date.today())
print("Today's date is: " + str(date.today()))

# converting parsecs to lightyears. One parsec is 3.26 lightyears, 
# so you will multiply parsecs by that value to determine lightyears.

parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")