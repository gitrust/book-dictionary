
TITLE:=Journey to the centre of the earth
URL:=http://www.gutenberg.org/files/18857/18857-h/18857-h.htm


# Main target 
# - to download a book
# - process it (extract all words for translation)
# - translate 
# - create a html version of dictionary
all:
	make download-book
	make book2text
	make parse-text
	make translate
	make html

# Download HTML book as book.html
download-book:
	wget -O book.html $(URL)

# Convert HTML book to text version
book2text:
	python totext.py book.html > book.txt

parse-text:
	python parse.py book.txt > rawlist.txt
	cat  rawlist.txt | sort | uniq -i > sorted.txt

# translate dictionary entries
translate:
	python translate.py sorted.txt translated.txt
	
# Convert dictionary to HTML version
html:
	python tohtml.py translated.txt dic.html "$(TITLE)"

#
# Additional help targets
#

# sort translated file
sort-translated:
	cat translated.txt | sort > translated_2.txt
	mv -f translated_2.txt translated.txt

# determine untranslated words
untranslated:
	grep -e ':: *$$' translated.txt | sed 's/::  //' > untranslated.txt

# filter untranslated words (error during translation) to a new list
filter-translated:
	grep -ve ':: *$$' translated.txt | sort > filtered-translated.txt

# create patch with local changes
git-patch:
	git format-patch origin

# apply mail patches
git-apply-patch:
	git am < 000*.patch