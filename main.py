import pyxhook
import time
import math

timer = None
last_press = None
total_time = 0
total_words = 0
current_time = 0
current_words = 0

def OnKeyPress(event):
	global timer
	global last_press
	global total_time
	global total_words
	global current_time
	global current_words

	if event.Ascii > 32 and event.Ascii < 122:
		if timer is None:
			timer = time.time()
			last_press = time.time()
		elif time.time() - last_press <= 1:
			last_press = time.time() #Reset timer
		else:
			wpm = (current_words * 60) / current_time
			avg_wpm = (total_words * 60) / total_time
			print(f"Typed {current_words} word(s) in {current_time:.2f} seconds.")
			print(f"{wpm:.2f} WPM.")
			print(f"Avg: {avg_wpm:.2f} WPM.")
			# Reset word count
			current_words = 0
			timer = None
	elif (event.Key == "Return" or chr(event.Ascii) == ' ') and timer is not None:
		# Calculate wpm
		current_words += 1
		if timer is not None:
			# Calculate WPM every time a space or enter is pressed
			current_time = time.time() - timer
			total_time += current_time
			total_words += current_words
		if current_words == int(math.sqrt(current_words)) ** 2: # perfect square
			wpm = (current_words * 60) / current_time
			avg_wpm = (total_words * 60) / total_time
			print(f"Typed {current_words} word(s) in {current_time:.2f} seconds.")
			print(f"{wpm:.2f} WPM.")
			print(f"Avg: {avg_wpm:.2f} WPM.")

h = pyxhook.HookManager()
h.KeyDown = OnKeyPress
h.HookKeyboard()
h.start()