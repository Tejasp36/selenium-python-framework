import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from config.config_reader import ConfigReader


@pytest.fixture(scope="function")
def driver():

    options = Options()

    # =========================
    # Headless Mode
    # =========================

    if ConfigReader.is_headless():
        options.add_argument("--headless=new")

    # =========================
    # Browser Stability Options
    # =========================

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")

    # Better stability in CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # =========================
    # Launch Browser
    # =========================

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # =========================
    # Timeouts
    # =========================

    driver.set_page_load_timeout(30)

    # =========================
    # Open Application
    # =========================

    driver.get(ConfigReader.get_base_url())

    yield driver

    # =========================
    # Close Browser
    # =========================

    driver.quit()