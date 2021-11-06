import json
import SensorReader

print("Temp : " + '{:.3f}'.format(
    SensorReader.readFromSensor('DS18B20', '28-00000d635f25') / float(1000)))

data = {}
data['devices'] = []



with open('devices.txt', 'r') as devicesConf:
    for singleDevice in devicesConf.readlines():
        deviceAtrributes = singleDevice.split(',')
        data['devices'].append({
            'name': deviceAtrributes[0],
            'type': deviceAtrributes[1],
            'adres': deviceAtrributes[2],
            'measurment': SensorReader.readFromSensor(deviceAtrributes[1], deviceAtrributes[2]) / float(1000)
        })
        
with open('devicesStatus.json', 'w') as outfile:
    json.dump(data, outfile)