from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    timeout = 5

    def __init__(self, driver: webdriver, url: str):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def wait_element_is_visible(self, locator: tuple[str, str], timeout: int = timeout) -> WebElement:
        """
        Waits for the element to be visible on the page for the specified time
        and returns the element object if it becomes visible.

        :param locator: Element Locator
        :param timeout: Waiting time in seconds
        :return: WebElement
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_elements_are_visible(self, locator: tuple[str, str], timeout: int = timeout) -> list:
        """
        Waits for the elements to be visible on the page for the specified time
        and returns list of the elements object if they become visible.

        :param locator: Element Locator
        :param timeout: Waiting time in seconds
        :return: list of WebElements
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def wait_element_is_present(self, locator: tuple[str, str], timeout: int = timeout) -> WebElement:
        """
        Waits for the element to be located in the DOM for the specified time
        and returns the element object if it is located in the DOM.
        Does not necessarily mean that the element is visible.

        :param locator: Element Locator
        :param timeout: Waiting time in seconds
        :return: WebElement
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_elements_are_present(self, locator: tuple[str, str], timeout: int = timeout) -> list:
        """
        Waits for the element to be located in the DOM for the specified time
        and returns the element object if it is located in the DOM.
        Does not necessarily mean that the element is visible.

        :param locator: Element Locator
        :param timeout: Waiting time in seconds
        :return: list of WebElements
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def wait_element_is_not_visible(self, locator: tuple[str, str], timeout: int = timeout) -> bool | WebElement:
        """
        The `element_is_not_visible` method is used to wait for the specified element ('WebElement')
        to become invisible on a web page.

        :param locator: Element Locator
        :param timeout: Waiting time in seconds
        :return: WebElement or bool
        """
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def wait_element_is_clickable(self, locator: tuple[str, str], timeout: int = timeout) -> WebElement:
        """
        Waits for the element to be visible on the page and clickable for the specified time
        and returns the element object.

        :param locator: Element Locator
        :param timeout: Waiting time in seconds
        :return: WebElement
        """
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, element: WebElement):
        """
        The method uses the execution of a JavaScript script by the web driver (`self.driver`)
        to scroll the page to the specified element.
        The script `argument[0].scrollIntoView()` scrolls the page
        to make the specified element (`argument[0]`) visible in the viewport.

        :param element: WebElement
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
