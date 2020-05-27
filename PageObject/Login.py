import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    request.cls.driver = chrome_driver
    yield
@pytest.mark.usefixtures("chrome_driver_init")
class Basic_Chrome_Test:
    pass
class Test_URL_Login(Basic_Chrome_Test):
    def test_Login(self):
        self.driver.get("https://stg.nexusplatform.co.uk/")
        print(self.driver.title)
        time.sleep(10)
        self.driver.find_element_by_xpath("//input[@name='emailAddress']").send_keys("ramanan.renjith@hashedin.com")
        time.sleep(10)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("Hasher@1991")
        time.sleep(10)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(10)