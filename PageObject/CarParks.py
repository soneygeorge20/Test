from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from Tests.test_Login import login
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select



class EstateManagement():
    def __init__(self, driver):
        self.driver = driver
        self.Intellegence = "//div[@class='ant-menu-submenu-title']"

        # 4.Car Park:
        self.CarPark = "//*[@id='root']/section/section/section/main/div/div[1]/div/div/div/div/div[1]/div[4]"
        self.AddCarPark = "//*[@id='root']/section/section/section/main/header/div/div/div[1]/span[2]/div/div[2]/button"
        self.SelectSites = "//*[contains(text(), 'Select Site')]"
        self.CarParkName = "//Input[@name = 'carParkName']"
        self.Mid = "//Input[@name = 'mid']"
        # Timing Settings
        self.MonDay = ".ant-row .ant-tag-checkable:nth-of-type(1)"
        self.TuesDay = ".ant-row .ant-tag-checkable:nth-of-type(2)"
        self.WednesDay = ".ant-row .ant-tag-checkable:nth-of-type(3)"
        self.ThursDay = ".ant-row .ant-tag-checkable:nth-of-type(4)"
        self.FriDay = ".ant-row .ant-tag-checkable:nth-of-type(5)"
        self.SaturDay = ".ant-row .ant-tag-checkable:nth-of-type(6)"
        self.SunDay = ".ant-row .ant-tag-checkable:nth-of-type(7)"
        self.BankHolidays = ".ant-row .ant-tag-checkable:nth-of-type(8)"


        self.EnforcementFullDay = ".ant-row-flex-space-between:nth-child(5) .ant-radio-button-wrapper-checked > span:nth-of-type(2)"
        self.EnforcementDuration = ".ant-row-flex-space-between:nth-child(5) .ant-radio-button-wrapper:nth-of-type(2) > span:nth-of-type(2)"

        self.OpeningTimerFrom = "/html/body/div[2]/div/div[2]/div/div/div[2]/div/form/div[3]/div[2]/div[3]/div[1]/div/div[2]/div/span/span"
        self.OpeningTimingFrom = "//input [@class='ant-time-picker-panel-input'][1]"
        self.OpeningTimerTo = "/html/body/div[2]/div/div[2]/div/div/div[2]/div/form/div[3]/div[2]/div[3]/div[2]/div/div[2]/div/span/span/input"
        self.OpeningTimingTo = "/html/body/div[4]/div/div/div/div[1]/input"

        self.ConsiderationPeriod = "//Input[@name = 'timingSettings[0].considerationPeriod']"
        self.GracePeriodPeriod = "//Input[@name = 'timingSettings[0].gracePeriod']"
        self.GracePeriodPeriodBlueBadge = "//Input[@name = 'timingSettings[0].gracePeriodBlueBadge']"

        self.FreePeriodPerVisit = ".ant-row-flex-space-between:nth-child(8) .ant-radio-button-wrapper:nth-of-type(1) > span:nth-of-type(2)"
        self.FreePeriodPerDay = ".ant-row-flex-space-between:nth-child(8) .ant-radio-button-wrapper-checked > span:nth-of-type(2)"

        self.FreePeriodFromTimer = "/html/body/div[2]/div/div[2]/div/div/div[2]/div/form/div[3]/div[2]/div[7]/div[2]/div/div[2]/div/span/span/input"
        self.FreePeriodFromTime = "/html/body/div[5]/div/div/div/div[1]/input"
        self.FreePeriodToTimer = "/html/body/div[2]/div/div[2]/div/div/div[2]/div/form/div[3]/div[2]/div[7]/div[3]/div/div[2]/div/span/span/input"
        self.FreePeriodToTime = "/html/body/div[6]/div/div/div/div[1]/input"
        self.AddCarParkSubmit = "//button[@class = 'ant-btn permit-primary-btn']"

    def Click_Intellegence(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.Intellegence)))
        element.click()


    def Click_CarParks_and_AddCarParks(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.CarPark)))
        element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.AddCarPark)))
        element.click()

    def Click_CarParkDetails(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.CarParkName)))
        element.send_keys("UBUN")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Mid)))
        element.send_keys("9100101")
        time.sleep(5)

        element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.MonDay)))
        element.click()

        element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.ThursDay)))
        element.click()

        element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.BankHolidays)))
        element.click()



        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.EnforcementDuration)))
        element.click()


        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.OpeningTimerFrom)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.OpeningTimingFrom)))
        element.click()
        element.send_keys("08:10")
        element.click()

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.OpeningTimerTo)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.OpeningTimingTo)))
        element.click()
        element.send_keys("23:30")
        element.click()
        wait = WebDriverWait(self.driver, 10)

        
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.ConsiderationPeriod)))
        element.click()
        element.send_keys("20")
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.GracePeriodPeriod)))
        element.send_keys("20")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.GracePeriodPeriodBlueBadge)))
        element.send_keys("30")

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.FreePeriodPerDay)))
        element.click()

        element = wait.until(ec.presence_of_element_located((By.XPATH, self.FreePeriodFromTimer)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.FreePeriodFromTime)))
        element.click()
        element.send_keys("13:00")
        element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.FreePeriodToTimer)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.FreePeriodToTime)))
        element.click()
        element.send_keys("15:00")
        element.click()

        time.sleep(10)

#        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AddCarParkSubmit)))
#        element.click()


