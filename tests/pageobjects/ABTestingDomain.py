from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
import time

class ABTesting(PageObject):
        
    def home_page(self):
        """
        open the home page
        """
        # self.driver.get('https://the-internet.kineticskunk.co.za/')
        self.driver.get('{}'.format(self.config.get('Test', 'url')))
        time.sleep(3)
        return self
    
    def click_on_link(self, ab_testing):
        """ 
        click on the link to open the page
        """
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{ab_testing}']").click()
        time.sleep(3)
    
    def redirected_to_the_abTestVariation_page(self):
        """
        confirming the page is opened
        """
        
        assert self.driver.find_element(By.xpath, "//h3[normalize-space()='A/B Test Variation 1']").is_displayed() == False, 'Error. Page did not redirect or locator is incorrect'
        
        time.sleep(3)