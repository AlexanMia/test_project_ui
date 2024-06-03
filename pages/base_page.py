from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: webdriver, url: str):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5) -> WebElement:
        """
        Waits for the element to be visible on the page for the specified time
        and returns the element object if it becomes visible.

        :param locator: Element Locator
        :param timeout: Waiting time in seconds
        :return: WebElement
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_present(self, locator, timeout=5) -> WebElement:
        """
        Waits for the element to be located in the DOM for the specified time
        and returns the element object if it is located in the DOM.
        Does not necessarily mean that the element is visible.

        :param locator: Element Locator
        :param timeout: Waiting time in seconds
        :return: WebElement
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_not_visible(self, locator, timeout=5) -> WebElement:
        """
        The `element_is_not_visible` method is used to wait for the specified element (`WebElement')
        to become invisible on a web page.

        :param locator: Element Locator
        :param timeout: Waiting time in seconds
        :return: WebElement
        """
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5) -> WebElement:
        """
        Waits for the element to be visible on the page and clickable for the specified time
        and returns the element object.

        :param locator: Element Locator
        :param timeout: Waiting time in seconds
        :return: WebElement
        """
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, element):
        """
        The method uses the execution of a JavaScript script by the web driver (`self.driver`)
        to scroll the page to the specified element.
        The script `argument[0].scrollIntoView()` scrolls the page
        to make the specified element (`argument[0]`) visible in the viewport.

        :param element: WebElement
        """
        self.driver.execute_script("argument[0].scrollIntoView();", element)

    @staticmethod
    def extract_text_from_element(element) -> str:
        """
        The `extract_text_from_element' method is used
        to extract text from a specified element (`WebElement') on a web page.

        :param element: WebElement
        :return: string
        """
        return element.text

