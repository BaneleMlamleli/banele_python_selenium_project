from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from toolium.pageelements import *
import time
class FormAuthentication(PageObject):
    
    def init_page_elements(self):
        self.screenshot_path = "C:\\Users\\BaneleMlamleli\\Documents\\Programming\\python\\banele_python_selenium_project\\tests\\screenshot\\"
        self.password = InputText(By.XPATH, "//input[@id='username']", wait=True)
        self.username = InputText(By.XPATH, "//input[@id='password']", wait=True)
        self.loginButton = Button(By.XPATH, "//button[@type='submit']", wait=True)
        self.message = Text(By.XPATH, "//div[@id='flash']", wait=True)
        
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
        time.sleep(3)
    
    def user_enter_login_credentials(self, usrname, passwrd):
        self.utils.wait_until_element_visible(self.username).send_keys(usrname)
        self.utils.wait_until_element_visible(self.password).send_keys(passwrd)
        time.sleep(2)
        
    def login_and_confirm_login_message(self):
        self.driver.save_screenshot(self.screenshot_path+'form_authentication.png')
        self.utils.wait_until_element_clickable(self.loginButton).click()
        # TODO: Check for response message after login
        # msgCorrectLoginDetails = self.utils.wait_until_element_visible(self.message).get_text().contains('You logged into a secure area!')
        # msgIncorrectLoginDetails = self.utils.wait_until_element_visible(self.message).get_text().contains('Your username is invalid!')
        # assert msgCorrectLoginDetails == False, "Incorrect login details"
        time.sleep(2)