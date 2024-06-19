import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# @pytest.fixture()
# def driver():
#     options = webdriver.ChromeOptions()
#     # options.add_argument('--headless')
#     service = Service(executable_path=ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)
#     yield driver
#     driver.quit()


# В этом примере мы создаем экземпляр `webdriver.ChromeOptions` и передаем его в конструктор `webdriver.Chrome`.
# WebDriver будет автоматически использовать вебдрайвер, который установлен в системе.
# @pytest.fixture()
# def driver():
#     options = webdriver.ChromeOptions()
#     yield webdriver.Chrome(options=options)


@pytest.fixture(scope="module")
def driver(request):
    browser = request.param if request.param else "chrome"
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        # options.add_argument('--headless')
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    yield driver
    driver.close()
    driver.quit()

