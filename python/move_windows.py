import ctypes
import win32gui
import sys

M_X = 0 # monitor x position index
M_Y = 1 # monitor y position index
W_W = 2 # window width index
W_H = 3 # window height index

config = {
	'Intellij': (-100, -1000, 1500, 850),
	'SQL Developer': (1800, -1000, 1500, 850),
	'Command Prompt': (2700, -800, 800, 500),
	'Vivaldi': (0, 0, 1400, 1000),
	'Outlook': (0, 0, 1400, 1000),
	'fish': (1700, -700, 800, 500),
	'SingleMonitorConfig': (0, 0, 800, 800)
}

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

titles = []

def foreach_window(hwnd):
	if IsWindowVisible(hwnd):
		length = GetWindowTextLength(hwnd)
		buff = ctypes.create_unicode_buffer(length + 1)
		GetWindowText(hwnd, buff, length + 1)
		titles.append(buff.value)
	return True

def get_handle(window_title):
	return wind32gui.FindWindow(None, window_title)

def move_window(hwnd, config_tuple):
	win32gui.MoveWindow(hwnd, config_tuple[M_X], config_tuple[M_Y], config_tuple[W_W], config_tuple[W_H], True)

def init_titles():
	EnumWindows(EnumWindowsProc(foreach_window), 0)

def maximize(hwnd):
	ctypes.WinDLL('user32').ShowWindow(hwnd, 3) # 3 is maximize const

def move_windows(is_multi_monitor):
	for key in config:
		for title in titles:
			if key in title:
				hwnd = get_handle(title)
				window_config = config[key] if is_multi_monitor else config['SingleMonitorConfig']

if __name__ == '__main__':
	init_titles()
	if len(sys.argv) == 1 or sys.argv[1] == 'one':
		move_windows(is_multi_monitor=False)
	else:
		move_windows(is_multi_monitor=True)
		move_windows(is_multi_monitor=True) # 2nd run properly resizes on new monitor