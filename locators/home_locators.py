from selenium.webdriver.common.by import By

class HomeLocators:

    CLOSE_POPUP = (By.CSS_SELECTOR, "span.commonModal__close")
    FLIGHTS_TAB = (By.XPATH, "//span[text()='Flights']")
    FROM_CITY = (By.ID, "fromCity")
    FROM_INPUT = (By.CSS_SELECTOR, "input[placeholder='From']")
    
    