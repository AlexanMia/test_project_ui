import pytest

from enums.enum_endpoints import ENDPOINTS, URL
from enums.error_messages_enum import ErrorMessages
from pages.textbox_page import TextboxPage


class TestTextboxes:

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    def test_fill_in_textboxes(self, driver):
        """
        This test fills textboxes with generated person info
        and checks text in textbox is matched with generated one

        :param driver: webdriver
        """
        textbox_page = TextboxPage(driver, f'{URL.DEMOQA.value}{ENDPOINTS.TEXTBOX.value}')
        textbox_page.open()

        person = textbox_page.fill_all_fields_in_textboxes()

        person_output = textbox_page.get_filled_text_from_textboxes()

        assert person.full_name == person_output.full_name, ErrorMessages.EXPECTED_TEXT.value.format(
            person.full_name, person_output.full_name)

        assert person.email == person_output.email, ErrorMessages.EXPECTED_TEXT.value.format(
            person.email, person_output.email)

        assert person.current_address == person_output.current_address, ErrorMessages.EXPECTED_TEXT.value.format(
            person.current_address, person_output.current_address)

        assert person.permanent_address == person_output.permanent_address, ErrorMessages.EXPECTED_TEXT.value.format(
            person.permanent_address, person_output.permanent_address)
