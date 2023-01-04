import pyautogui, pyperclip, time, sys

class StudyPlaceImprover():
	""" Initiate the improveStudyPlace object, informing users of any potentially dangerous data values for the automation script. """
	def __init__(self):
		try:
			with open('preferences.txt') as preferencesFile: # Read the preferences from the appropriate file.
				preferences = preferencesFile.readlines()
				self.imageURL = preferences[0].strip()
				movementWaitDuration = float(preferences[1])
				movementLength = float(preferences[2])
				pauseBetween = float(preferences[3])
		except: # An issue was encountered due to missing or unacceptable values in the preferences file.
			pyautogui.alert(text='There is an issue with the "preferences.txt" file. \nPlease fix this before running the program again!', title='Error', button='ok') # Inform the user.
			sys.exit() # Exit the program.
		if movementWaitDuration < 3:  # The movementWaitDuration value is potentially too low.
			if pyautogui.confirm(text='The movementWaitDuration value is below the safety threshold  of 5 seconds. \nContinuing could cause unexpected and potentially damaging results.', title='Warning', buttons=['Accept Risk', 'Cancel']) == 'Cancel': # Inform the user.
				sys.exit() # Exit the program if "Cancel" is selected.
		if movementLength < 0.2: # The movementLength value is potentially too low.
			if pyautogui.confirm(text='The movementLength value is below its safety threshold of 0.5 seconds. \nContinuing could cause unexpected and potentially damaging results.', title='Warning', buttons=['Accept Risk', 'Cancel']) == 'Cancel': # Inform the user.
				sys.exit() # Exit the program if "Cancel" is selected.
		if pauseBetween < 0.2: # The pauseBetween value is potentially too low.
			if pyautogui.confirm(text='The pauseBetween value is below its safety threshold of 0.2 seconds. \nContinuing could cause unexpected and potentially damaging results.', title='Warning', buttons=['Accept Risk', 'Cancel']) == 'Cancel': # Inform the user.
				sys.exit() # Exit the program if "Cancel" is selected.
		self.movementWaitDuration = movementWaitDuration # Set the object variables
		self.movementLength = movementLength
		self.pauseBetween = pauseBetween

	def run(self):
		""" Simulate keypresses and mouse movements to gather manipulate and replace HTML in TPS StudyPlace to change the background to your desired picture """
		time.sleep(self.movementWaitDuration) # Give the user an opportunity to select the browser tab that has TPS StudyPlace open.
		startX, startY = pyautogui.position() # Gather the starting mouse position.
		startClipboard = pyperclip.paste() # Gatger the starting contents of the clipboard
		pyautogui.click() # Select the window.
		pyautogui.hotkey('fn','f12') # Open the Dev Tools.
		time.sleep(1)
		try:
			dotsX, dotsY = (pyautogui.locateCenterOnScreen('ChromeDevTools_Elements Ellipsis.png')) # Locate the Elements Ellipsis button in the Chrome Dev Tools.
		except:
			pyautogui.click() # Check again in case the Chrome Dev Tools were open at the start of the program.
			pyautogui.hotkey('fn','f12') # Open the Dev Tools.
			time.sleep(1)
			try:
				dotsX, dotsY = (pyautogui.locateCenterOnScreen('ChromeDevTools_Elements Ellipsis.png')) # Locate the Elements Ellipsis button in the Chrome Dev Tools.
			except: # There is an issue with the file.
				print("Check that you have a minimalistic, unobstructed and up-to-date image at \"ChromeDevTools_Edit as HTML.png\"")
				sys.exit() # Exit the program if "Cancel" to prevent program failure.
		pyautogui.moveTo(dotsX, dotsY, duration=self.movementLength) # Move to and click the Elements Ellipsis.
		pyautogui.click()
		time.sleep(self.pauseBetween)
		try:
			buttonX, buttonY = (pyautogui.locateCenterOnScreen('ChromeDevTools_Edit as HTML.png')) # Locate the "Edit as HTML" button in the Chrome Dev Tools.
		except: # Catch errors in which the image is not found.
			print("Check that you have a minimalistic, unobstructed and up-to-date image at \"ChromeDevTools_Edit as HTML.png\"")
			sys.exit()
		pyautogui.moveTo(buttonX, buttonY, duration=self.movementLength) # Move to and click "Edit as HTML".
		pyautogui.click()
		time.sleep(self.pauseBetween)
		pyautogui.hotkey('ctrl','a') # Select all the current HTML in the Chrome Dev Tools window.
		pyautogui.hotkey('ctrl','c') # Copy to the clipboard.
		page_html = pyperclip.paste() # Paste into a variable.
		page_html_as_list = page_html.split("><") # Change the HTML.
		page_html_as_list[0] = f"""<body id="ext-gen1018" class="x-body x-webkit x-chrome x-reset x-border-layout-ct x-container ux-desktop-black" style="background-repeat: no-repeat;background-size: cover;background-image: url('{self.imageURL}');z-index: -100">"""
		new_page_html = "><".join(page_html_as_list)
		pyperclip.copy(new_page_html)
		time.sleep(self.pauseBetween)
		pyautogui.hotkey('ctrl','v') # Replace the HTML in the Dev Tools
		pyautogui.moveTo(dotsX, dotsY+25, duration=self.movementLength) # Move and click out to update the background.
		pyautogui.click()
		time.sleep(self.pauseBetween)
		pyautogui.moveTo(startX, startY, duration=self.movementLength) # Return the mouse to the starting position.
		pyperclip.copy(startClipboard) # Reset the clipboard to its original contents.
		pyautogui.click()
		pyautogui.hotkey('fn','f12') # Close the Chrome Dev Tools. 
	def test(self):
		""" Run a test to measure how long it takes to execute the run() function """
		test_subject = improveStudyPlace() # Create a test object.
		startTime = time.time() # Record the test start time.
		test_subject.run() # Run the test.
		endTime = time.time() # Record the test end time. 
		timeElapsed = endTime-startTime # Calculate the full duration of the test.
		waitTime = (self.movementWaitDuration) + (self.pauseBetween * 4) + (self.movementLength * 4) + 1 # Calculate the amount of time spent by the necessary time.sleep() calls throughout the automation script.
		realTime = timeElapsed - waitTime # Calculate the amount of time actually spent by the automation script in action.
		print(f"----- Test Run -----\n >>  Total runtime: {round(timeElapsed,3)} sec\n >>  Wait & pause time: {round(waitTime, 3)} sec\n >>  Actual runtime: {round(realTime, 3)} sec") # Display the results to the user in the console.

if __name__ == "__main__":
	""" Create the object and run it """
	improver = StudyPlaceImprover()
	improver.run()

