#!/usr/bin/python
import serial
import MySQLdb as mdb
ser = serial.Serial('/dev/ttyUSB0',2400,timeout=1)
line=ser.readline()
line=ser.readline()
line=line.strip()
tempC=line.split(" ")[1]
tempF=(float(tempC)*(9.0/5.0))+32
tempstr="{:.2f}".format(tempF)
ser.close()

con = mdb.connect('localhost','iot','','iot');

with con:
	cur=con.cursor()
	cur.execute("INSERT INTO TempMeter2(Temperature) VALUES("+tempstr+")")
