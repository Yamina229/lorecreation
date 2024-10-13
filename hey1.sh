#!/bin/bash

# Function to click at a random location from a given array
click_random() {
  local locations=("$@")
  local random_location=${locations[$RANDOM % ${#locations[@]}]}
  xdotool mousemove $random_location click 1
}

# Function to generate a random name of 5 to 8 alphabetic characters
generate_random_name() {
  local length=$((5 + RANDOM % 4))  # Random length between 5 and 8
  tr -dc 'a-z' < /dev/urandom | head -c "$length"
}

# Function to generate a random password of 12 to 15 characters
generate_random_password() {
  local length=$((12 + RANDOM % 4))  # Random length between 12 and 15
  tr -dc 'A-Za-z0-9@!:;,./=$' < /dev/urandom | head -c "$length"
}

# Step 1: Wait for 2 seconds
sleep 2

# Step 2: Move to location (x:384, y:83) and click
xdotool mousemove 384 83 click 1
sleep 1

# Step 3: Type "hey.com" and press Enter
xdotool type "hey.com"
xdotool key Return
sleep 3

# Step 4: Click randomly on one of the locations from the first set
click_random "1010 222" "1038 222" "1058 217" "1074 226" "1087 221" "1099 222" "1047 218" "1057 231"
sleep 12

# Step 5: Click randomly on one of the locations from the second set
click_random "581 533" "612 531" "634 534" "656 534" "692 534" "719 534" "744 537" "762 533" "773 532" "672 542"

# Step 6: Wait for 10 seconds
sleep 10

# Step 7: Click randomly on one of the locations from the third set
click_random "510 464" "542 470" "599 468" "642 470" "680 469" "721 472" "756 469" "816 472" "843 472" "669 475" "622 473" "621 473"

# Step 8: Generate a random name and save it to the clipboard
random_name=$(generate_random_name)
echo "$random_name" | xclip -selection clipboard

# Step 9: Type the random name and press Tab, then press Enter
xdotool type "$random_name"
sleep 2
xdotool mousemove 689 543 click 1

# Step 10: Wait for 6 seconds
sleep 6

# Step 11: Click randomly on one of the new locations
click_random "654 602" "671 604" "685 606" "701 605" "710 605" "717 604"
sleep 3

# Step 12: Generate a random password and type it
random_password=$(generate_random_password)
xdotool type "$random_password"
sleep 2

# Step 13: Click at (x:233, y:426)
xdotool mousemove 233 426 click 1
sleep 2

# Step 14: Press the down arrow key twice
for i in {1..2}; do
  xdotool key Down
  sleep 1
done

# Step 15: Click randomly on one of the locations from the next set
click_random "502 494" "547 497" "594 487" "648 497" "695 490" "757 484" "788 492" "821 492" "840 494"
sleep 1

# Step 16: Type the same random password again
xdotool type "$random_password"
sleep 1

# Step 17: Click randomly on one of the locations from the last set
click_random "652 565" "674 567" "699 566" "712 565" "687 578" "685 555"

# Step 18: Wait for 6 seconds
sleep 6
