import sys
import os
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.homepage import HomePage
from pages.checkboxes_page import CheckboxesPage
from pages.file_upload_page import FileUploadPage

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope="class")
def setup(request):
     # Get the ChromeDriver path dynamically
    driver_path = os.path.join(os.getcwd(), "drivers", "chromedriver.exe")
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.maximize_window()
    driver.get('http://the-internet.herokuapp.com/')
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestWebApp:
    def test_verify_home_page_title(self):
        homepage = HomePage(self.driver)
        title = homepage.get_title()
        logger.info("Home page title verified")
        assert title == "The Internet", "Home page title does not match"

    def test_verify_checkboxes(self):
        homepage = HomePage(self.driver)
        homepage.click_checkboxes_link()

        checkboxes_page = CheckboxesPage(self.driver)
        title_text = checkboxes_page.get_title_text()
        logger.info("Checkboxes page title verified")
        assert title_text == "Checkboxes", "Page title is not 'Checkboxes'"
        
        checkbox1_status = checkboxes_page.is_checkbox_selected(1)
        checkbox2_status = checkboxes_page.is_checkbox_selected(2)
        logger.info("Checkbox 1 status: %s", checkbox1_status)
        logger.info("Checkbox 2 status: %s", checkbox2_status)
        assert not checkbox1_status, "Checkbox 1 is checked, expected unchecked"
        assert checkbox2_status, "Checkbox 2 is not checked, expected checked"
        
        # Navigate back to the home page
        self.driver.back()

    def test_file_upload(self):
        homepage = HomePage(self.driver)
        
        # Wait for the File Upload link to be clickable
        wait = WebDriverWait(self.driver, 10)
        file_upload_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'File Upload')]")))

        homepage.click_file_upload_link()

        file_upload_page = FileUploadPage(self.driver)

        # Wait for the File Uploader text to be visible
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h3')))
        title_text = file_upload_page.get_title_text()
        logger.info("File Uploader page title verified")
        assert title_text == "File Uploader", "Page title is not 'File Uploader'"
        # Use a generic file path
        file_path = os.path.join(os.getcwd(), "files", "example.txt")
        file_upload_page.upload_file(file_path)
