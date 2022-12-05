import _datetime as dt

def temp(closingDate):
    formatted = dt.datetime.strptime(closingDate, "%d-%m-%Y")
    year = formatted.year
    month = formatted.month
    day = formatted.day

    formatted_month = formatted.strftime('%b')

    date = str(formatted_month) + ' ' + str(day) + ', ' + str(year)
    print(date)

temp("05-12-2022")