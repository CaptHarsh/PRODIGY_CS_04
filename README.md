# Keylogger

This is a simple keylogger program written in Python using the `keyboard` library. It logs keystrokes and separates special keys from regular text in the output log file.

## Installation

1. Clone the repository:

   ```
   https://github.com/CaptHarsh/PRODIGY_CS_04.git
   ```

2. Install the required dependencies:

   ```
   pip install keyboard
   ```

## Usage

1. Run the keylogger.py script:

   ```
   python keylogger.py
   ```

2. Press keys on your keyboard. The program will log the keystrokes to a file called keylog.txt in the specified directory (`D:\Prodigy`).

3. To stop logging, press the 'esc' key.

## Notes

- Special keys (e.g., 'Shift', 'Ctrl') are logged as "[Special Key: {key}]".
- Regular text keys are logged as-is.
