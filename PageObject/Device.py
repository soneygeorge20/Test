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





        # 5.Device:
        self.Device = "//*[@id='root']/section/section/section/main/div/div[1]/div/div/div/div/div[1]/div[5]"
        self.AddDevice = "//*[@id='root']/section/section/section/main/header/div/div/div[1]/span[2]/div/div[2]/button"
        self.SelectSite = ".custom-form .undefined:nth-of-type(1) .ant-select-selection__placeholder"
        self.CarParkName = ".custom-form .undefined:nth-of-type(2) .ant-select-selection__placeholder"
        self.NextPage = ".ant-row-flex-end .permit-primary-btn"

        self.CameraName = "//Input[@name = 'deviceName']"
        self.CameraType = "//button[@name = 'ant-btn device-btn ']"
        self.Make = "//Input[@name = 'make']"
        self.Model = "//Input[@name = 'model']"
        self.ExternalReference = "//Input[@name = 'reference']"
        self.InstallationDateSelect = "/html/body/div[9]/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/div[4]/div[2]/div/div[2]/div/span/span/div/input"
        self.InstallationDate = "/html/body/div[10]/div/div/div/div/div[1]/div/input"
        self.WarrantyExpirationDateSelect = "/html/body/div[9]/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/div[5]/div[1]/div[1]/div[2]/div/span/span/div/input"
        self.WarrantyExpirationDate = "/html/body/div[11]/div/div/div/div/div[1]/div/input"

        self.SerialNo = "//Input[@name = 'serialNo']"
        self.AuthenticationToken = "//Input[@name = 'token']"
        self.IPAddress = "//Input[@name = 'ip']"

        self.FacingDirection = "//div [@class='ant-select-selection__placeholder']"
        self.DefaultDirection = "/html/body/div[9]/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/div[8]/div[2]/div/div[2]/div/span/div/div/div/div"

        self.ActivationDateSelect = "/html/body/div[9]/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/div[8]/div[1]/div/div[2]/div/span/div/div/div/div"
        self.ActivationDateEnter = "/html/body/div[13]/div/div/div/div/div[1]/div/input"

        self.ActivationTime = "/html/body/div[9]/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/div[9]/div[2]/div[1]/div[2]/div/span/span/input"
        self.ActivationTimeEnter = "/html/body/div[14]/div/div/div/div[1]/input"

        self.DeactivationDateSelect = "/html/body/div[9]/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/div[10]/div[1]/div[1]/div[2]/div/span/span/div/input"
        self.DeactivationDateEnter = "/html/body/div[15]/div/div/div/div/div[1]/div/input"

        self.DeactivationTime = "/html/body/div[9]/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/div[10]/div[2]/div[1]/div[2]/div/span/span/input"
        self.DeactivationTimeEnter = "/html/body/div[16]/div/div/div/div[1]/input"

        self.Note = "//Input[@name = 'notes']"
        self.AddDeviceSubmit = "//button[@class = 'ant-btn permit-primary-btn']"




    def Click_Intellegence(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.Intellegence)))
        element.click()

    def Click_Device_and_AddDevice(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.Device)))
        element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.AddDevice)))
        element.click()

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.NextPage)))
        element.click()
        time.sleep(20)

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.SelectSite)))
        element.click()
        element = self.driver.find_element_by_xpath("//li[contains(text(),'site test 222')]")
        element.click()

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.CarParkName)))
        element.click()

        element = self.driver.find_element_by_xpath("//li[contains(text(),'edd')]")
        element.click()



    def Click_DeviceDetails(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.CameraName)))
        element.send_keys("UK_ERA")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.CameraType)))
        element.click()
        element = self.driver.find_element_by_xpath("//li[contains(text(),'Digital')]")
        element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Make)))
        element.send_keys("L&T")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Model)))
        element.send_keys("Nexuom333")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.ExternalReference)))
        element.send_keys("R1902R")

        element = wait.until(ec.presence_of_element_located((By.XPATH, self.InstallationDateSelect)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.InstallationDate)))
        element.click()
        element.send_keys("05-05-2020")
        element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.WarrantyExpirationDateSelect)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.WarrantyExpirationDate)))
        element.click()
        element.send_keys("05-05-2021")
        element.click()

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.SerialNo)))
        element.send_keys("91120010")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AuthenticationToken)))
        element.send_keys("R0910922119AB")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.IPAddress)))
        element.send_keys("1.9.0291")

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.FacingDirection)))
        element.click()
        element = self.driver.find_element_by_xpath("//li[contains(text(),'In')]")
        element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.DefaultDirection)))
        element.click()
        element = self.driver.find_element_by_xpath("//li[contains(text(),'Out')]")
        element.click()



        element = wait.until(ec.presence_of_element_located((By.XPATH, self.ActivationDateSelect)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.ActivationDateEnter)))
        element.click()
        element.send_keys("15-05-2020")
        element.click()

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.ActivationTime)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.ActivationTimeEnter)))
        element.click()
        element.send_keys("11:30")
        element.click()


        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.DeactivationDateSelect)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.DeactivationDateEnter)))
        element.click()
        element.send_keys("15-05-2025")
        element.click()

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.DeactivationTime)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.DeactivationDateEnter)))
        element.click()
        element.send_keys("23:30")
        element.click()


        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Note)))
        element.send_keys("SampleAutomationTest..")

        time.sleep(10)

#        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AddManCoSubmit)))
#        element.click()

