
from actions.login_action import LoginAction


def test_valid_login(driver):

    login = LoginAction(driver)

    login.login("Admin", "admin123")

    login.validateURL("dashboard")
