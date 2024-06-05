import random

from locators.locators import CheckboxPageLocators
from pages.base_page import BasePage


class CheckboxPage(BasePage):
    locators = CheckboxPageLocators()

    def open_full_list_checkboxes(self):
        self.wait_element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_checkbox_list = self.wait_elements_are_visible(self.locators.ITEM_CHECKBOX_LIST)
        for _ in range(10):
            random_item = item_checkbox_list[random.randint(1, len(item_checkbox_list)-1)]
            self.scroll_to_element(random_item)
            random_item.click()

    def get_chosen_checkboxes(self) -> str:
        checked_list = self.wait_elements_are_present(self.locators.CHECKED_CHECKBOXES)
        list_checked_names = []
        for checkbox in checked_list:
            title_checkbox = checkbox.find_element(*self.locators.TITLE_ITEM)
            list_checked_names.append(title_checkbox.text)
        return (str(list_checked_names).replace(" ", "")
                                       .replace("doc", "")
                                       .replace(".", "")
                                       .lower())

    def get_output_chosen_checkboxes(self) -> str:
        resul_chosen_checkboxes = self.wait_elements_are_present(self.locators.OUTPUT_CHOSEN_CHECKBOXES)
        list_output_checkboxes = []
        for item in resul_chosen_checkboxes:
            list_output_checkboxes.append(item.text)
        return str(list_output_checkboxes).replace(" ", "").lower()
