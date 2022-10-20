import pytest
import selenium.webdriver as webdriver

#driver_path="C:\\Users\\skone\\OneDrive - PROSOL GESTION\\Documents\\formation_tests"
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#executable_path=driver_path

@pytest.fixture
def browser():
    #driver= webdriver.Chrome()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
