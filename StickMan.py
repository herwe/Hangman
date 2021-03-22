from GenerateString import GenerateString


class StickMan:
    lines = None
    words_dict = {}
    rmd_str = None
    pics_url = ["https://i.imgur.com/tpj2ULE.png", "https://i.imgur.com/GI679NK.png", "https://i.imgur.com/wzhJsGK.png",
                "https://i.imgur.com/o5T1IjB.png",
                "https://i.imgur.com/1iWJtaw.png", "https://i.imgur.com/4CWAWkK.png", "https://i.imgur.com/njRN5gQ.png"]

    def __init__(self):
        self.next()

    def add(self):
        self.lines += 1

    def next(self):
        temp = GenerateString()
        self.rmd_str = temp.rmdWord
        print(temp.rmdWord)
        self.lines = 0
        self.words_dict.clear()
        for i in range(97, 123):
            self.words_dict[chr(i)] = self.rmd_str
