Prerequisites

You need to have the pynput library installed. You can install it using pip:

pip install pynput

How the Script Works

Importing keyboard from pynput: This module is used to capture keyboard events.

on_press function: Logs every key that is pressed. For normal characters, it logs the character directly. For special keys like Enter, Space, or Esc, it logs the name of the key.

on_release function: Stops the keylogger if the Esc key is pressed.

Listener: The keyboard.Listener listens to keyboard events and calls the on_press and on_release functions.
Ethical Considerations

Permission: Always get explicit permission from the owner of the device before running a keylogger.

Transparency: Clearly communicate to the user that a keylogger is being used, what it will log, and how the data will be handled.

Security: Securely handle and store any logged data to prevent unauthorized access.


Running the Script
To run the script, save it as keylogger.py and execute it:

python keylogger.py

The script will run in the background, logging keystrokes to keylog.txt. To stop the keylogger, press the Esc key.

Disclaimer: Use this script responsibly and only in environments where it is legal and ethical to do so.
