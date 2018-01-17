from bs4 import BeautifulSoup
import sys
import codecs

def main():
    with codecs.open(sys.argv[1],'r','utf-8') as fp:
        soup = BeautifulSoup(fp,'html.parser')
        text = soup.get_text()
        print(text.encode("utf-8"))
    
if __name__ == "__main__":
    main()