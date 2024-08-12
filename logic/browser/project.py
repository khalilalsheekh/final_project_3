from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser.base_page import BasePage


class Project_ll(BasePage):
    FINAL_PROJECT_BUTTON = '//a[@aria-label="Final Project, 1 task"]'
    FINAL_TASK_BUTTON = '//div[@class = "task_content"]'  # '//div[text()="Final Task"]'
    FINAL_TASK_NAME = '//div[@aria-describedby="a11y_task_name"]//div[contains(@class, "task_content")]'  # '//div[@data-action-hint="task-detail-view-edit"]//div[text()="Final Task"]'
    TASK_DUE_DATE = '//div[@aria-label="Due date"]//span'
    TASK_PROPERTY = '//div[@aria-label="Priority"]//span'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def final_project_button(self):
        final_project_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.FINAL_PROJECT_BUTTON)))
        final_project_button.click()

    def final_task_button(self):
        final_task_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.FINAL_TASK_BUTTON)))
        final_task_button.click()

    def create_project_and_task_flow(self):
        self.final_project_button()
        self.final_task_button()

    def project_name_is_displayed(self):
        return self._driver.find_element(By.XPATH, self.FINAL_PROJECT_BUTTON).is_displayed()

    def task_name_is_displayed(self, task_name):
        return self._driver.find_element(By.XPATH,
                                         f'//div[@class="task-overview-main"]//div[text()="{task_name}"]').is_displayed

    def priority_is_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f'//div[@aria-label="Priority"]//span[text()="P4"]'))).is_displayed()

    def get_final_task_due_date(self):
        return WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.TASK_DUE_DATE))).text

