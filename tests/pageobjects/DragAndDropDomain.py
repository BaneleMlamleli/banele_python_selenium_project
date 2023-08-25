from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from selenium.webdriver import ActionChains
from toolium.pageelements import *
import time

class DragAndDrop(PageObject):
    # def init_page_elements(self):
    #     self.box_a = PageElements(By.XPATH, "//div[@id='column-a']")
    #     self.box_b = PageElements(By.XPATH, "//div[@id='column-b']")
    
    def home_page(self):
        """ Open url in browser
        :returns: this page object instance
        """
        self.driver.get('{}'.format(self.config.get('Test', 'url')))
        self.driver.maximize_window()
        return self
    
    def click_on_link(self, drag_and_drop):
        """ 
        click on the link to open the page
        """
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{drag_and_drop}']").click()
        time.sleep(3)
        
    def drag_and_drop_to_swap_boxes(self):
        # NOTE: I think there is a bug on the Selenium Drag and Drop
        self.box_a = self.driver.find_element(By.XPATH, "//div[@id='column-a']")
        self.box_b = self.driver.find_element(By.XPATH, "//div[@id='column-b']")
        
        ActionChains(self.driver).drag_and_drop(self.box_a, self.box_b).perform()
        time.sleep(3)
        