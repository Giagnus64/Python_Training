from Milestone_4.locators.book_locators import BookLocators

class BookParser:
    """
    A class that takes in an HTML page part and identifies the parts of a book.
    """
    RATINGS = {
        'One':1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.title}, Price: {self.price}, Rating: {self.rating} {"star" if self.rating == 1 else "stars"}>'

    @property
    def title(self):
        locator = BookLocators.TITLE
        return self.parent.select_one(locator).attrs['title']

    @property
    def link(self):
        locator = BookLocators.LINK
        return self.parent.select_one(locator).attrs['href']

    @property
    def price(self):
        locator = BookLocators.PRICE
        price_unformatted = self.parent.select_one(locator).string
        price_formatted = price_unformatted.replace("£", "")
        return float(price_formatted)

    @property
    def rating(self):
        locator = BookLocators.RATING
        star_rating_element = self.parent.select_one(locator)
        classes = star_rating_element.attrs['class']
        rating_classes = filter(lambda x: x != 'star-rating', classes)
        number_rating = BookParser.RATINGS.get(next(rating_classes))
        return number_rating

    @property
    def availability(self):
        locator = BookLocators.AVAILABILITY
        availability_element = self.parent.select_one(locator)
        classes = availability_element.attrs['class']
        availability_classes = filter(lambda x: x != 'availability', classes)
        return next(availability_classes)

