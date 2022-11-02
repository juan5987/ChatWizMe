import unittest
from utils import call_api

class Chatbox_TestCase(unittest.TestCase):
    def test_callAPI(self):
        self.assertIsInstance((call_api('helo, how are you ?')), str)
        

if __name__ == "__main__":
    unittest.main()