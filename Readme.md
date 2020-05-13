# Description

Project contains all work files for creating a novell book dictionary.

The idea behind this project was to have a lookup dictionary while reading a book in english.

# How To

1. adapt Makefile (Title, URL)
2. make all

## Simple steps explained

1. Download raw book
2. Preprocess raw version of book text
3. Split by words
4. Sort and uniq words
5. Translate each word
6. make a browsable HTML version

# Requirements

* python 3.5
* python module googletrans 2.2.0
* python module beautifulsoup
* make
* Unix tools (wget, cat, mv, sort, grep)

# References

* https://pypi.python.org/pypi/googletrans
* http://www.gutenberg.org/files/18857/18857-h/18857-h.htm
* https://pypi.python.org/pypi/nltk

# Screenshot

![Screenshot](https://raw.githubusercontent.com/gitrust/book-dictionary/master/screenshot.JPG)
