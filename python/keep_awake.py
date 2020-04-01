import keyword
import time

print("Keeping computer awake. Send keyboard interrupt to stop program")
while True:
	keyword.send('numlock')
	keyword.send('numlock')
	time.sleep(10)