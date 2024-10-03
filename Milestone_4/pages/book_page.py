from bs4 import BeautifulSoup

from Milestone_4.locators.book_page_locators import BookPageLocators
from Milestone_4.parsers.book import BookParser

class BookPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = BookPageLocators.BOOK
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]