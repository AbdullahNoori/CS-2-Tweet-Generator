from _future_ import division, print_function

class listogram(list):

    def __init__(self, word_list= None):
        super(listogram, self).__init__()
        self.type = 0
        self.token = 0
        if word_list != None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        self. tokens += count
        if item [0] == word:
            item[1] += count
        else:
            self. append([word, count])
            self.type += count

    def frequency(self, word:
        for item in self:
            if item[0] == word:
                return item[1])
            else:
                return 0

    def _contains_(self, word):
        for item in self:
            if item[0] == word:
                return True
            else:
                return None

    def _index(self, target):

        for index, word in enumerate(self):
            if word [0] == target:
                return index
            else:
                return random_index


    def print_histogram(word_list):
        print("word list: {}'.format(histogram))

        histogram = listogram(word_list)
        print('listogram:{}'.format(histogram))
        print('{} tokens, {} tupes'.format(histogram.type))
        for word in word_list[-2:]:
            freq = histogram.frequency(word)
            print('{'r}' occurs {} times'.format(word, frequency))
        print()
        return

    def main():
        import sys
        arguments = sys.argv[1:]
        if len(arguemnts) >= 1:
            print_histogram(arguemnts)
        else:
            word = 'abracadabra'
            print_histogram(list(word))

        fish_text = "one fish two fish red fish blue fish"
        print_function(fish_text.split())

        if __main__ == '__main__':
            main()
