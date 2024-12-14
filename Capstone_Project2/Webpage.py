from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

##defined all the locators
class web_page:
    def __init__(self, driver):
        self.driver = driver
        self.forgot_button=(By.CSS_SELECTOR,"p[class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
        self.dialog_box=(By.XPATH,"//*[@id='app']/div[1]/div[1]/div/form")
        self.dialog_box_title=(By.CSS_SELECTOR,"h6[class='oxd-text oxd-text--h6 orangehrm-forgot-password-title']")
        self.username_input=(By.NAME,"username")
        self.reset_button=(By.CSS_SELECTOR,"button[class='oxd-button oxd-button--large oxd-button--secondary orangehrm-forgot-password-button orangehrm-forgot-password-button--reset']")
        self.admin=(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span")
        self.username_input=(By.NAME,"username")
        self.password_input=(By.NAME,"password")
        self.login_button=(By.CSS_SELECTOR,"button[type='Submit']")
        self.admin_menu_items=(By.LINK_TEXT,"Admin")

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def forgot_login(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.forgot_button)).click()

    def reset_window(self,username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.dialog_box))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dialog_box))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_input)).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.reset_button)).click()
        expected_output=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dialog_box_title)).text
        actual_output="Reset Password link sent successfully"
        assert expected_output==actual_output ##Validated the expected output

    def login_page(self,username,password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_input)).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_input)).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.login_button)).click()

    def admin_menu(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.admin)).click()
    def title_validation(self,pagetitle):
        current_title=self.driver.title
        if current_title==pagetitle:
            print("Correct Page Title")
        else:
            print("Incorrect Page Title")

    def admin_page_options(self,admin_ops):
        for ad_options in admin_ops: ## validating if all the header menu options are present in the admin page
            if ad_options in self.driver.page_source:
                print (ad_options," is available in Admin page")
            else:
                print (ad_options," is not available in Admin page")

    def admin_panel_options(self,admin_panel):
        for ad_panel_ops in admin_panel:## validating if all the side panel menu options are present in the admin page
            if ad_panel_ops in self.driver.page_source:
                print (ad_panel_ops," is available in Admin page")
            else:
                print (ad_panel_ops," is not available in Admin page")










