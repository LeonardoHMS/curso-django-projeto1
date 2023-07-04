import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from selenium.webdriver.common.by import By

from .base import AuthorsBaseTest


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    def test_user_valid_data_can_login_successfully(self):
        string_password = 'pass'
        user = User.objects.create_user(
            first_name='user_test',
            username='my_user',
            password=string_password,
        )

        # Usuário abre a página de login
        self.browser.get(self.live_server_url + reverse('authors:login'))

        # Usuário vê o formulário de login
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.get_by_placeholder(form, 'Type your username')
        password_field = self.get_by_placeholder(form, 'Type your password')

        # Usuário digita seu usuário e senha
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        # Usuário enviar o formulário
        form.submit()

        # Usuário vê a mensagem de login com sucesso e seu nome
        self.assertIn(
            'Your are logged in with user_test. Please, click here to logout.',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_login_create_raises_404_if_not_POST_method(self):
        self.browser.get(self.live_server_url +
                         reverse('authors:login_create'))
        self.assertIn(
            'Not Found',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_login_error_invalid_username_or_password(self):
        # Usuário abre a página de login
        self.browser.get(self.live_server_url + reverse('authors:login'))

        # Usuário vê o formulário de login
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.get_by_placeholder(form, 'Type your username')
        password_field = self.get_by_placeholder(form, 'Type your password')

        # Usuário preenche os campos incorretamente
        username_field.send_keys(' ')
        password_field.send_keys(' ')

        # Usuário envia o formulário
        form.submit()

        # Usuário vê a mensagem de erro de usuário ou senha inválidos
        self.assertIn(
            'Invalid username or password',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_login_invalid_credentials_error_message(self):
        # Usuário abre a página de login
        self.browser.get(self.live_server_url + reverse('authors:login'))

        # Usuário vê o formulário de login
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.get_by_placeholder(form, 'Type your username')
        password_field = self.get_by_placeholder(form, 'Type your password')

        # Usuário preenche os campos
        # Porém com erro em um dos campos que não condiz
        # Com a conta a ser logada
        username_field.send_keys('my_user')
        password_field.send_keys('P@ssw0rd')

        # Usuário envia o formulário
        form.submit()

        # Usuário vê a mensagem de erro de credenciais
        self.assertIn(
            'Invalid credentials',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
