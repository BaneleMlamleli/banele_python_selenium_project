from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from toolium.pageelements import *
import time
class BasicAuth(PageObject):
    
    def init_page_elements(self):
        self.screenshot_path = "C:\\Users\\BaneleMlamleli\\Documents\\Programming\\python\\banele_python_selenium_project\\tests\\screenshot\\"
        
    def home_page(self):
        """ Open url in browser
        :returns: this page object instance
        """
        self.driver.get('{}'.format(self.config.get('Test', 'url')))
        self.driver.maximize_window()
        return self
    
    def click_on_link(self, basicAuth):
        """ 
        click on the link to open the page
        """
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{basicAuth}']").click()
        time.sleep(2)

    def user_credentials_verification(self, username, password):
        completeUrl = 'https://'+username+':'+password+'@the-internet.kineticskunk.co.za/basic_auth'
        print('complete url: ',completeUrl)
        self.driver.get(completeUrl)
        self.driver.save_screenshot(self.screenshot_path+'before_basic_auth.png')
        time.sleep(2)
        
    def login_status(context):
        assert self.driver.find_element(By.XPATH, "//p[contains(text(),'Congratulations! You must have the proper credenti')]").is_displayed() == True, "Successfully logged in"
        
        assert self.driver.find_element(By.XPATH, "//body[contains(text(),'Not authorized')]").is_displayed() == True, "Incorrect login credentials"
        self.driver.save_screenshot(self.screenshot_path+'after_basic_auth.png')
        
        time.sleep(3)
        self.driver.implicitly_wait(200)