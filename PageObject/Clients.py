from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from Tests.test_Login import login
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains



class EstateManagement():
    def __init__(self, driver):
        self.driver = driver
        self.Intellegence = "//div[@class='ant-menu-submenu-title']"
        self.Clients = "/html//div[@id='root']/section/section/section[@class='ant-layout']//div[@role='tablist']//div[@class='ant-tabs-nav ant-tabs-nav-animated']/div[1]/div[2]"
        self.AddClients = "/html//div[@id='root']/section/section/section[@class='ant-layout']//div[@class='main-header-container']//button[@type='button']"



        # 2.Clients Details:
        self.ClientName = "//Input[@name = 'clientName']"
        # Address
        self.BuildingName = "//Input[@name = 'buildingName']"
        self.AddressLine1 = "//Input[@name = 'address1']"
        self.AddressLine2 = "//Input[@name = 'address2']"
        self.Town = "//Input[@name = 'town']"
        self.County = "//Input[@name = 'county']"
        self.PostCode = "//Input[@name = 'postCode']"
        self.Country = "//div[contains(text(),'Country')]"
        # Contact
        self.Title = "//div[contains(text(),'Mr')]"
        self.C_FirstName = "//Input[@name = 'firstName']"
        self.C_LastName = "//Input[@name = 'lastName']"
        self.C_Email = "//Input[@name = 'email']"
        self.CountryCode = "//Input[@name = 'countryCode']"
        self.C_MobileNumber = "//Input[@name = 'mobileNumber']"
        self.C_LandLine = "//Input[@name = 'landLine']"
        self.AddClientsSubmit = "//button[@class = 'ant-btn permit-primary-btn']"
        self.Clients = "//*[@id='root']/section/section/section/main/div/div[1]/div/div/div/div/div[1]/div[2]"

    def Click_Intellegence(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.Intellegence)))
        element.click()

    def Click_Client_and_AddClient(self):

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.Clients)))
        element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.AddClients)))
        element.click()


    def Click_ClientsDetails(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.ClientName)))
        element.send_keys("CBA_UK")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.BuildingName)))
        element.send_keys("BBBBB")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AddressLine1)))
        element.send_keys("9th Street")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AddressLine2)))
        element.send_keys("Downland")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Town)))
        element.send_keys("ATP")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.County)))
        element.send_keys("GreenField")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.PostCode)))
        element.send_keys("ATP01010")
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Country)))
        element.click()
        element = self.driver.find_element_by_xpath("//li[contains(text(),'UK')]")
        element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Title)))
        element.click()
        element = self.driver.find_element_by_xpath("//li[contains(text(),'Mr')]")
        element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.C_FirstName)))
        element.send_keys("Jhon")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.C_LastName)))
        element.send_keys("Dave")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.C_Email)))
        element.send_keys("jhon_dave@gmail.com")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.C_MobileNumber)))
        element.send_keys("9990009900")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.C_LandLine)))
        element.send_keys("0401919191")


        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AddClientsSubmit)))
        element.click()

        time.sleep(10)


        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.Clients)))
        element.click()

        time.sleep(15)

        #Hover_Clients:
        element3 = self.driver.find_element_by_xpath("/html//div[@id='root']/section/section/section[@class='ant-layout']//div[@class='ant-tabs-content ant-tabs-content-animated ant-tabs-top-content']/div[2]//div[@class='ant-table-body']/table[@class='ant-table-fixed']/tbody//span[.='CBA_UK']")
        actions = ActionChains(self.driver)
        actions.move_to_element(element3)
        actions.perform()

        element4 = self.driver.find_element_by_xpath("//div[@class='ant-col addIcon']")
        actions.move_to_element(element4)
        actions.perform()
        element4.click()

        time.sleep(5)
