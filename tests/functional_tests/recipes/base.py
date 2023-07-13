from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By

from recipes.tests.test_recipe_base import RecipeMixing
from utils.browser import make_edge_browser


class RecipeBaseFunctionalTest(StaticLiveServerTestCase, RecipeMixing):
    def setUp(self) -> None:
        self.browser = make_edge_browser('--disabled-extensions')
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def get_by_name(self, web_element, tag_name, name):
        return web_element.find_element(
            By.XPATH,
            f'//{tag_name}[@name="{name}"]'
        )
