import subprocess
import pyautogui
import time
import os

# Step 1: Sleep for 3 seconds before starting
time.sleep(3)

# Path to the image of the mail button
mail_button_image = 'mail_button.png'

# Coordinates to click if the button is not detected
fallback_x, fallback_y = 96, 81

# Check if the image file exists
if not os.path.isfile(mail_button_image):
    print(f"Error: The image file '{mail_button_image}' does not exist.")
else:
    # Maximum number of detection attempts
    max_attempts = 1000

    for attempt in range(max_attempts):
        print(f"Attempt {attempt + 1} of {max_attempts}: Attempting to detect the mail button...")

        # Sleep for 4 seconds before each detection attempt
        time.sleep(4)

        # Attempt to locate the mail button
        button_location = None
        try:
            button_location = pyautogui.locateOnScreen(mail_button_image, confidence=0.8)
        except Exception as e:
            print(f"Error while detecting the mail button: {e}")

        # Check if the button is found
        if button_location:
            print(f"Mail button detected at {button_location}, clicking...")
            time.sleep(1)  # Wait before clicking
            pyautogui.click(button_location)  # Click the detected button
            print("Mail button clicked!")
            break  # Exit the loop after clicking the button

        # If the button is not found, click the fallback location
        print("Mail button not detected. Clicking fallback location...")
        # Use xdotool to click at the fallback location
        subprocess.run(['xdotool', 'mousemove', str(fallback_x), str(fallback_y), 'click', '1'])
        print(f"Clicked fallback location at ({fallback_x}, {fallback_y}).")

    else:
        print("Maximum detection attempts reached. Exiting...")

time.sleep(3)

# Step 2: Click on (x:614, y:454)
pyautogui.click(672, 510)
time.sleep(2)

# Step 3: Press the Tab key 3 times with 1 second delay between each press
for _ in range(3):
    pyautogui.press('tab')
    time.sleep(1)

# Step 4: Press the Enter key
pyautogui.press('enter')

# Step 5: Sleep for 8 seconds
time.sleep(15)
pyautogui.click(95, 84)
time.sleep(2)
pyautogui.click(703, 39)
time.sleep(1)
pyautogui.click(250, 42)
time.sleep(7)
