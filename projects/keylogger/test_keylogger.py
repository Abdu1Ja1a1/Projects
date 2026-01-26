import sys
from datetime import datetime, timezone
from keylogger import KeyEvent, KeyType, keylogger
from pynput.keyboard import Key , KeyCode
import json
from tempfile import TemporaryDirectory
from pathlib import Path

class test_keylogger:

        def test_toggle(self):
                logger= keylogger()
                logger.recording = False
                logger.keyPressed(logger.toggle_key)
                assert logger.recording == True , "Toggle on has failed"

                logger.keyPressed(logger.toggle_key)
                assert logger.recording == False , "Toggle OFF has failed"

                print("Toggle test has PASSED")

        def test_key_event(self):
                now = datetime.now(timezone.utc)

                ev = KeyEvent(
                timestamp=now,
                key="a",
                window_title=None,
                key_type=KeyType.CHAR,
                )

                # Field checks
                assert ev.key == "a", "ev check has failed"
                assert ev.key_type is KeyType.CHAR,"ev check has failed"
                assert ev.timestamp == now,"ev check has failed"

                # Serialization
                data = ev.to_dict()
                assert data["key"] == "a","serialization check has failed"
                assert data["key_type"] == "char","serialization check has failed"
                assert "timestamp" in data,"serialization check has failed"

                # Human-readable format
                log_str = ev.to_log_string()
                assert "a" in log_str,"human-readable format check has failed"

                print("KeyEvent model test has PASSED")

        def test_datetime(self):
                logger = keylogger()
                ev = logger.build_event("ENTER", KeyType.SPECIAL)
                assert isinstance(ev.timestamp, datetime)
                assert ev.key == "ENTER"
                assert ev.key_type is KeyType.SPECIAL

                print("KeyEvent builder test has PASSED")

        def test_jsonl_written_when_recording(self):
                with TemporaryDirectory() as d:

                        log_path = Path(d) / "test_log.jsonl"

                        logger = keylogger()
                        logger.keyFile = str(log_path)
                        logger.recording = True

                        logger.keyPressed(Key.enter)

                        assert log_path.exists(),"file does not exist"

                        lines = log_path.read_text(encoding="utf-8").splitlines()
                
                        assert len(lines) == 1,"There is more than 1 line when there is meant to be one"
                        data = json.loads(lines[0])
                        assert data["key"] == "[ENTER]","incorrect key recorded"
                        assert data["key_type"] == "special","incorrect key type recorded"

                        print("json writing test has PASSED")
                        

        def test_keyPressed_last_event(self):
                logger = keylogger()
                logger.recording = True

                logger.keyPressed(Key.enter)

                assert logger.last_event.key == "[ENTER]","incorrect key recorded"
                assert logger.last_event.key_type is KeyType.SPECIAL,"incorrect key type recorded"
                print("last_event test has PASSED")
def run_tests():
        tests=test_keylogger()
        tests.test_toggle()
        tests.test_key_event()
        tests.test_datetime()
        tests.test_jsonl_written_when_recording()
        tests.test_keyPressed_last_event()
        print("ALL TESTS HAS PASSED")
        return 0

if __name__ == "__main__":
        sys.exit(run_tests())