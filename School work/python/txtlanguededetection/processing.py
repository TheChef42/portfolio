import os
import string

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
        print(f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nLanguage: {self.language}\n")


def calculate_frequencies(text):
    '''calculate the freq of lettesers 1 by 1 '''
    # where to get thte alphabet?
    alphabet = string.ascii_lowercase
    text = text.lower()

    frequencies = {}
    for char in text:
        if char in alphabet:
            if char in frequencies.keys():
                frequencies[char] += 1
            else:
                frequencies[char] = 1

    frequencies = dict(sorted(frequencies.items(), key = lambda x: x[0]))
    total_freq = sum(frequencies.values())
    frequencies = {k: v/total_freq for k, v in frequencies.items()}

    return frequencies

def process_book(book_path):
    """
    TODO:
    1. open a book with name filename
    2. extract the text
    3. extrat the metadata
    4. create a Book instance
    :param filename: Is the book that is to be opened
    :return:
    book
    """
    with open(book_path, 'r', encoding='UTF-8') as file:
        content = file.read()

        title = ''
        author = ''
        year = ''
        language = ''
        text = ''

        header_end = content.index('***\n')
        header = content[:header_end]
        text = content[header_end:]

        # using the split funktion to find the metadata
        header_lines = header.split('\n')
        # look for the metadata line by line
        for line in header_lines:
            #Titel
            if line.startswith('Title: '):
                title = line.replace('Title: ', '')

            # author
            if line.startswith('Author: '):
                author = line.replace('Author: ', '')

            if line.startswith('Release Date: '):
                year = line.replace('Release Date: ', '').split(' ')[2]

            if line.startswith('Language: '):
                language = line.replace('Language: ', '')

            # create a Book class object
        book = Book(title, author, year, language, text)

        return book

book_path = 'Books-20221006/46-0.txt'

print(calculate_frequencies(process_book(book_path).text))
#Extracting and processing all books inside the Book folder
list_books = []
with os.scandir(r'Books-20221006') as files:
    for file in files:
        #print('working with file ', file)
        book = process_book(file)
        list_books.append(book)

for x in list_books:
    x.print_metadata()






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
