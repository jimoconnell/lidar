import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)

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
print 'Starting Lidar'
input=1
while 1 :
		#Take a reading every one second:
		time.sleep(1)
		# send the character to the device
		# Sending "D" to the device will hopefully tell it to take a measurement and return the value. (\r\n\ is added to send)
		ser.write('D\r\n')
		out = ''
		# let's wait one second before reading output (let's give device time to answer)
		while ser.inWaiting() > 0:
			out += ser.read(1)
			
		if out != '':
			print "" + out

