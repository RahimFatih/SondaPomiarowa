import socket
import re
def readDS18B20(id):
    #try:
        file = open('/sys/bus/w1/devices/'+id+"/w1_slave","r")
        line= file.readline()
        if re.search('YES', line).group(0)=="YES":
            myTemp=re.search("(?<=t=)\d+",file.readline()).group(0)
        else:
            myTemp=999998
        file.close()
        return int(myTemp)
    #except:
    #    return 999999
def web_page(temp):
    html = b"""<html><head> <title>Pogodynka Komandorska</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>Pogodynka Komandorska</h1> 
  <p>Temperatura w salonie: <strong>""" + str(temp) 
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 3000))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    response = web_page('{:.1f}'.format(readDS18B20('28-00000d635f25')/float(1000)))
    conn.send(b'HTTP/1.1 200 OK\n')
    conn.send(b'Content-Type: text/html\n')
    conn.send(b'Connection: close\n\n')
    conn.sendall(response)
    conn.close()
