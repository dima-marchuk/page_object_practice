from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def product_should_have_correct_name(self):
        book_title_in_message = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_IN_MESSAGE)
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        assert book_title_in_message.text == book_title.text, "incorrect title"

    def product_should_have_correct_price(self):
        book_price_in_message = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_MESSAGE)
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        assert book_price_in_message.text == book_price.text, "incorrect price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared"