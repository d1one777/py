#Input - Output IO
import datetime

name = input("Your first name: ")
name = name.title()
print(name)

month = input("month (format XX): ")
year = input("year (format XXXX): ")

print(month + " " + year)
realdate = datetime.date.today()
print(realdate.month, realdate.year )