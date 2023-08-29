from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from toolium.pageelements import *
import time

class DropDownList(PageObject):
    
    def init_page_elements(self):
        self.screenshot_path = "C:\\Users\\BaneleMlamleli\\Documents\\Programming\\python\\banele_python_selenium_project\\tests\\screenshot\\"
        self.select = Select(By.ID, 'dropdown')
        
    def home_page(self):
        """ Open url in browser
        :returns: this page object instance
        """
        self.driver.get('{}'.format(self.config.get('Test', 'url')))
        self.driver.maximize_window()
        return self
    
    def click_on_link(self, drop_down):
        """ 
        click on the link to open the page
        """
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{drop_down}']").click()
        time.sleep(2)
    
    def drop_down_option(self):
        self.driver.find_element(By.XPATH, "//select[@id='dropdown']").click()
        time.sleep(1)
        self.driver.save_screenshot(self.screenshot_path+'drop_down_list.png')
        self.driver.find_element(By.XPATH, "//option[normalize-space()='Option 1']").click()
        time.sleep(2)