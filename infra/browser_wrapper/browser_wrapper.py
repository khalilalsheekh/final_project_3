import time

from pip._internal.resolution.resolvelib.factory import C


from selenium import webdriver

from infra.browser_wrapper.config_provider import ConfigProvider


class BrowserWrapper:
    def __init__(self):
        self._driver = None
        self.config = ConfigProvider.load_config_json('../../config.json')

    def get_driver(self, url):
        try:
            if self.config["browser"] == "chrome":
                self._driver = webdriver.Chrome()
            elif self.config["browser"] == "edge":
                self._driver = webdriver.Edge()
            else:
                print("Browser type not supported")
                return None
            self._driver.get(url)
            time.sleep(10)
            return self._driver
        except C.webDriverException as e:
            print("ERROR : ", e)
            return None
