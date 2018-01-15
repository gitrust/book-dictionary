from bs4 import BeautifulSoup


with open("book.html") as fp:
    soup = BeautifulSoup(fp)
    print(soup.get_text())