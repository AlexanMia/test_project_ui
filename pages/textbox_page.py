from helpers.generators import generated_info_person
from helpers.helper_methods import HelperMethods
from locators.locators import TextboxLocators
from pages.base_page import BasePage


class TextboxPage(BasePage):
    locators = TextboxLocators()
    helper = HelperMethods()

    def fill_all_fields_in_textboxes(self) -> tuple:
        """
        This method fills all fields on a form with generated person information and submits the form.
        And return this data

        :return: tuple with generated person info for further checks
        """
        person_info = next(generated_info_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.BUTTON_SUBMIT).click()

        return full_name, email, current_address, permanent_address

    def get_filled_text_from_textboxes(self) -> tuple:
        """
        This method extract text from webelements with info filled in textboxes
        with help helper methods .text and .split (separated into individual methods for reuse)

        :return: tuple of filled info in textboxes
        """

        full_name = self.helper.split_string(
            self.extract_text_from_element(
                self.element_is_present(
                    self.locators.CREATED_FULL_NAME)), ":")[1]

        email = self.helper.split_string(
            self.extract_text_from_element(
                self.element_is_present(
                    self.locators.CREATED_EMAIL)), ":")[1]

        current_address = self.helper.split_string(
            self.extract_text_from_element(
                self.element_is_present(
                    self.locators.CREATED_CURRENT_EMAIL)), ":")[1]

        permanent_address = self.helper.split_string(
            self.extract_text_from_element(
                self.element_is_present(
                    self.locators.CREATED_PERMANENT_ADDRESS)), ":")[1]

        return full_name, email, current_address, permanent_address
