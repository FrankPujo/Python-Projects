# HOW TO USE:
# run the python script from the cmd
# choose the mod to use
# you will have a certain amount of time to move the cursor to the right input box
# (the boxes where you type the messages)
# then the loop will start typing and entering the messages

import pyautogui
import time

# message to repeatedly type and send
message = ""
# seconds to wait so the text is entered in the right input box
time.sleep(12)

# to send messages with the same contetn multiple times
def singleWord():
	# number (+1) of messages to send
	for x in range(11):
		pyautogui.typewrite( message )
		pyautogui.press( 'enter' )
		# time to wait between each message
		time.sleep(1)

# to send messages with different words (dividing a big text file in lines)
def multipleWords():
	for word in message:
		pyautogui.typewrite( word )
		pyautogui.press( 'enter' )
		#time to wait between each message-word

mod = input( "Choose the mode [single/multiple]: " )
if mod == "single":
	singleWord()
elif mod == "multiple":
	multipleWords()