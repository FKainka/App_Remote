from machine import UART
import machine
from umqtt.simple import MQTTClient
import ubinascii

# Default MQTT server to connect to
SERVER = "192.168.178.76" #laura pi: 56, home: 76
#SERVER = socket.getaddrinfo("nodepi.local",8080)
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"serialwatch/output"


c = MQTTClient(CLIENT_ID, SERVER)
c.connect()
uart = UART(2, 57600)                         # init with given baudrate


while True:
    line = uart.readline()
    if line is not None:
        line.decode('utf-8')
        if len(line) > 2:
            print(line)
            c.publish(TOPIC,line)
