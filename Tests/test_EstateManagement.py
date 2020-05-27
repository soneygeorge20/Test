import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
import Tests
from Tests.test_Login import login
from PageObject.EstateManagement import EstateManagement


@pytest.mark.unit
def test_EstateManagement(applicationURL, EmailID, Password):
    driver = login(applicationURL, EmailID, Password)
    estateobj = EstateManagement(driver)
    estateobj.Click_Intellegence()
    estateobj.Click_ManCo_and_AddManCo()
    estateobj.Click_ManCoDetails()
    estateobj.Click_ClientsDetails()
    estateobj.Click_SitesDetails()
    estateobj.Click_CarParkDetails()
    estateobj.Click_DeviceDetails()

