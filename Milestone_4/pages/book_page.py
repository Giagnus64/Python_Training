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

    @property
    def page_count(self):
        locator = BookPageLocators.PAGECOUNT
        content = self.soup.select_one(locator).string
        page_count_string = content.split("of ")
        page_count_clean = page_count_string[1].replace("\n", "")
        return int(page_count_clean)