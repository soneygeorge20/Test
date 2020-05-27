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





        # 3.Sites Details:
        self.Sites = "//*[@id='root']/section/section/section/main/div/div[1]/div/div/div/div/div[1]/div[3]"
        self.AddSites = "//button[@class = 'ant-btn permit-primary-btn add-to-collection-btn']"
#        self.SelectManCoName = "/html/body/div[7]/div/div[2]/div/div/div[2]/form/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/span/div/div/span/i/svg"
#        self.SelectClientName = "/html/body/div[7]/div/div[2]/div/div/div[2]/form/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/span/div/div/span/i/svg"
        self.SiteName = "//Input[@name = 'siteName']"
        self.SiteId = "//Input[@name = 'siteId']"
        self.Status = "//*[contains(text(), 'Select Status')]"
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
        self.FirstName = "//Input[@name = 'contacts[0].firstName']"
        self.LastName = "//Input[@name = 'contacts[0].lastName']"
        self.Email = "//Input[@name = 'contacts[0].email']"
        self.CountryCode = "//Input[@name = 'countryCode']"
        self.MobileNumber = "//Input[@name = 'contacts[0].mobileNumber']"
        self.LandLine = "//Input[@name = 'contacts[0].landLine']"
        self.AddSitesSubmit = "//button[@class = 'ant-btn permit-primary-btn']"
        self.ClickCarPark = "[role='tabpanel']:nth-of-type(3) .ant-row-flex-middle:nth-of-type(1) div:nth-of-type(1) .link-display"


    def Click_Intellegence(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.Intellegence)))
        element.click()



    def Click_Sites_and_AddSites(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.Sites)))
        element.click()
   #     wait = WebDriverWait(self.driver, 10)
   #     element = wait.until(ec.element_to_be_clickable((By.XPATH, self.AddSites)))
   #     element.click()


    #    wait = WebDriverWait(self.driver, 10)
    #    element = wait.until(ec.element_to_be_clickable((By.XPATH, self.Sites)))
    #    element.click()

        time.sleep(5)


        #Hover_Sites:
        element7 = self.driver.find_element_by_xpath("/html//div[@id='root']/section/section/section[@class='ant-layout']/main[@class='ant-layout-content']//div[@class='ant-tabs-content ant-tabs-content-animated ant-tabs-top-content']/div[3]//div[@class='ant-table-body']/table[@class='ant-table-fixed']/tbody/tr[3]//span[.='BMWsite']")
        actions = ActionChains(self.driver)
        actions.move_to_element(element7)
        actions.perform()

        wait = WebDriverWait(self.driver, 15)
        element8 = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.ClickCarPark)))
        actions.move_to_element(element8)
        actions.perform()
        element8.click()


        time.sleep(5)



'''    def Click_SitesDetails(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.SiteName)))
        element.send_keys("ABABA")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.SiteId)))
        element.send_keys("CDCDCD")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Status)))
        element.click()
        element = self.driver.find_element_by_xpath("//li[contains(text(),'Active')]")
        element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.BuildingName)))
        element.send_keys("RRRR")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AddressLine1)))
        element.send_keys("19th Street")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AddressLine2)))
        element.send_keys("DownCourt")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Town)))
        element.send_keys("QWERTY")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.County)))
        element.send_keys("RedField")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.PostCode)))
        element.send_keys("QWERTY09999")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Country)))
        element.click()
        element = self.driver.find_element_by_xpath("//li[contains(text(),'UK')]")
        element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Title)))
        element.click()
        element = self.driver.find_element_by_xpath("(//li[contains(text(),'Mr')])[1]")
        element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.FirstName)))
        element.send_keys("Jhames")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.LastName)))
        element.send_keys("Robert")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Email)))
        element.send_keys("jhames.robert777@gmail.com")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.MobileNumber)))
        element.send_keys("9090909090")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.LandLine)))
        element.send_keys("0101909090")

        time.sleep(10)

#        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AddClientsSubmit)))
#        element.click()
'''