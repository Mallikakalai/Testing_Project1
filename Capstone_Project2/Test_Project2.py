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

##Test Objective - Forgot password link validation
## Launched the website, used forgot login button and provided user name and clicked reset button
##validated the output in the reset_window function
def test_PIM_01(driver):
    web_page_obj1=web_page(driver)
    web_page_obj1.open_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    web_page_obj1.forgot_login()
    web_page_obj1.reset_window("Mallika")

##Test objective to validate the title and the header menus are present in the admin page
##launched the website and logged in to the page
##navigated to admin page
def test_PIM_02(driver):
    web_page_obj2=web_page(driver)
    web_page_obj2.open_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    web_page_obj2.login_page("Admin","admin123")
    web_page_obj2.admin_menu()
    web_page_obj2.title_validation("OrangeHRM") ##Validated the title
    ##created a list with the options to validate
    admin_options=["User Management","Job","Organization","Qualifications","Nationalities","Corporate Branding","Configuration"]
    web_page_obj2.admin_page_options(admin_options)

##Test objective to validate the side panel menus are present in the admin page
##launched the website and logged in to the page
##navigated to admin page
def test_PIM_03(driver):
    web_page_obj3 = web_page(driver)
    web_page_obj3.open_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    web_page_obj3.login_page("Admin", "admin123")
    web_page_obj3.admin_menu()
    ##created a list with the options to validate
    admin_sidepanel=["Admin","PIM","Leave","Time","Recruitment","My Info","Performance","Dashboard","Directory","Maintenance", "Buzz"]
    web_page_obj3.admin_panel_options(admin_sidepanel) ## passed the list argument
