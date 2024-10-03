import requests

from pages.book_page import BookPage


page_content = requests.get('http://books.toscrape.com').content
page = BookPage(page_content)


print (page.page_count)

books = page.books

for page_num in range(1, page.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(url).content
    page = BookPage(page_content)
    books.extend(page.books)

