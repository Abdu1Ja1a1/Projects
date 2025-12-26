# Keyboard Input Logger (pynput)

## Overview
This repository contains a small Python script that listens for keyboard press events using `pynput` and appends typed characters to a local file

## Legal / Ethical Warning
Only run this script on systems you own or have explicit permission to monitor
Unauthorized monitoring of keyboard input may be illegal and unethical

## What it does
- Listens for **key press** events
- Prints each key event to the terminal
- Appends **character keys** (e.g., `a`, `b`, `1`) to `keyfile.txt`
- Ignores non-character keys (e.g., Shift, Ctrl, Enter) and prints an error message for those

## Files
- `keylogger.py` (or your script filename): main script
- `keyfile.txt`: created automatically when keys are pressed while the script is running

## Requirements
- Python 3.x
- `pynput`

Install dependency:
```bash
python -m pip install pynput
```

## Usage
Run the script:
```bash
python keylogger.py
```

While the script is running:
- Key presses are printed to the console
- Character keys are appended to `keyfile.txt`

To stop the script:
- Close the terminal window or
- Press `Ctrl + C`

## License
MIT

