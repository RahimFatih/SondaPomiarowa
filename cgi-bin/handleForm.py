#!/usr/bin/env python3
import cgitb
import random
import cgi
cgitb.enable() # Will catch tracebacks and errors for you. Comment it out if you no-longer need it.

if __name__ == '__main__':
    form = cgi.FieldStorage()
    f = open("devices.txt", "a")
    f.write("\n"+form.getvalue('sname')+","+form.getvalue('sType')+","+form.getvalue('sType')+","+form.getvalue('pin_number'))
    f.close()
    print ("Content-type:text/html\r\n\r\n")
    print ('<html>')
    print ('<head>')
    print('<style>')
    print('body {background-color: black;}')
    print('</style>')
    print("""<meta http-equiv="refresh" content="0; URL='http://172.23.114.67:8000'" />""")
    print ('</head>')
    print ('<body background-color="red">')
    print ('Sensor added, redirect to main page')
    print ('</body>')
    print ('</html>')
