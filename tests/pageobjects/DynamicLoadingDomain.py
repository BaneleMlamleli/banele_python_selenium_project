from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from selenium.webdriver import ActionChains
from toolium.pageelements import *
import time

class DynamicLoading(PageObject):
    def init_page_elements(self):
        self.screenshot_path = "C:\\Users\\BaneleMlamleli\\Documents\\Programming\\python\\banele_python_selenium_project\\tests\\screenshot\\"
        self.load = PageElements(By.XPATH, "//div[@id='loading']")
        self.helloWorld = Texts(By.XPATH, "//h4[normalize-space()='Hello World!']")
        
    def home_page(self):
        """ Open url in browser
        :returns: this page object instance
        """
        self.driver.get('{}'.format(self.config.get('Test', 'url')))
        self.driver.maximize_window()
        return self
    
    def click_on_link(self, dynamic_loading):
        """ 
        click on the link to open the page
        """
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{dynamic_loading}']").click()
    
    def clink_on_example_option(self, example_option):
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{example_option}']").click()
        
    def start_button(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Start']").click()
        
    def loader(self):
        self.load = self.driver.find_element(By.XPATH, "//div[@id='loading']").is_displayed() #.get_attribute("value")
        self.driver.save_screenshot(self.screenshot_path+'dynamic_loading.png')
        
    def hello_world(self):        
        self.driver.save_screenshot(self.screenshot_path+'dynamic_loading.png')
        self.hello_wld = self.driver.find_element(By.XPATH, "//h4[normalize-space()='Hello World!']").is_displayed()