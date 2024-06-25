from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

##defined all the locators
## to locate the disappearing pop-up message used setTimeout debugger function to freeze the page and find the webelement locators
class web_page:
    def __init__(self, driver):
        self.driver = driver
        self.username_input=(By.NAME,"username")
        self.password_input=(By.NAME,"password")
        self.login_button=(By.CSS_SELECTOR,"button[type='Submit']")
        self.pim_menu=(By.LINK_TEXT,"PIM")
        self.add_item=(By.CSS_SELECTOR,"button[class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.fn_input=(By.CSS_SELECTOR,"input[name='firstName']")
        self.ln_input=(By.CSS_SELECTOR,"input[name='lastName']")
        self.empid_input=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input")
        self.save_button=(By.CSS_SELECTOR,"button[class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
        self.success_message=(By.XPATH,"// *[ @ id = 'oxd-toaster_1'] / div / div[1] / div[2] / p[2]")
        self.existing_emp=(By.XPATH,"// *[ @ id = 'app'] / div[1] / div[2] / div[2] / div / div[2] / div[3] / div / div[2] / div[5] / div")
        self.driving_lic=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input")
        self.emp_delete=(By.CSS_SELECTOR,"i[class='oxd-icon bi-trash']")
        self.ok_del=(By.XPATH,"//*[@id='app']/div[3]/div/div/div/div[3]/button[2]")
        self.update_message=(By.CSS_SELECTOR,"p[class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']")
        self.del_message=(By.XPATH,"//*[@id='oxd-toaster_1']/div/div[1]/div[2]/p[2]")
        self.popup_dialog=(By.XPATH,"//*[@id='app']/div[3]/div/div/div")
    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def login_page(self,username,password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_input)).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_input)).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.login_button)).click()

    def pim_module_add(self,firstname,lastname,empid):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.pim_menu)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.add_item)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.fn_input)).send_keys(firstname)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ln_input)).send_keys(lastname)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.empid_input)).send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.empid_input)).send_keys(empid)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.save_button)).click()
        self.success_text=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.success_message)).text
        print(self.success_text) ##validated by printing the pop-up message

    def pim_module_edit(self,drivinglicense):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.pim_menu)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.existing_emp)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.driving_lic)).send_keys(drivinglicense)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.save_button)).click()
        self.update_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.update_message)).text
        print(self.update_text) ##validated by printing the pop-up message

    def pim_emp_delete(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.pim_menu)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.emp_delete)).click()
        ##the delete confirmation dialog box is with in the window(modal dialog box) so used visibility of element
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.popup_dialog))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.popup_dialog))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ok_del)).click()
        self.del_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.del_message)).text
        print(self.del_text)##validated by printing the pop-up message





