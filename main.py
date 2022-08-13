import mydatabase as md
import mydashboard as mdb
import mydataacquisition as dac
import time

def current_milli_time():
    return round(time.time() * 1000)

lastVal = 0
newVal = 0

readCSV = dac.dataAcquisition('dummy_data.csv')
dataDist = readCSV.sensorData('distance')
#dataThetaBall = readCSV.sensorData('theta_ball')

x = md.database('localhost','root','mypass')
# average filter to clean data noise
for x in range(len(dataDist)):
    if dataDist[x][1] > 50:
        dataDist[x][1] = 0
    elif dataDist[x][1] < 0:
        dataDist[x][1] = 0
    else:
        dataDist[x][1] = dataDist[x][1]
    lastVal = dataDist[x][1]
    newVal = lastVal + newVal
AverageFilter = newVal / len(dataDist)

"""
# Database edit
y = dac.dataAcquisition('dummy_data.csv')
data = y.sensorData('theta_ball')
#x.createDB("database_baru")
#x.createTableDB('database_baru', 'dummy_dat', 'Id', 'name', 'value', 'detection')
#x.insertDataDBNew('database_baru', 'dummy_dat', 'name', 'value', 'detection', data)
#x.insertDataDBIfNotExists('database_baru', 'dummy_dat', 'name', 'value', 'detection', data)
#x.updateTableDB('database_baru', 'dummy_dat', 'name', 'name', 'human_detection', 'robot_detection')
#x.deleteTableDB('database_baru', 'dummy_dat')
print(x.readDB('database_baru', 'dummy_dat'))
"""

# open dashboard
mydatabase = x.connectDB('database_baru')
mycon = mdb.dashboard('dummy_dat', cnxn=mydatabase)
myNew = mycon.selectData('name', 'value', 'detection')

