import pyxhook
import time

timer = None

last_press = None

total_time = 0
total_words = 0

def OnKeyPress(event):
	global timer
	global last_press
	global total_time
	global total_words

	if event.Ascii > 65 and event.Ascii < 122:
		if timer is None:
			timer = time.time()
			last_press = time.time()
		elif time.time() - last_press <= 1:
			last_press = time.time() #Reset timer
		else:
			#Reset word count
			words = 1
			timer = None
	elif (event.Key == "Return" or chr(event.Ascii) == ' ') and timer is not None:
		#Calculate wpm
		deltaT = time.time() - timer
		print("Typed 1 word in " + str(deltaT) + " seconds.")
		print(str(60 / deltaT) +  " wpm.")

		total_time += deltaT
		total_words += 1

		print("Avg: " + str(total_words * 60 / total_time))
		timer = None
 	

h = pyxhook.HookManager()
h.KeyDown = OnKeyPress
h.HookKeyboard()
h.start()
