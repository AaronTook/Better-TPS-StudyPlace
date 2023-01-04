# Better-TPS-StudyPlace
A Mouse and Keyboard automation script for improving the appearance of the TPS Student StudyPlace Website.

This project, specifically designed for personal use or adaptation by other students at TPS (https://at-tps.org),is a simple Python automation script to improve the user's experience with StudyPlace by allowing them to customize their background using an image from the internet.

--------------------------------
Project Requirements:
 1.  Must have Al Sweigart's module "pyautogui" installed (https://pyautogui.readthedocs.io/en/latest/install.html)
 2.  Must have Al Sweigart's module "pyperclip" installed (https://pypi.org/project/pyperclip/)
 3.  Must modify the data found in "preferences.txt"
 4.  Must replace "ChromeDevTools_Edit as HTML.png" and "ChromeDevTools_Elements Ellipsis.png" with equivalant screenshots from your Chrome Dev Tools.
 5.  Run on Windows device (due to pyautogui's locateCenterOnScreen function limitations)


Before first using the program, please enter your preferences into the file "preferences.txt" as follows:

Line 1: Complete URL to an easily accessible image you would like to use as your background.

Line 2: An integer value of a minimum of 3 seconds. Times less than 3 seconds will raise a prompt informing the user of potential program failures.

Line 3: An integer value of a minimum of 0.2 seconds. Times less than 0.2 seconds will raise a prompt informing the user of potential program failures.

Line 4: An integer value of a minimum of 0.2 seconds. Times less than 0.2 seconds will raise a prompt informing the user of potential program failures.

Run the program file from the command line, your IDE, or any other usual method.
After program starts, click into the TPS Student StudyPlace web page within the set amount of time for user intervention.
Please do not move the mouse or use the keyboard during the approximately 10-20 second runtime of the program. 
