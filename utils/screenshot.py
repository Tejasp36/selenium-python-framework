
from datetime import datetime
import os


def capture(driver, name):

    os.makedirs("reports/screenshots", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    path = f"reports/screenshots/{name}_{timestamp}.png"

    driver.save_screenshot(path)
