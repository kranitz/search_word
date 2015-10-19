from argparse import ArgumentParser
import os
import shutil
import time


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
        self.dictfile = open(dictionary)
        self.logfile = open(log)

    def get_first_word(self, line: str):
        word = ""
        for letter in line:
            if not letter.isspace():
                word += letter
            else:
                return word

    def get_result(self):
        return self._result

    def find_them(self):
        pass


class EfficientSeeker(Seeker):
    def __init__(self, dictionary, log):
        super().__init__(dictionary, log)
        self.dy = self.read_with_yield(self.dictfile)
        self.log = self.read_with_yield(self.logfile)
        self.tree = {}
        self.start_to_build_tree()

    def read_with_yield(self, file):
        while True:
            data = file.readline()
            if not data:
                break
            yield data

    def start_to_build_tree(self):
        for word in self.read_with_yield(self.dictfile):
            self.build_tree(self.tree, word.strip())

    def build_tree(self, tree, word):
        if not word:
            tree['complete_word'] = True
            return
        if word[0] not in tree:
            tree[word[0]] = {'complete_word': False}
        self.build_tree(tree[word[0]], word[1:])

    def read_tree(self, tree, word):
        if word[0] in tree:
            self.read_tree(tree[word[0]], word[1:])
            if tree['complete_word']:
                print(word)

    def find_word_in_tree(self, word: str, tree: dict):
        if not word:
            return tree.get('complete_word', False)
        if word[0] not in tree:
            return False
        return self.find_word_in_tree(word[1:], tree[word[0]])

    def find_them(self):
        for log_line in self.log:
            fw = self.get_first_word(log_line)
            if self.find_word_in_tree(fw, self.tree):
                self._result.append(WantedRecord(fw.strip(), log_line))


class DummySeeker(Seeker):
    def __init__(self, dictionary, log):
        super().__init__(dictionary, log)
        self.dy = self.read_file(dictionary)
        self.log = self.read_file(log)

    def read_file(self, path: str):
        with open(path, 'r+') as file:
            return file.readlines()

    def find_them(self):
        for log_line in self.log:
            fw = self.get_first_word(log_line)
            for word in self.dy:
                if fw == word.strip():
                    self._result.append(WantedRecord(word.strip(), log_line))


class Controller:
    def __init__(self, dictionary: str, log: str, save_here: str, efficient):
        self.efficient = efficient
        self.dictionary = dictionary
        self.log = log
        self._saver = Saver(save_here)

    def run(self):
        if self.efficient:
            efficient_seeker = EfficientSeeker(self.dictionary, self.log)
            print("EfficientSeeker started to work...")
            start_time = time.time()
            efficient_seeker.find_them()
            print("And finished in: {} sec".format(time.time()-start_time))
            self._saver.save_them(efficient_seeker.get_result())
        else:
            dummy_seeker = DummySeeker(self.dictionary, self.log)
            print("DummySeeker started to work...")
            start_time = time.time()
            dummy_seeker.find_them()
            print("And finished in: {} sec".format(time.time() - start_time))
            self._saver.save_them(dummy_seeker.get_result())



def main(dictionary: str, log: str, save_here: str, efficient):
    c = Controller(dictionary, log, save_here, efficient)
    c.run()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-d', dest='dictionary', help='Path of dictionary', required=True)
    parser.add_argument('-l', dest='log', help='Path of log file', required=True)
    parser.add_argument('-s', dest='save_here', help='Path where to save', required=False, default="separated")
    parser.add_argument('-e', dest='efficient', help='Use more efficient searching methods',
                        required=False, action="store_true")
    args = parser.parse_args()
    main(args.dictionary, args.log, args.save_here, args.efficient)
