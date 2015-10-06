from argparse import ArgumentParser
import os
import shutil


class Saver:
    def __init__(self, path: str):
        self.path = path
        if os.path.isdir(path):
            shutil.rmtree(path)
        os.mkdir(path)

    def save_them(self, found_items: list):
        for item in found_items:
            with open("{path}/{word}.txt".format(path=self.path, word=item.get_word()), 'a') as file:
                file.write(item.get_line())
                file.close()


class WantedRecord:
    def __init__(self, word: str, line: str):
        self._word = word
        self._line = line

    def get_word(self):
        return self._word.strip()

    def get_line(self):
        return self._line


class Seeker:
    def __init__(self, dictionary: str, log: str):
        self._result = []
        self._dictionary = dictionary
        self._log = log

    def get_result(self):
        return self._result

    def read_file(self, path: str):
        with open(path, 'r+') as file:
            return file.readlines() # ?

    def find_them(self):
        dy = self.read_file(self._dictionary)
        log = self.read_file(self._log)
        for log_line in log:
            fw = self.get_first_word(log_line)
            for word in dy:
                if fw == word.strip():
                    self._result.append(WantedRecord(word, log_line))

    def get_first_word(self, line:str):
        word = ""
        for letter in line:
            if not letter.isspace():
                word += letter
            else:
                return word


class Controller:
    def __init__(self, dictionary: str, log: str, save_here: str):
        self._seeker = Seeker(dictionary, log)
        self._saver = Saver(save_here)

    def run(self):
        self._seeker.find_them()
        self._saver.save_them(self._seeker.get_result())


def main(dictionary: str, log: str, save_here: str):
    c = Controller(dictionary, log, save_here)
    c.run()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-d', dest='dictionary', help='Path of dictionary', required=True)
    parser.add_argument('-l', dest='log', help='Path of log file', required=True)
    parser.add_argument('-s', dest='save_here', help='Path where to save', required=False, default="separated")
    args = parser.parse_args()
    main(args.dictionary, args.log, args.save_here)
