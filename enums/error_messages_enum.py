from enum import Enum


class ErrorMessages(str, Enum):
    EXPECTED_TEXT: str = "Expected text to be '{}' but got '{}'"
