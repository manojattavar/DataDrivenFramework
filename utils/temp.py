import _datetime as dt

closingDate = '04-01-2023'
format = dt.datetime.strptime(closingDate, '%d-%m-%Y')

year = format.year
month = format.month
day = format.day

desiredMonth = format.strftime('%b')

print(desiredMonth)

print(str(desiredMonth) + " " + str(day) + ", " + str(year))