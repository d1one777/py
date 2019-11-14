print (">>> Welcome to Blinchik project<<<")
name = "...jocker..."
name = name.title()
print(name.strip("."))
star = ""

for x in range (0,5):
    star = star + "*"
    print(star)


for x in range (0,5):
    print(star)
    star = star[:-1]


