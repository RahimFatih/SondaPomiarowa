import re


def readFromSensor(sensorType, id):
    if(sensorType=='DS18B20'):
        try:
            file = open('/sys/bus/w1/devices/' + id + "/w1_slave", "r")
            line = file.readline()
            if re.search('YES', line).group(0) == "YES":
                myTemp = re.search("(?<=t=)\d+", file.readline()).group(0)
            else:
                myTemp = 999998
            file.close()
            return int(myTemp)
        except:
            return 999999
