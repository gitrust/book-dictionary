
TITLE:=Testbook
URL:=http://www.gutenberg.org/files/18857/18857-h/18857-h.htm

# Download HTML book as book.html
download-book:
	wget -O book.html $(URL)

# Convert HTML book to text version
book2text:
	python totext.py > book.txt

parse:
	python parse.py > rawlist.txt
	cat  rawlist.txt | sort | uniq -i > sorted.txt

# translate dictionary entries
translate:
	python translate.py sorted.txt translated.txt

# Convert dictionary to HTML version
dic2html:
	python tohtml.py

