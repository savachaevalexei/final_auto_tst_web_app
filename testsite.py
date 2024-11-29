from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging, yaml

class TestSearchLocators:
    ids = dict()
    with open ("./locators.yaml") as f:
        locators = yaml.safe_load(f)
        
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])
    
 
class OperationsHelperUI(BasePage):
    
    def enter_text_info_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not Found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True
    
    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True
    
    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text
    
    # ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER
    
    # Ввод логина
    def enter_login(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")
        
    # Ввод пароля    
    def enter_pass(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

        
    # CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK
    
    def click_about_link(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_ABOUT_LINK"], description="LOCATOR_ABOUT_LINK")
              
    # Нажатие на кнопку авторизации  
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="LOCATOR_LOGIN_BTN")

    # GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET 
        
    def get_font_size(self):
        return self.get_element_property(TestSearchLocators.ids['LOCATOR_ABOUT_HEADER'], 'font-size')