from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def click_checkboxes_link(self):
        self.driver.find_element(By.LINK_TEXT, 'Checkboxes').click()

    def click_file_upload_link(self):
        # Update this line to use XPath
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'File Upload')]").click()
