import pyautogui

a=pyautogui.position()
print(a)


#(x=899, y=1042)  for brave browser
#Point(x=956, y=1051) for whatsapp
# full screen Point(x=1513, y=49)
#Point(x=369, y=276) for myself chat
# select from Point(x=687, y=135) to Point(x=1887, y=916)

import pyperclip
import time

# Safety pause - move mouse to corner to abort
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True  # Move mouse to top-left corner to abort

print("Starting in 3 seconds... Move mouse to TOP-LEFT corner to abort!")
time.sleep(3)

# Step 1: Click WhatsApp
print("Step 1: Clicking WhatsApp...")
pyautogui.click(x=956, y=1051)
time.sleep(2)

# Step 2: Click Full Screen
print("Step 2: Going Full Screen...")
pyautogui.click(x=1513, y=49)
time.sleep(1)

# Step 3: Click on 'Myself' chat
print("Step 3: Selecting chat...")
pyautogui.click(x=369, y=276)
time.sleep(1.5)

# Step 4: Click and drag to select text
print("Step 4: Selecting text via click and drag...")
pyautogui.moveTo(x=687, y=135)
time.sleep(0.3)
pyautogui.mouseDown()
time.sleep(0.2)
pyautogui.moveTo(x=1887, y=916, duration=1.0)
pyautogui.mouseUp()
time.sleep(0.5)

# Step 5: Copy selected text to clipboard
print("Step 5: Copying to clipboard...")
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 6: Get and display clipboard content
text = pyperclip.paste()
print("\n--- Copied Text ---")
print(text)
print("-------------------")
print(f"\nTotal characters copied: {len(text)}")