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
        self.ManCo = "//div[@class = 'ant-tabs-tab-active ant-tabs-tab']"
        self.AddManCo = "//button[@class='ant-btn permit-primary-btn add-to-collection-btn']"
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
        element.send_keys("Test_1")
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
        element.send_keys("ABC")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.LastName)))
        element.send_keys("Q")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Email)))
        element.send_keys("abc.q@gmail.com")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.MobileNumber)))
        element.send_keys("9809809809")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.LandLine)))
        element.send_keys("0805490210")

        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AddManCoSubmit)))
        element.click()

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.ManCo)))
        element.click()


        #Hover_ManCo_To_Clients:
        wait = WebDriverWait(self.driver, 30)
        element1 = wait.until(self.driver.find_element_by_xpath("//*[contains(text(), 'Test_01')]"))
        actions = ActionChains(self.driver)
        actions.move_to_element(element1)
        actions.perform()

        element2 = self.driver.find_element_by_xpath("//div[@class='ant-col addIcon']")
        actions.move_to_element(element2)
        actions.perform()
        element2.click()


        # 2.Clients Details:
        self.Clients = "//div[@class=' ant-tabs-tab'][1]"
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




    def Click_ClientsDetails(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.ClientName)))
        element.send_keys("Test_2")
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



        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.Clients)))
        element.click()



        #Hover_Clients_To_Sites:
        wait = WebDriverWait(self.driver, 30)
        element3 = wait.until(self.driver.find_element_by_xpath("//*[contains(text(), 'Test_2')]"))
        actions = ActionChains(self.driver)
        actions.move_to_element(element3)
        actions.perform()

        element4 = self.driver.find_element_by_xpath("//div[@class='ant-col addIcon']")
        actions.move_to_element(element4)
        actions.perform()
        element4.click()



        # 3.Site Details:
        self.Sites = "(//div[@class = ' ant-tabs-tab'])[2]"
        self.AddSites = "//button[@class = 'ant-btn permit-primary-btn add-to-collection-btn']"
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
        self.S_FirstName = "//Input[@name = 'contacts[0].firstName']"
        self.S_LastName = "//Input[@name = 'contacts[0].lastName']"
        self.S_Email = "//Input[@name = 'contacts[0].email']"
        self.CountryCode = "//Input[@name = 'countryCode']"
        self.S_MobileNumber = "//Input[@name = 'contacts[0].mobileNumber']"
        self.S_LandLine = "//Input[@name = 'contacts[0].landLine']"
        self.AddSitesSubmit = "//button[@class = 'ant-btn permit-primary-btn']"



    def Click_SitesDetails(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.SiteName)))
        element.send_keys("Test_3")
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
        element = self.driver.find_element_by_xpath("(//li[contains(text(),'Mr')])")
        element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.S_FirstName)))
        element.send_keys("Jhames")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.S_LastName)))
        element.send_keys("Robert")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.S_Email)))
        element.send_keys("jhames.robert777@gmail.com")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.S_MobileNumber)))
        element.send_keys("9090909090")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.S_LandLine)))
        element.send_keys("0101909090")


        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AddClientsSubmit)))
        element.click()


        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.Sites)))
        element.click()


        #Hover_Sites_To_CarParks:
        wait = WebDriverWait(self.driver, 30)
        element5 = wait.until(self.driver.find_element_by_xpath("(//*[contains(text(), 'Test_3')])[1]"))
        actions = ActionChains(self.driver)
        actions.move_to_element(element5)
        actions.perform()

        element6 = self.driver.find_element_by_css_selector("[role='tabpanel']:nth-of-type(3) .ant-row-flex-middle:nth-of-type(1) > div:nth-of-type(1) [src]")
        actions.move_to_element(element6)
        actions.perform()
        element6.click()


        # 4.Car Park:
        self.CarPark = "(//div[@class = ' ant-tabs-tab'])[3]"
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


        self.OpeningTimerFrom = "(//input[@class='ant-time-picker-input'])[1]"
        self.OpeningTimingFrom = "(//input[@class='ant-time-picker-panel-input'])[1]"
        self.OpeningTimerTo = "(//input[@class='ant-time-picker-input'])[2]"
        self.OpeningTimingTo = "(//input[@class='ant-time-picker-panel-input'])[2]"

        self.EnforcementFullDay = ".ant-row-flex-space-between:nth-child(5) .ant-radio-button-wrapper-checked > span:nth-of-type(2)"
        self.EnforcementDuration = ".ant-row-flex-space-between:nth-child(5) .ant-radio-button-wrapper:nth-of-type(2) > span:nth-of-type(2)"

        self.EnforcementDurationTimerFrom = "(//input[@class='ant-time-picker-input'])[3]"
        self.EnforcementDurationTimeFrom = "(//input[@class='ant-time-picker-panel-input'])[1]"
        self.EnforcementDurationTimerTo = "(//input[@class='ant-time-picker-input'])[4]"
        self.EnforcementDurationTimeTo = "(//input[@class='ant-time-picker-panel-input'])[2]"


        self.ConsiderationPeriod = "//Input[@name = 'timingSettings[0].considerationPeriod']"
        self.GracePeriodPeriod = "//Input[@name = 'timingSettings[0].gracePeriod']"
        self.GracePeriodPeriodBlueBadge = "//Input[@name = 'timingSettings[0].gracePeriodBlueBadge']"

        self.FreePeriodPerVisit = ".ant-row-flex-space-between:nth-child(8) .ant-radio-button-wrapper:nth-of-type(1) > span:nth-of-type(2)"
        self.FreePeriodPerDay = ".ant-row-flex-space-between:nth-child(8) .ant-radio-button-wrapper-checked > span:nth-of-type(2)"

        self.FreePeriodFromTimer = "(//input[@class='ant-time-picker-input'])[5]"
        self.FreePeriodFromTime = "(//input[@class='ant-time-picker-panel-input'])[1]"
        self.FreePeriodToTimer = "(//input[@class='ant-time-picker-input'])[6]"
        self.FreePeriodToTime = "(//input[@class='ant-time-picker-panel-input'])[2]"
        self.AddCarParkSubmit = "//button[@class = 'ant-btn permit-primary-btn']"


    def Click_CarParkDetails(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.CarParkName)))
        element.send_keys("Test_4")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Mid)))
        element.send_keys("9100101")

        wait = WebDriverWait(self.driver, 20)
        element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.MonDay)))
        element.click()

        element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.ThursDay)))
        element.click()

        element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.BankHolidays)))
        element.click()

        wait = WebDriverWait(self.driver, 20)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.OpeningTimerFrom)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.OpeningTimingFrom)))
        element.send_keys("08:10")
        element.click()

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.OpeningTimerTo)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.OpeningTimingTo)))
        element.send_keys("23:30")
        element.click()


        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.EnforcementDuration)))
        element.click()

        wait = WebDriverWait(self.driver, 20)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.EnforcementDurationTimerFrom)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.EnforcementDurationTimeFrom)))
        element.click()
        element.send_keys("08:10")
        element.click()

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.EnforcementDurationTimerTo)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.EnforcementDurationTimeTo)))
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
        wait = WebDriverWait(self.driver, 10)

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

        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AddCarParkSubmit)))
        element.click()

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.CarPark)))
        element.click()


        #Hover_CarParks_To_Devices:
        wait = WebDriverWait(self.driver, 30)
        element7 = wait.until(self.driver.find_element_by_xpath("(//*[contains(text(), 'Test_4')])[4]"))
        actions = ActionChains(self.driver)
        actions.move_to_element(element7)
        actions.perform()

        element8 = self.driver.find_element_by_css_selector(".ant-col.link-display")
        actions.move_to_element(element8)
        actions.perform()
        element8.click()





        # 5.Device:
        self.NextPage = "//button[@class='ant-btn permit-primary-btn']"

        self.CameraName = "//Input[@name = 'deviceName']"
        #self.CameraType = "//button[@name = 'ant-btn device-btn ']"
        self.Make = "//Input[@name = 'make']"
        self.Model = "//Input[@name = 'model']"
        self.ExternalReference = "//Input[@name = 'reference']"
        self.InstallationDateSelect = "(//input[@class='ant-calendar-picker-input ant-input'])[1]"
        self.InstallationDate = "(//input[@class='ant-calendar-input '])[1]"
        self.WarrantyExpirationDateSelect = "(//input[@class='ant-calendar-picker-input ant-input'])[2]"
        self.WarrantyExpirationDate = "(//input[@class='ant-calendar-input '])[2]"

        self.SerialNo = "input[name='serialNo']"
        self.AuthenticationToken = "//Input[@name = 'token']"
        self.IPAddress = "//Input[@name = 'ip']"

        self.FacingDirection = "(//div [@class='ant-select-selection__placeholder'])[1]"
        self.DefaultDirection = "(//div [@class='ant-select-selection__placeholder'])[2]"

        self.ActivationDateSelect = "(//input[@class='ant-calendar-picker-input ant-input'])[3]"
        self.ActivationDateEnter = ".ant-calendar-input"

        self.ActivationTime = "(//input[@class='ant-time-picker-input'])[1]"
        self.ActivationTimeEnter = "(//input[@class='ant-time-picker-panel-input'])[1]"

        self.DeactivationDateSelect = "(//input[@class='ant-calendar-picker-input ant-input'])[4]"
        self.DeactivationDateEnter = ".ant-calendar-input"

        self.DeactivationTime = "(//input[@class='ant-time-picker-input'])[2]"
        self.DeactivationTimeEnter = "(//input[@class='ant-time-picker-panel-input'])[2]"

        self.Note = "//Input[@name = 'notes']"
        self.AddDeviceSubmit = "//button[@class = 'ant-btn permit-primary-btn']"
        self.ManCo1 = "//div[@class=' ant-tabs-tab'][1]"



    def Click_DeviceDetails(self):

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.NextPage)))
        element.click()

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.CameraName)))
        element.send_keys("Test_5")
        wait = WebDriverWait(self.driver, 10)
        #element = wait.until(ec.presence_of_element_located((By.XPATH, self.CameraType)))
        #element.click()
        #element = self.driver.find_element_by_xpath("//li[contains(text(),'Digital')]")
        #element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.Make)))
        element.send_keys("LMT")
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
        element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.SerialNo)))
        element.click()
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
        element = self.driver.find_element_by_xpath("//li[contains(text(),'In')]")
        element.click()
        element.click()


        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.ActivationDateSelect)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.ActivationDateEnter)))
        element.send_keys("15-05-2020")
        element.click()

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.ActivationTime)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.ActivationTimeEnter)))
        element.send_keys("11:30")
        element.click()


        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.DeactivationDateSelect)))
        element.click()
        element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.DeactivationDateEnter)))
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


        element = wait.until(ec.presence_of_element_located((By.XPATH, self.AddManCoSubmit)))
        element.click()


        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.ManCo1)))
        element.click()



