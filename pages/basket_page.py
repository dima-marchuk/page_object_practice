from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Product is presented, but should not be"

    def basket_should_have_message_about_emptiness(self):
        assert self.is_element_present(*BasketPageLocators.YOUR_BASKET_IS_EMPTY_INSCRIPTION), \
            "Basket is not empty"
