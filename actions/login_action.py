from utils.base_action import BaseAction
from locators.login_locator import LoginLocator


class LoginAction(BaseAction):

    def login(self, username, password):
        self.enter_text(LoginLocator.USERNAME, username)
        self.enter_text(LoginLocator.PASSWORD, password)
        self.click(LoginLocator.LOGIN_BUTTON)

    def validateURL(self, text):
        assert "dashboard" in self.driver.current_url.lower()
