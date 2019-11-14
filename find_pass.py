#----
# pass search in file
#-----

#dirnamefile = "names.txt"
dirpassfile = "rockyou.txt"

#namefile = open(dirnamefile, mode='r', encoding='latin_1')
passfile = open(dirpassfile, mode='r', encoding='latin_1')

#print(namefile.read())

for num, line in enumerate(passfile, 1):
    if "fc23" in line :
        print(str(num) + line.strip() )