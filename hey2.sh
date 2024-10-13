#!/bin/bash

# Function to click at a random location from a given array
click_random() {
  local locations=("$@")
  local random_location=${locations[$RANDOM % ${#locations[@]}]}
  xdotool mousemove $random_location click 1
}

# Function to generate a random name of 6 to 9 alphabetic characters
generate_random_name() {
  local length=$((6 + RANDOM % 4))  # Random length between 6 and 9
  tr -dc 'a-z' < /dev/urandom | head -c "$length"
}

# Function to generate a random email address
generate_random_email() {
  local name=$(generate_random_name)
  local domain=$((RANDOM % 2))  # Randomly choose between 0 and 1
  if [ "$domain" -eq 0 ]; then
    echo "${name}@gmail.com"
  else
    echo "${name}@outlook.com"
  fi
}
sleep 3
xdotool mousemove 295 85 click 1
sleep 3

# Step 1: Click randomly on one of the locations from the new set
click_random "423 545" "448 539" "478 540" "512 541" "551 541" "581 542" "612 543" "651 543" "684 543" "723 542" "752 544"
sleep 1

# Step 2: Generate a random email and type it
random_email=$(generate_random_email)
xdotool type "$random_email"
sleep 1
xdotool key Return
sleep 5
xdotool key Return
sleep 8
# Step 3: Click at (x:210, y:409) and press Down arrow 4 times
xdotool mousemove 555 179 click 1
sleep 2
xdotool mousemove 1337 127 click 1
sleep 2
xdotool mousemove 210 409 click 1
sleep 1
for i in {1..4}; do
  xdotool key Down
  sleep 1
done
sleep 5
# Step 4: Click randomly on one of the new locations from the next set
click_random "616 554" "641 562" "669 563" "686 566" "703 567" "724 567" "738 569" "682 572" "660 572"
sleep 4

# Step 5: Click at (x:245, y:364) and press Down arrow 4 times
xdotool mousemove 245 364 click 1
sleep 2
for i in {1..3}; do
  xdotool key Down
  sleep 1
done
sleep 3
# Step 6: Click randomly on one of the locations from the last set
click_random "665 544" "675 542" "690 543" "702 541" "709 545"

# Step 7: Click at (x:558, y:181) and (x:217, y:377) with up arrow presses
xdotool mousemove 558 181 click 1
sleep 2
xdotool mousemove 217 377 click 1
sleep 2
for i in {1..2}; do
  xdotool key Up
  sleep 1
done
sleep 2


# Step 8: Click randomly on the specified new locations
xdotool mousemove 258 264 click 1

sleep 5

# Step 9: Click at (x:238, y:515) and sleep for 5 seconds
xdotool mousemove 238 515 click 1
sleep 5

# Step 10: Click randomly on another set of specified locations
click_random "280 396" "334 391" "388 399" "433 394" "469 392" "503 399" 
sleep 5

# Step 11: Click randomly on the final specified locations
click_random "88 177" "102 180" "113 177" "127 178" "136 179" "144 179" 
sleep 5

# Step 12: Finally click at (x:290, y:43)
xdotool mousemove 290 43 click 1

