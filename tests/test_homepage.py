from utilities.driver_factory import DriverFactory


def test_launch_makemytrip():

    driver = DriverFactory.get_driver()

    driver.get("https://www.makemytrip.com/flights/")

    print(driver.title)

    assert "MakeMyTrip" in driver.title

    driver.quit()