from selenium.webdriver.common.by import By

class CheckboxesPage:
    def __init__(self, driver):
        self.driver = driver

    def get_title_text(self):
        return self.driver.find_element(By.TAG_NAME, 'h3').text

    def is_checkbox_selected(self, index):
        checkbox = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')[index - 1]
        return checkbox.is_selected()
