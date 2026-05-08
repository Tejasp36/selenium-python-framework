
import configparser
import os

config = configparser.ConfigParser()
config.read("config/config.ini")


class ConfigReader:

    @staticmethod
    def get_base_url():
        return config["DEFAULT"]["BASE_URL"]

    @staticmethod
    def get_browser():
        return config["DEFAULT"]["BROWSER"]

    @staticmethod
    def is_headless():
        github_actions = os.getenv("GITHUB_ACTIONS")

        if github_actions == "true":
            return config["GITHUB_ACTIONS"].getboolean("HEADLESS")

        return config["DEFAULT"].getboolean("HEADLESS")
