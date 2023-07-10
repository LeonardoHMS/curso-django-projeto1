from django.contrib.auth.models import User
from selenium.webdriver.common.by import By

from .base import RecipeBaseFunctionalTest


class RecipeTestFormCreate(RecipeBaseFunctionalTest):
    def login_user(self):
        User.objects.create_user(username='my_user', password='P@ssw0rd')
        self.client.login(username='my_user', password='P@ssw0rd')
        cookie = self.client.cookies['sessionid']
        self.browser.get(self.live_server_url)
        self.browser.add_cookie({
            'name': 'sessionid',
            'value': cookie.value,
            'secure': False,
            'path': '/'
        })

    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/main/div/div[2]/div/form',
        )

    def test_recipe_form_create_error_title_5_chars(self):
        # Usuário loga em sua conta
        self.login_user()

        # Usuário entra no formulário de criação de receita
        self.browser.get(self.live_server_url +
                         '/authors/dashboard/recipe/create/')
        form = self.get_form()

        # Usuário preenche os campos
        # Porém o título menor que 5 caracteres
        title = self.get_by_name(form, 'input', 'title')
        description = self.get_by_name(form, 'input', 'description')
        preparation_time = self.get_by_name(form, 'input', 'preparation_time')
        servings = self.get_by_name(form, 'input', 'servings')
        preparation_steps = self.get_by_name(
            form, 'textarea', 'preparation_steps')

        title.send_keys('abc')
        description.send_keys('description correct')
        preparation_time.send_keys(5)
        servings.send_keys(8)
        preparation_steps.send_keys('preparation steps correct')

        # Usuário envia o formulário
        form.submit()

        # Usuário vê a mensagem de erro no título
        self.assertIn(
            'Must have at least 5 chars',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_recipe_form_create_error_description_5_chars(self):
        # Usuário loga em sua conta
        self.login_user()

        # Usuário entra no formulário de criação de receita
        self.browser.get(self.live_server_url +
                         '/authors/dashboard/recipe/create/')
        form = self.get_form()

        # Usuário preenche os campos
        # Porém a descrição menor que 5 caracteres
        title = self.get_by_name(form, 'input', 'title')
        description = self.get_by_name(form, 'input', 'description')
        preparation_time = self.get_by_name(form, 'input', 'preparation_time')
        servings = self.get_by_name(form, 'input', 'servings')
        preparation_steps = self.get_by_name(
            form, 'textarea', 'preparation_steps')

        title.send_keys('title correct')
        description.send_keys('abc')
        preparation_time.send_keys(5)
        servings.send_keys(8)
        preparation_steps.send_keys('preparation steps correct')

        # Usuário envia o formulário
        form.submit()

        # Usuário vê a mensagem de erro no título
        self.assertIn(
            'Must have at least 5 chars',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_recipe_form_create_error_description_and_title_equals(self):
        # Usuário loga em sua conta
        self.login_user()

        # Usuário entra no formulário de criação de receita
        self.browser.get(self.live_server_url +
                         '/authors/dashboard/recipe/create/')
        form = self.get_form()

        # Usuário preenche os campos
        # Porém a descrição e título estão iguais
        title = self.get_by_name(form, 'input', 'title')
        description = self.get_by_name(form, 'input', 'description')
        preparation_time = self.get_by_name(form, 'input', 'preparation_time')
        servings = self.get_by_name(form, 'input', 'servings')
        preparation_steps = self.get_by_name(
            form, 'textarea', 'preparation_steps')

        title.send_keys('is my title')
        description.send_keys('is my title')
        preparation_time.send_keys(5)
        servings.send_keys(8)
        preparation_steps.send_keys('preparation steps correct')

        # Usuário envia o formulário
        form.submit()

        # Usuário vê a mensagem de erro no título
        self.assertIn(
            'Cannot be equal to description',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
        self.assertIn(
            'Cannot be equal to title',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_create_recipe_with_negative_preparation_time(self):
        # Usuário loga em sua conta
        self.login_user()

        # Usuário entra no formulário de criação de receita
        self.browser.get(self.live_server_url +
                         '/authors/dashboard/recipe/create/')
        form = self.get_form()

        # Usuário preenche os campos
        # Porém em preparation time, ele insere um número negativo
        title = self.get_by_name(form, 'input', 'title')
        description = self.get_by_name(form, 'input', 'description')
        preparation_time = self.get_by_name(form, 'input', 'preparation_time')
        servings = self.get_by_name(form, 'input', 'servings')
        preparation_steps = self.get_by_name(
            form, 'textarea', 'preparation_steps')

        title.send_keys('is my title')
        description.send_keys('is my description')
        preparation_time.send_keys(-5)
        servings.send_keys(8)
        preparation_steps.send_keys('is my preparation steps for my recipe')

        # Usuário envia o formulário
        form.submit()

        # Usuário vê a mensagem de erro na tela
        self.assertIn(
            'Must be a positive number',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_create_recipe_with_negative_servings(self):
        # Usuário loga em sua conta
        self.login_user()

        # Usuário entra no formulário de criação de receita
        self.browser.get(self.live_server_url +
                         '/authors/dashboard/recipe/create/')
        form = self.get_form()

        # Usuário preenche os campos
        # Porém em preparation time, ele insere um número negativo
        title = self.get_by_name(form, 'input', 'title')
        description = self.get_by_name(form, 'input', 'description')
        preparation_time = self.get_by_name(form, 'input', 'preparation_time')
        servings = self.get_by_name(form, 'input', 'servings')
        preparation_steps = self.get_by_name(
            form, 'textarea', 'preparation_steps')

        title.send_keys('is my title')
        description.send_keys('is my description')
        preparation_time.send_keys(5)
        servings.send_keys(-8)
        preparation_steps.send_keys('is my preparation steps for my recipe')

        # Usuário envia o formulário
        form.submit()

        # Usuário vê a mensagem de erro na tela
        self.assertIn(
            'Must be a positive number',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_create_recipe_successfully(self):
        # Usuário loga em sua conta
        self.login_user()

        # Usuário entra no formulário de criação de receita
        self.browser.get(self.live_server_url +
                         '/authors/dashboard/recipe/create/')
        form = self.get_form()

        # Usuário preenche os campos corretamente
        title = self.get_by_name(form, 'input', 'title')
        description = self.get_by_name(form, 'input', 'description')
        preparation_time = self.get_by_name(form, 'input', 'preparation_time')
        servings = self.get_by_name(form, 'input', 'servings')
        preparation_steps = self.get_by_name(
            form, 'textarea', 'preparation_steps')

        title.send_keys('is my title')
        description.send_keys('is my description')
        preparation_time.send_keys(5)
        servings.send_keys(8)
        preparation_steps.send_keys('is my preparation steps for my recipe')

        # Usuário envia o formulário
        form.submit()
        # Usuário vê a mensagem de receita criada com sucesso
        self.assertIn(
            'Sua receita foi salva com sucesso!',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
