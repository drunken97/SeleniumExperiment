
from pages.home_page import HomePage
from datetime import datetime
def test_verify_title(driver):

    driver.get("https://www.makemytrip.com/flights/")
    test_take_screenshot(driver)
    expected = "MakeMyTrip"
    assert expected in driver.title

def test_verify_url(driver):

    driver.get("https://www.makemytrip.com/flights/")
    test_take_screenshot(driver)
    assert "makemytrip" in driver.current_url.lower()

def test_window_size(driver):

    driver.get("https://www.makemytrip.com/flights/")
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]
    test_take_screenshot(driver)
    print(width, height)
    assert width > 1000

def test_take_screenshot(driver):
    driver.get("https://www.makemytrip.com/flights/")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/{timestamp}_homepage.png")

def test_home_page(driver):

    driver.get("https://www.makemytrip.com/flights/")
    home = HomePage(driver)
    home.close_popup()
    test_take_screenshot(driver)
    assert home.flights_tab_visible()

def test_click_from(driver):

    driver.get("https://www.makemytrip.com/flights/")
    home = HomePage(driver)
    home.close_popup()
    home.click_from_city()
    test_take_screenshot(driver)
