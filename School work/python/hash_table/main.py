#!/usr/bin/env python3
# dll.py

# Introduction to Algorithms, Fourth edition
# Linda Xiao

#########################################################################
#                                                                       #
# Copyright 2022 Massachusetts Institute of Technology                  #
#                                                                       #
# Permission is hereby granted, free of charge, to any person obtaining #
# a copy of this software and associated documentation files (the       #
# "Software"), to deal in the Software without restriction, including   #
# without limitation the rights to use, copy, modify, merge, publish,   #
# distribute, sublicense, and/or sell copies of the Software, and to    #
# permit persons to whom the Software is furnished to do so, subject to #
# the following conditions:                                             #
#                                                                       #
# The above copyright notice and this permission notice shall be        #
# included in all copies or substantial portions of the Software.       #
#                                                                       #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,       #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF    #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                 #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS   #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN    #
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN     #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE      #
# SOFTWARE.                                                             #
#                                                                       #
#########################################################################
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


class LinkedListNode:

    def __init__(self, data):
        """Initialize a node of a doubly linked list with the given data."""
        self.prev = None
        self.next = None
        self.data = data

    def get_data(self):
        """Return data."""
        return self.data

    def __str__(self):
        """Return data as a string."""
        return str(self.data)


class LinkedList:

    def __init__(self, get_key_func=None):
        """Initialize an empty doubly linked list with only a head pointer.

        Argument:
        get_key_func -- an optional function that returns the key for the
        objects stored. May be a static function in the object class. If
        omitted, then identity function is used.
        """
        self.head = None
        if get_key_func is None:
            self.get_key = lambda x: x  # return self
        else:
            self.get_key = get_key_func  # return key defined by user

    def search(self, k):
        """Search a doubly linked list for a node with key k.

        Returns:
        x -- a node with key k or None if not found
        """
        x = self.head
        # get_key_func used in searching.
        while x is not None and self.get_key(x.data) != k:
            x = x.next
        return x

    def insert(self, data, y):
        """Insert a node with data after node y.  Return the new node."""
        x = LinkedListNode(data)  # construct a node x
        x.next = y.next  # x's successor is y's successor
        x.prev = y  # x's predecessor is y
        if y.next is not None:
            y.next.prev = x  # x comes before y's successor
        y.next = x  # x is now y's successor
        return x

    def prepend(self, data):
        """Insert a node with data as the head of a doubly linked list.  Return the new node."""
        x = LinkedListNode(data)  # construct a node x
        x.next = self.head  # set its next to the head
        if self.head is not None:  # if a head already exists, change its prev
            self.head.prev = x
        self.head = x  # x is the new head
        x.prev = None
        return x

    def delete(self, x):
        """Remove a node x from a doubly linked list.

        Assumption:
        x is a node in the linked list.
        """
        if x.prev is not None:  # if x is not the head
            x.prev.next = x.next  # connect its previous to its next
        else:
            self.head = x.next  # otherwise, set new head
        if x.next is not None:  # if x is not the tail
            x.next.prev = x.prev  # connect its next to its previous

    def delete_all(self):
        """Delete all nodes in a doubly linked list."""
        self.head = None

    def iterator(self):
        """Iterator from the head of a doubly linked list."""
        x = self.head
        while x is not None:
            yield x.get_data()
            x = x.next

    def copy(self):
        """Return a copy of this doubly linked list."""
        c = LinkedList(self.get_key)  # c is the copy
        x = self.head
        if x is not None:  # start by making the head node in the copy
            last = c.prepend(x.data)  # last is the last node in the copied list
            x = x.next
        while x is not None:
            last = c.insert(x.data, last)  # append a node with x's data to c
            x = x.next
        return c

    def __str__(self):
        """Return this doubly linked list formatted as a list of chars."""
        x = self.head
        string = "["
        while x.next is not None:
            string += (str(x) + ", ")
            x = x.next
        string += (str(x) + "]")
        return string

    def str(self):
        """Return this doubly linked list formatted as a list tuple elements."""
        x = self.head
        array = []
        while x is not None:
            array.append(x.data)
            x = x.next
        return array


# Testing
if __name__ == "__main__":

    from key_object import KeyObject

    m = 10  # the size of our hashtable array
    array = [None] * m
    top_10 = [("None", 0)] * 20
    with open("file.txt", encoding='UTF-8') as f:
        inp = f.readlines()
        inp = str(inp)

        for inp in inp.split(" "):
            inp = inp.replace('"', '')
            inp = inp.replace("'", '')
            inp = inp.replace(".", '')
            inp = inp.replace(",", '')
            inp = inp.replace("?", '')
            inp = inp.replace("”", '')
            inp = inp.replace(":", '')
            inp = inp.replace("\n", '')
            inp = inp.replace("\\n", '')
            inp = inp.replace("’", '')
            input_key = 0
            for x in inp:
                input_key += ord(x)
            input_key = input_key % m
            if array[input_key] is None:
                array.pop(input_key)
                list_name = LinkedList()
                list_name.prepend((inp, 1))
                array.insert(input_key, list_name)
            else:
                y = array[input_key].str()
                counter = 0
                for item in y:
                    if item[0] == inp:
                        word_amount = item[1]
                        k = array[input_key].search((inp, word_amount))
                        array[input_key].delete(k)
                        array[input_key].prepend((inp, word_amount + 1))
                        counter = -1
                        sub_counter = 0
                        for item1 in top_10:
                            if item1[1] >= word_amount and item[0] is not inp:
                                sub_counter += 1
                                continue
                            else:
                                top_10.__delitem__(sub_counter)
                                top_10.insert(sub_counter, (inp, word_amount))
                                break
                        break
                    counter += 1
                    if counter == -1:
                        break
                    if counter == len(y):
                        array[input_key].prepend((inp, 1))
    with open('result.txt', 'w') as file:
        for key in array:
            print(key, file=file)
    print([item[0] for item in top_10])
    print(top_10)

    # convert list to string and generate
    unique_string = str([item[0] for item in top_10])
    wordcloud = WordCloud(width=1000, height=500).generate(unique_string)
    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("wordcloud" + ".png", bbox_inches='tight')
    plt.show()
    plt.close()
"""

"""
