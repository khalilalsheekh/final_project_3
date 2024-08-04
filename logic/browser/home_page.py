import time

from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains as EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from infra.browser_wrapper.base_page import BasePage


class HomePage(BasePage):
    SEARCH_BUTTON = '//button[@aria-label="Search"]'
    SEARCH_BUTTON_INPUT = '//input[@placeholder="Search or type a command…"]'
    GO_TO_UPCOMING_BUTTON = '//div[@aria-labelledby="groupLabel_Navigation"]//span[@class="ElZ8nipNhBcVTHErb8wvnguehEVDW9PB"]'
    SEARCH_COMPLETED_TASKS_BUTTON = '//div[text()="Search completed tasks"]'
    NO_RESULTS_TEXT_FOR_INVALID_TEXT = '//div[text()="No completed tasks matching for “123”"]'
    #################################################################
    PLUS_PROJECT_BUTTON = '//button[@aria-label="My projects menu"]'
    ADD_PROJECT_BUTTON = '//div[text()="Add project"]'
    NEW_NAME_PROJECT_INPUT = '//input[@id="edit_project_modal_field_name"]'
    ADD_PROJECT_SUBMIT_BUTTON = '//button[@type="submit"]'
    MY_PROJECT_HOVER = '//a[@href="/app/projects"]'
    MY_PROJECTS_LIST = '//div[@data-index]'
    MENU_PROJECT_BUTTON = '//button[@aria-label="Project options menu"]'
    INBOX_BUTTON = '//a[@aria-label="Inbox, 0 tasks"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._search_button = self._driver.find_element(By.XPATH, self.SEARCH_BUTTON)
        ##############################################################################################
        self._plus_project_button = self._driver.find_element(By.XPATH, self.PLUS_PROJECT_BUTTON)

    def click_on_search_button(self):
        self._search_button.click()
        time.sleep(10)

    def fill_search_button(self, text):
        search_input = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.SEARCH_BUTTON_INPUT)))
        search_input.send_keys(text)

    def click_on_go_to_upcoming_button_in_search(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.GO_TO_UPCOMING_BUTTON)))
        element.click()

    def search_button_with_input_flow(self, text):
        self.click_on_search_button()
        self.fill_search_button(text)
        self.click_on_go_to_upcoming_button_in_search()
        time.sleep(5)

    def click_on_search_completed_tasks_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_COMPLETED_TASKS_BUTTON)))
        button.click()

    def search_process_unsuccessfully_flow(self, text):
        self.fill_search_button(text)
        self.click_on_search_completed_tasks_button()
        time.sleep(10)

    def no_results_text_is_displayed(self):
        self._no_results_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.NO_RESULTS_TEXT_FOR_INVALID_TEXT)))
        if self._no_results_text.is_displayed():
            return True

    ####################################################################################################################

    def however_to_plus_button(self):
        ActionChains(self._driver).move_to_element(self._driver.find_element(By.XPATH, self.MY_PROJECT_HOVER)).perform()

    def click_on_plus_project_button(self):
        plus_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PLUS_PROJECT_BUTTON)))
        plus_button.click()

    def click_on_add_project_button(self):
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_PROJECT_BUTTON)))
        add_button.click()

    def fill_name_for_new_project_input(self, name):
        new_name = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.NEW_NAME_PROJECT_INPUT)))
        new_name.send_keys(name)

    def click_on_add_project_button_submit(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_PROJECT_SUBMIT_BUTTON)))
        submit_button.click()

    def create_an_new_project_process(self, name):
        self.however_to_plus_button()
        self.click_on_plus_project_button()
        self.click_on_add_project_button()
        self.fill_name_for_new_project_input(name)
        self.click_on_add_project_button_submit()

    def project_name_is_displayed(self, project_name):
        return self._driver.find_element(By.XPATH, f'//span[text()="{project_name}"]').is_displayed()

    ####################################################################################################################
    def click_on_inbox_button(self):
        inbox_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.INBOX_BUTTON)))
        inbox_button.click()

    ####################################################################################################################
