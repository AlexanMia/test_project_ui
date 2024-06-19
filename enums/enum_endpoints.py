from enum import Enum


class URL(Enum):
    DEMOQA: str = "https://demoqa.com"


class ENDPOINTS(Enum):
    TEXTBOX: str = "/text-box"
    CHECKBOX: str = "/checkbox"
