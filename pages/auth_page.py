# -*- coding: utf-8 -*-
"""
Модуль для страницы авторизации
"""
from atf.ui import *

from selenium.webdriver.common.by import By


class AuthPage(Region):
    """Страница авторизации"""

    login_inp       = TextField(    By.CSS_SELECTOR, '[name="login"]', 'Логин')
    password_inp    = TextField(    By.CSS_SELECTOR, '[name="password"]', 'Пароль')
    enter_btn       = Button(       By.CSS_SELECTOR, '.auth-Form__submit', 'Войти')

    def auth(self, login, password):
        """Авторизация
        :param login: (string) Логин
        :param password: (string) Пароль
        """

        self.check_load()
        self.login_inp.type_in(login)
        self.password_inp.type_in(password)
        self.enter_btn.click()

    def check_load(self):
        """Проверка загрузки страницы"""

        self.enter_btn.should_be(Displayed,
                                 msg='Страница авторизации не загрузилась')
