#!/usr/bin/python3
import cgitb
cgitb.enable()
print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print("""<meta http-equiv="refresh" content="0; URL='http://172.23.114.67:8000'" />""")
print ('<title>Hello World - First CGI Program</title>')
print ('</head>')
print ('<body>')
print ('Sensor added, redirect to main page')
print ('</body>')
print ('</html>')