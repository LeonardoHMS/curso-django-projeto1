import os

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def make_edge_browser(*options):
    edge_options = webdriver.EdgeOptions()
    service = Service(EdgeChromiumDriverManager().install())

    if options is not None:
        for option in options:
            edge_options.add_argument(option)

    if os.environ.get('SELENIUM_HEADLESS') == '1':
        edge_options.add_argument('--headless')

    browser = webdriver.Edge(service=service, options=edge_options)

    return browser


if __name__ == '__main__':
    browser = make_edge_browser()
    browser.get('https://www.google.com.br')
    browser.quit()
