import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Webpage import web_page
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    time.sleep(2)
    driver.close()
    driver.quit()

##Test Objective - Successful login page
## Launched the website and logged in with the correct uername and password
def test_Login_01(driver):
    web_page_obj1=web_page(driver)
    web_page_obj1.open_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    web_page_obj1.login_page("Admin","admin123")
    assert "Dashboard" in driver.page_source ##validated with the sucessfully updated message

##Test Objective - Invalid Employee login
## Launched the website and logged in with the uername and password (incorrect, which has been provided in the case sheet)
def test_Login_02(driver):
    web_page_obj2 = web_page(driver)
    web_page_obj2.open_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    web_page_obj2.login_page("Admin", "Invalid password")
    assert "Invalid credentials" in driver.page_source ##validated with the invalid credential message

##Test Objective - Add a new employee in the PIM module
##Launched the website and logged in to the admin page
##Added employee details and saved
##validated and printed the message in the pim_module_add function
def test_PIM_01(driver):
    web_page_obj3=web_page(driver)
    web_page_obj3.open_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    web_page_obj3.login_page("Admin", "admin123")
    web_page_obj3.pim_module_add("Mallika","V","2014")

##Test Objective - edit an existing employee in PIM module
##Launched the website and logged in to the admin page
##edited the existing employee details
##validated and printed the message in the pim_module_edit function
def test_PIM_02(driver):
    web_page_obj4=web_page(driver)
    web_page_obj4.open_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    web_page_obj4.login_page("Admin", "admin123")
    web_page_obj4.pim_module_edit("87656") ##edited the driving license field by passing the value


##Test Objective - edit an existing employee in PIM module
##Launched the website and logged in to the admin page
##deleted the existing employee details
##validated and printed the message in the pim_emp_delete function
def test_PIM_03(driver):
    web_page_obj5 = web_page(driver)
    web_page_obj5.open_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    web_page_obj5.login_page("Admin", "admin123")
    web_page_obj5.pim_emp_delete()