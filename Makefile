

parse:
	python parse.py > rawlist.txt
	cat  rawlist.txt | sort | uniq -i > sorted.txt

translate:
	python translate.py sorted.txt translated.txt
	
tohtml:
	python tohtml.py