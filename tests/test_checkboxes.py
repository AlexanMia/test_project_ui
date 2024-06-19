import pytest

from enums.enum_endpoints import ENDPOINTS, URL
from enums.error_messages_enum import ErrorMessages
from pages.checkbox_page import CheckboxPage


class TestCheckBox:

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    def test_choose_checkboxes(self, driver):
        checkbox_page = CheckboxPage(driver, f"{URL.DEMOQA.value}{ENDPOINTS.CHECKBOX.value}")
        checkbox_page.open()
        checkbox_page.open_full_list_checkboxes()
        checkbox_page.click_random_checkbox()
        selected_checkboxes = checkbox_page.get_chosen_checkboxes()
        output_checkboxes = checkbox_page.get_output_chosen_checkboxes()

        assert selected_checkboxes == output_checkboxes, \
            ErrorMessages.EXPECTED_CHOSEN_CHECKBOXES.value.format(selected_checkboxes, output_checkboxes)
