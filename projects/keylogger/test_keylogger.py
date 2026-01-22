from datetime import datetime, timezone
from keylogger import KeyEvent, KeyType, keylogger
import json
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

        def test_jsonl_written_when_recording(tmp_path):
                log_path = "test_log.jsonl"

                logger = keylogger()
                logger.keyFile = Path(log_path)
                logger.recording = True

                logger.keyPressed(key="ENTER")

                assert logger.keyFile.exists(),"file does not exist"

                lines = logger.keyFile.read_text(encoding="utf-8").splitlines()
              
                assert len(lines) == 1,"There is more than 1 line when there is meant to be one"
                data = json.loads(lines[0])
                assert data["key"] == "[ENTER]","incorrect key recorded"
                assert data["key_type"] == "special","incorrect key type recorded"

                print("json writing test has PASSED")
                
def run_tests():
        tests=test_keylogger()
        tests.test_toggle()
        tests.test_key_event()
        tests.test_datetime()
        tests.test_jsonl_written_when_recording()
        print("ALL TESTS HAS PASSED")

if __name__ == "__main__":
        run_tests()