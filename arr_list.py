#array training
from typing import List

countries = ['ukraine','poland','hungary','slovakia']
print(countries)
num = len(countries)
print(num)
countries.sort(reverse=True)
print(countries)

for i in range(len(countries)):
    #print(i)
    countries[i] = countries[i].title()

print(countries)