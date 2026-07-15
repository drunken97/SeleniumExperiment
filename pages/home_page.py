from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.home_locators import HomeLocators

class HomePage(BasePage):

    def close_popup(self):
        self.wait.until(
            EC.element_to_be_clickable(HomeLocators.CLOSE_POPUP)
        ).click()

    def flights_tab_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                HomeLocators.FLIGHTS_TAB
            )
        ).is_displayed()

    def click_from_city(self):
        self.wait.until(
            EC.element_to_be_clickable(HomeLocators.FROM_CITY)
        ).click()

