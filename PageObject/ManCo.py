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

        # 1.ManCo Details:
        self.ManCo = "//*[@id='root']/section/section/section/main/div/div[1]/div/div/div/div/div[1]/div[1]"
        self.AddManCo = "//*[@id='root']/section/section/section/main/header/div/div/div[1]/span[2]/div/div[2]/button"
        self.ManCoName = "//Input[@name = 'mancoName']"
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
        self.FirstName = "//Input[@name = 'firstName']"
        self.LastName = "//Input[@name = 'lastName']"
        self.Email = "//Input[@name = 'email']"
        self.MobileNumber = "//Input[@name = 'mobileNumber']"
        self.LandLine = "//Input[@name = 'landLine']"
        self.AddManCoSubmit = "//button[@class = 'ant-btn permit-primary-btn']"


    def Click_Intellegence(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.Intellegence)))
        element.click()

    def Click_ManCo_and_AddManCo(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.ManCo)))
        element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.AddManCo)))
        element.click()

    def Click_ManCoDetails(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.ManCoName)))
        element.send_keys("ABC_UK")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.BuildingName)))
        element.send_keys("ABCD")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AddressLine1)))
        element.send_keys("10th Street")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AddressLine2)))
        element.send_keys("Upland")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Town)))
        element.send_keys("HYD")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.County)))
        element.send_keys("WhiteField")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.PostCode)))
        element.send_keys("HYD0010")
        wait = WebDriverWait(self.driver, 10)
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
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.FirstName)))
        element.send_keys("Renjith")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.LastName)))
        element.send_keys("R")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Email)))
        element.send_keys("renjith.rr@gmail.com")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.MobileNumber)))
        element.send_keys("7793977515")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.LandLine)))
        element.send_keys("0805490210")

        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AddManCoSubmit)))
        element.click()

        time.sleep(10)

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.ManCo)))
        element.click()

        time.sleep(15)


        #Hover_ManCo:
        element1 = self.driver.find_element_by_xpath("//*[contains(text(), 'ABC_UK')]")
        actions = ActionChains(self.driver)
        actions.move_to_element(element1)
        actions.perform()

        element2 = self.driver.find_element_by_xpath("//div[@class='ant-col addIcon']")
        actions.move_to_element(element2)
        actions.perform()
        element2.click()

        time.sleep(5)
