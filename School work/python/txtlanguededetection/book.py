class Book:
    def __init__(self, title, author, year, language, text):
        self.title = title
        self.author = author
        self.year = year
        self.language = language
        self.text = text

    def print_metadata(self):
        """
        Prints the metadata of the book
        :return:
        """
        print(f"Author: {self.author}\nYear: {self.year}\nLanguage: {self.language}\n")
