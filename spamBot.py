import pyautogui
import time

# message to repeatedly type
message = ""
# seconds to wait so the text is entered at the right position
time.sleep(10)

# number (+1) of messages to send
for x in range(11):
	pyautogui.typewrite( message )
	pyautogui.press( 'enter' )
	# time to wait between each message
	time.sleep(1)