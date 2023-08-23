from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from toolium.pageelements import *
import time
class FormAuthentication(PageObject):
        
    def home_page(self):
        """ Open url in browser
        :returns: this page object instance
        """
        self.driver.get('{}'.format(self.config.get('Test', 'url')))
        self.driver.maximize_window()
        return self
    
    def click_on_link(self, add_remove_element):
        """ 
        click on the link to open the page
        """
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{add_remove_element}']").click()