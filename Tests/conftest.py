import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
def pytest_addoption(parser):
    parser.addoption("--applicationURL", action="store", default="default input1")
    parser.addoption("--EmailID", action="store", default="default input2")
    parser.addoption("--Password", action="store", default="default input3")
@pytest.fixture
def applicationURL(request):
    return request.config.getoption("--applicationURL")
@pytest.fixture
def EmailID(request):
    return request.config.getoption("--EmailID")
@pytest.fixture
def Password(request):
    return request.config.getoption("--Password")
#@pytest.fixture()
def login(applicationURL, EmailID, Password):
    driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(applicationURL)
    email = "//input[@name='emailAddress']"
    password = "//input[@name='password']"
    loginButton = "//button[@type='submit']"
    wait = WebDriverWait(driver, 10)
    element = wait.until(ec.presence_of_element_located((By.XPATH, email)))
    element.send_keys(EmailID)
    wait1 = WebDriverWait(driver, 10)

    element1 = wait1.until(ec.presence_of_element_located((By.XPATH, password)))
    element1.send_keys(Password)
    wait2 = WebDriverWait(driver, 10)
    element2 = wait2.until(ec.presence_of_element_located((By.XPATH, loginButton)))
    element2.click()
    time.sleep(5)
    return driver