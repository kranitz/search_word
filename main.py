__author__ = 'gabor'


class Saver:
    def save_them(self, found_items: list):
        for item in found_items:
            with open("separated/" + item.get_word() + ".txt", 'a') as file:
                file.write(item.get_line())
                file.close()


class FoundIt:
    def __init__(self, word: str, line: str):
        self._word = word
        self._line = line

    def get_word(self):
        return self._word

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
                    self._result.append(FoundIt(word, log_line))

    def get_first_word(self, line:str):
        word = ""
        for letter in line:
            if not letter.isspace():
                word += letter
            else:
                return word


class Controller:
    def __init__(self):
        self._seeker = Seeker("dictionary.txt", "log.txt")
        self._saver = Saver()

    def run(self):
        self._seeker.find_them()
        if self._seeker.get_result():
            self._saver.save_them(self._seeker.get_result())


def main():
    c = Controller()
    c.run()

if __name__ == "__main__":
    main()

