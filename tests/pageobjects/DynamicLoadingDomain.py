from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from selenium.webdriver import ActionChains
from toolium.pageelements import *
import time

class DynamicLoading(PageObject):
    def init_page_elements(self):
    #     self.start_button = PageElements(By.XPATH, "//button[normalize-space()='Start']")
        # self.load = PageElements(By.XPATH, "//img[@src='/img/ajax-loader.gif']")
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
        # self.utils.wait_until_element_clickable(self.driver.find_element(By.XPATH, f"//a[normalize-space()='{example_option}']")).click()
        # self.example_opt.click()
        
    def start_button(self):
        # self.utils.wait_until_element_visible(self.start_button).click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Start']").click()
        
    def loader(self):
        self.load = self.driver.find_element(By.XPATH, "//div[@id='loading']").is_displayed() #.get_attribute("value")
        # print("Load value: ", self.load)
        # time.sleep(3)
        # loadValue = self.utils.wait_until_element_present(self.load).get().contains("Loading")
        # print("loadValue: ", loadValue)
        # self.utils.wait_until_element_visible(self.load).get().contains("Loading")
        # self.driver.find_element(By.XPATH, "//img[@src='/img/ajax-loader.gif']").is_displayed()
        # assert self.load
        
    def hello_world(self):
        self.hello_wld = self.driver.find_element(By.XPATH, "//h4[normalize-space()='Hello World!']").is_displayed() #.get_attribute("value")
        # self.hello_wld = self.utils.wait_until_element_visible(self.helloWorld).get().contains("Hello World")
        
        # assert self.hello_wld
        # print("hello_wld value", self.hello_wld)