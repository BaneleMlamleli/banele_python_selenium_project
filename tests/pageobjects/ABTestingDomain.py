from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from selenium.webdriver import ActionChains
from toolium.pageelements import *
import time

class ABTesting(PageObject):
    
    def init_page_elements(self):
        self.screenshot_path = "C:\\Users\\BaneleMlamleli\\Documents\\Programming\\python\\banele_python_selenium_project\\tests\\screenshot\\"
        
    def home_page(self):
        """
        open the home page
        """
        self.driver.get('{}'.format(self.config.get('Test', 'url')))
        self.driver.maximize_window()
        time.sleep(3)
        return self
    
    def click_on_link(self, ab_testing):
        """ 
        click on the link to open the page
        """
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{ab_testing}']").click()
        self.driver.save_screenshot(self.screenshot_path+'ab_testing.png')
    
    def redirected_to_the_abTestVariation_page(self):
        """
        confirming the page is opened
        """
        time.sleep(3)
        assert self.driver.find_element(By.xpath, "//h3[normalize-space()='A/B Test Variation 1']").is_displayed() == False, 'Error. Page did not redirect or locator is incorrect'