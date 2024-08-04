import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser_wrapper.base_page import BasePage


class InboxPage(BasePage):
    COMMENTS_BUTTON = '//a[@data-note-type="project_note"]'
    COMMENTS_INPUT = '//p[@class="is-empty is-editor-empty"]'
    COMMENTS_SUBMIT_BUTTON = '//button[@data-track="comments|add_comment"]'
    COMMENT_CONTAINER = './/div[@class="note_text has_avatar"]'
    STAM_COMMENT = './/div[@class="note_content"]'
    ####################################################################################################################
    COMMENT_MENU = '//button[@aria-label="Comment options"]'
    COPY_COMMENT_BUTTON = '//div[text()="Copy text"]'  #'//div[@data-tabindex="0"][1]'
    COMMENT_COPIED = '//div[@role="textbox"]//p[text()="0000"]'
    ####################################################################################################################
    ADD_EMOJI_BUTTON = '//button[@aria-label="Add a reaction"]'
    LIKE_EMOJI_BUTTON = '//img[@alt="👍"][1]'
    REACTION_EMOJI = '//button[@class="reaction_holder"]'

    def click_on_comments_button(self):
        comments_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COMMENTS_BUTTON)))
        comments_button.click()

    def fill_new_comment(self, comment):
        comment_input = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.COMMENTS_INPUT)))
        comment_input.clear()
        comment_input.send_keys(comment)

    def click_on_comments_submit_button(self):
        comment_submit_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.COMMENTS_SUBMIT_BUTTON)))
        comment_submit_button.click()

    def create_a_new_comment_process_flow(self, comment):
        self.click_on_comments_button()
        self.fill_new_comment(comment)
        self.click_on_comments_submit_button()

    # def is_comment_displayed(self, comment):
    #     if self._comment_visibility.is_displayed():
    #         return True
    #     return False

    def get_comment_containers(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.COMMENT_CONTAINER)))
        comment_containers = self._driver.find_elements(By.XPATH, self.COMMENT_CONTAINER)
        return comment_containers

    def get_comment_from_container(self, container):
        return container.find_element(By.XPATH, self.STAM_COMMENT)

    def get_comments(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.STAM_COMMENT)))
        comments = self._driver.find_elements(By.XPATH, self.STAM_COMMENT)
        return comments

    def comment_is_displayed(self, comment):
        return self._driver.find_element(By.XPATH, f'//p[text()="{comment}"]').is_displayed()

    ####################################################################################################################
    def however_to_comment_menu(self):
        ActionChains(self._driver).move_to_element(self._driver.find_element(By.XPATH, self.STAM_COMMENT)).perform()

    def hover_to_comment_container_menu(self, container):
        ActionChains(self._driver).move_to_element(container).perform()

    def click_on_comment_menu(self):
        comment_menu_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.COMMENT_MENU)))
        comment_menu_button.click()

    def click_on_copy_comment_button(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COPY_COMMENT_BUTTON))).click()

        # copy_button = self._driver.find_element(By.XPATH, self.COPY_COMMENT_BUTTON)
        # copy_button.click()

    def paste_comment(self):
        # actions = ActionChains(self._driver)
        # actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        ActionChains(self._driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    # def chick_if_the_comment_is_paste(self):
    #     self._comment_visibility = WebDriverWait(self._driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, self.COMMENT_COPIED)))
    #     if self._comment_visibility.is_displayed():
    #         return True

    def add_and_copy_new_comment_process_flow(self, comment):
        self.hover_to_comment_container_menu(comment)
        self.click_on_comment_menu()
        self.click_on_copy_comment_button()
        # self.fill_new_comment(comment)
        self.paste_comment()
        self.click_on_comments_submit_button()

    ####################################################################################################################

    def click_on_emoji_button(self):
        emoji_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.ADD_EMOJI_BUTTON)))
        emoji_button.click()

    def click_on_like_emoji_button(self):
        like_emoji = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.ADD_EMOJI_BUTTON)))
        like_emoji.click()

    def add_emoji_process_flow(self):
        self.however_to_comment_menu()
        self.click_on_emoji_button()
        self.click_on_like_emoji_button()

    def emoji_reaction_is_displayed(self):
        self._emoji_reaction = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.REACTION_EMOJI)))
        if self._emoji_reaction.is_displayed():
            return True
