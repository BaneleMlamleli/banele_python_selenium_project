from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from toolium.pageelements import *
import time
class AddRemoveElements(PageObject):
    
    def init_page_elements(self):
        self.screenshot_path = "C:\\Users\\BaneleMlamleli\\Documents\\Programming\\python\\banele_python_selenium_project\\tests\\screenshot\\"
        
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
        
    def redirected_to_the_add_remove_button_page(self):
        self.driver.implicitly_wait(5)
        
        # Asserting that the Add button is displayed before pressing it
        assert self.driver.find_element(By.XPATH, "//button[@onclick='addElement()']").is_displayed() == True, "The Add button is displayed"
        
        # clicking the Add button 3 times to add 3 Delete buttons 
        for x in range(1,4):
            self.driver.find_element(By.XPATH, "//button[@onclick='addElement()']").click()
            self.driver.implicitly_wait(1)
            time.sleep(1)
        
        self.driver.save_screenshot(self.screenshot_path+'before_user_clicks_on_the_delete_button.png')
        time.sleep(3)

    def user_clicks_on_the_delete_button(self):
        
        assert self.driver.find_element(By.XPATH, "//div[@id='elements']//button[1]").is_displayed() == True,  "Delete button is not yet displayed on the DOM"
        
        if self.driver.find_element(By.XPATH, "//div[@id='elements']//button[1]").is_displayed():
            self.driver.find_element(By.XPATH, "//div[@id='elements']//button[1]").click() 
        
        self.driver.save_screenshot(self.screenshot_path+'after_user_clicks_on_the_delete_button.png')
        time.sleep(3)