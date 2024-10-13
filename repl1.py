import pyautogui
import time
import random
import string

# Function to type text like a human
def type_like_human(text):
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(0.05, 0.2))  # Random delay between each keystroke

# Function to generate a random name of 6 to 8 alphabetic characters
def generate_random_name():
    length = random.randint(6, 8)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# Function to generate a random password of 9 to 12 characters
def generate_random_password():
    length = random.randint(9, 12)
    characters = string.ascii_letters + string.digits + "@$./;!"
    return ''.join(random.choice(characters) for _ in range(length))

# Step 1: Click on (x:307, y:82)
pyautogui.click(307, 82)
time.sleep(1)

# Step 2: Type 'replit.com' and press Enter
type_like_human('replit.com')
time.sleep(1)
pyautogui.press('enter')
time.sleep(8)

# Step 3: Click on (x:306, y:362)
pyautogui.click(306, 362)
time.sleep(2)

# Step 4: Press the down arrow key 2 times with 1 second delay between each press
for _ in range(2):
    pyautogui.press('down')
    time.sleep(1)

# Step 5: Click randomly on one of the first set of locations
click_locations_1 = [(489, 516), (517, 518), (549, 514), (581, 517), (597, 525), (612, 518), (618, 524)]
random_location_1 = random.choice(click_locations_1)
pyautogui.click(random_location_1)
time.sleep(8)

# Step 6: Click randomly on the second set of locations
click_locations_2 = [(861, 433), (899, 433), (940, 431), (978, 436), (1038, 437), (1091, 434)]
random_location_2 = random.choice(click_locations_2)
pyautogui.click(random_location_2)
time.sleep(2)

# Step 7: Press Ctrl + V to paste
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Step 8: Type '@hey.com' like a human
type_like_human('@hey.com')
time.sleep(2)

# Step 9: Press Tab
pyautogui.press('tab')

# Step 10: Type a random password
random_password = generate_random_password()
type_like_human(random_password)
time.sleep(2)

# Step 11: Click randomly on the third set of locations
click_locations_3 = [(866, 562), (885, 560), (910, 561), (929, 560), (950, 559), (972, 559), 
                     (999, 561), (1021, 559), (1050, 556), (1071, 559), (1102, 561), (1126, 559)]
random_location_3 = random.choice(click_locations_3)
pyautogui.click(random_location_3)
time.sleep(15)

# Step 12: Click randomly on the fourth set of locations
click_locations_4 = [(960, 557), (969, 557), (982, 556), (995, 558), (1009, 554), (1015, 555)]
random_location_4 = random.choice(click_locations_4)
pyautogui.click(random_location_4)
time.sleep(2)

# Step 13: Click randomly on the fifth set of locations
click_locations_5 = [(341, 329), (365, 331), (398, 331), (426, 331), (470, 331), (513, 329), (541, 328)]
random_location_5 = random.choice(click_locations_5)
pyautogui.click(random_location_5)
time.sleep(1)

# Step 14: Type a random name (6 to 8 characters), press Tab, then another random name
random_name_1 = generate_random_name()
type_like_human(random_name_1)
time.sleep(1)
pyautogui.press('tab')

random_name_2 = generate_random_name()
type_like_human(random_name_2)
time.sleep(1)

# Step 15: Click randomly on the sixth set of locations
click_locations_6 = [(653, 416), (700, 418), (747, 416), (761, 415), (863, 413), 
                     (910, 416), (944, 415), (982, 417), (916, 414)]
random_location_6 = random.choice(click_locations_6)
pyautogui.click(random_location_6)
time.sleep(1)

# Step 16: Click randomly on the seventh set of locations
click_locations_7 = [(581, 513), (608, 515), (634, 511), (736, 515), (768, 511), 
                     (805, 510), (829, 511), (894, 516), (933, 512), (956, 513), (980, 509)]
random_location_7 = random.choice(click_locations_7)
pyautogui.click(random_location_7)
time.sleep(2)

# Step 17: Click on (x:992, y:565)
pyautogui.click(992, 565)
time.sleep(1)

# Step 18: Click randomly on the eighth set of locations
click_locations_8 = [(361, 537), (389, 541), (403, 542), (426, 543), (453, 542), 
                     (479, 542), (500, 540), (517, 537)]
random_location_8 = random.choice(click_locations_8)
pyautogui.click(random_location_8)
time.sleep(3)

# Step 19: Finally, click on (x:134, y:41)
pyautogui.click(134, 41)
