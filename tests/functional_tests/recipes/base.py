from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from recipes.tests.test_recipe_base import RecipeMixing
from utils.browser import make_edge_browser


class RecipeBaseFunctionalTest(StaticLiveServerTestCase, RecipeMixing):
    def setUp(self) -> None:
        self.browser = make_edge_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()
