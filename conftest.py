import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


# В этом примере мы создаем экземпляр `webdriver.ChromeOptions` и передаем его в конструктор `webdriver.Chrome`.
# WebDriver будет автоматически использовать вебдрайвер, который установлен в системе.
# @pytest.fixture()
# def driver():
#     options = webdriver.ChromeOptions()
#     yield webdriver.Chrome(options=options)
