import os
import keyboard
import time
import random
import sys

default_file = 'model_service.txt'

def random_type_delay():
	time.sleep(random.uniform(0.0, 0.5))

def random_pause():
	if random.randint(0, 100) < 1:
		print('Adding random pause - ' + str(time.time()))
		time.sleep(5)

def create_typing_source(file_name):
	to_type = []
	print('Reading from code file')
	with open(file_name) as f:
		for line in f:
			for char in line:
				to_type.append(char)
	print('Finished reading')
	return to_type

def write(to_type):
	print('Writing code')
	last_char = ' '
	is_annotation = False
	for char in to_type:
		random_pause()
		if char == '@':
			is_annotation = True
		random_type_delay()
		keyboard.write(char)
		if is_annotation and char == '\n': # handle autocomplete eating the newline
			keyboard.write('\n')
			is_annotation = False
		# add pause at new blocks to allow some more time to switch window focus and stop script
		if char == '\n' and last_char == '\n':
			print('Pausing to "think" - ' + str(time.time()))
			time.sleep(5)
		last_char = char

if __name__ == '__main__':
	file_name = sys.argv[1] if len(sys.argv) > 1 else default_file
	to_type = create_typing_source(file_name)
	print('You have 3 seconds to focus to the target window')
	time.sleep(1)
	print('2')
	time.sleep(1)
	print('1')
	time.sleep(1)
	while True:
		write(to_type)
		keyboard.send('ctrl+a')
		keyboard.send('del')