import unittest
from main import Seeker, WantedRecord


class MyTestCase(unittest.TestCase):
    def test_get_first_word(self):
        test_line = "This is a test line"
        exptected_word = "This"
        self.assertEqual(Seeker.get_first_word(self, test_line), exptected_word)

    def test_find_them(self):
        s = Seeker("test/dict", "test/log")
        expected_records = [WantedRecord("second", "second line"),
                            WantedRecord("third", "third party")]
        s.find_them()
        self.assertEqual(s.get_result(), expected_records)


def find_them(self):
    for log_line in self.log:
        fw = self.get_first_word(log_line)
        for word in self.dy:
            if fw == word.strip():
                self._result.append(WantedRecord(word, log_line))


if __name__ == '__main__':
    unittest.main()
