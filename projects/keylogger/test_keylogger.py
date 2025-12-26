from keylogger import keylogger
class test_keylogger:

    def test_toggle(self):
        logger= keylogger()
        logger.recording = False
        logger.keyPressed(logger.toggle_key)
        assert logger.recording == True , "Toggle on has failed"

        logger.keyPressed(logger.toggle_key)
        assert logger.recording == False , "Toggle OFF has failed"

        print("Toggle test has PASSED")


def run_tests():
        tests=test_keylogger()
        tests.test_toggle()
        print("ALL TESTS HAS PASSED")

if __name__ == "__main__":
        run_tests()