#----------------------------------------
#
# Create file named by date of today
# by Gennadiy
#
#-----------------------------------------

import datetime

dateToday = datetime.date.today()
fileName = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
fileDir = 'tmp/'+fileName
print("Date today: " + str(dateToday))
print(fileDir)


myfile = open(fileDir, mode='w', encoding='latin_1')
#myfile.write()
myfile.close()