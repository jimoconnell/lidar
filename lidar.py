import time
import serial
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")
mqttc.connect("mqtt.gasnet.io", 1883)
# configure the serial connections (the parameters differs on the device you are connecting to)
#Comment
ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=19200,
	parity=serial.PARITY_ODD,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

# ser.open()
ser.isOpen()

#print 'Enter your commands below.\r\nInsert "exit" to leave the application.'
print 'Starting Lidar\nReadings in meters.\n'
input=1
while 1 :
		#Take a reading every one second:
		time.sleep(5)
		# send the character to the device
		# Sending "D" to the device will hopefully tell it to take a measurement and return the value. (\r\n\ is added to send)
		ser.write('D\r\n')
		out = ''
		# let's wait one second before reading output (let's give device time to answer)
		while ser.inWaiting() > 0:
			out += ser.read(1)
			
		if out != '':
			print "" + out
		if out != 'D' and out != '' and 'Er' not in out:
			a,b = out.split(",")	
			a = a.translate(None,":")
			a = a.translate(None,"m")
			a = a.translate(None,"D")
			inches = float(a) / .3048 % 1 * 12
			#mqttc.publish("gasnet/lidar", inches)
			mqttc.publish("gasnet/lidar", a)
