from enums.enum_endpoints import ENDPOINTS
from enums.error_messages_enum import ErrorMessages
from pages.textbox_page import TextboxPage


class TestTextboxes:

    URL_DEMOQA = "https://demoqa.com"

    def test_fill_in_textboxes(self, driver):
        """
        This test fills texboxes with generated person info
        and checks text in textbox is matched with generated one

        :param driver: webdriver
        """

        textbox_page = TextboxPage(driver, f'{self.URL_DEMOQA}{ENDPOINTS.TEXTBOX.value}')
        textbox_page.open()

        (full_name,
         email,
         current_address,
         permanent_address) = textbox_page.fill_all_fields_in_textboxes()

        (output_full_name,
         output_email,
         output_cur_address,
         output_perm_address) = textbox_page.get_filled_text_from_textboxes()

        assert full_name == output_full_name, ErrorMessages.EXPECTED_TEXT.value.format(full_name, output_full_name)

        assert email == output_email, ErrorMessages.EXPECTED_TEXT.value.format(email, output_email)

        assert current_address == output_cur_address, ErrorMessages.EXPECTED_TEXT.value.format(current_address,
                                                                                               output_cur_address)

        assert permanent_address == output_perm_address, ErrorMessages.EXPECTED_TEXT.value.format(permanent_address,
                                                                                                  output_perm_address)
