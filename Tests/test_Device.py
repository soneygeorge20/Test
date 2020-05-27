import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
import Tests
from Tests.test_Login import login
from PageObject.Device import EstateManagement


@pytest.mark.unit
def test_EstateManagement(applicationURL, EmailID, Password):
    driver = login(applicationURL, EmailID, Password)
    print("Displaying input1: %s" % applicationURL)
    print("Displaying input2: %s" % EmailID)
    print("Displaying input2: %s" % Password)
    estateobj = EstateManagement(driver)
    estateobj.Click_Intellegence()

    estateobj.Click_Device_and_AddDevice()
  #  estateobj.Click_DeviceDetails()