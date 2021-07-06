# -*- coding: utf-8 -*-
"""
Модуль для Главной страницы
"""
from atf.ui import *

from selenium.webdriver.common.by import By


class MainPage(Region):
    """Главная страница"""

    menu_cslst      = CustomList(   By.CSS_SELECTOR, '.NavigationPanels-Accordion__title', 'Меню')
    submenu_cslst   = CustomList(   By.CSS_SELECTOR, '.NavigationPanels-SubMenu__wrapper', 'Подменю')

    def go_to(self, menu, submenu):
        """Переход на  страницу через left bar
        :param menu: (string) название меню
        :param submenu: (string) название подменю
        """

        self.check_load()
        self.menu_cslst.item(with_text=menu).click()
        self.submenu_cslst.should_be(Displayed)
        self.submenu_cslst.item(with_text=submenu).click()

    def check_load(self):
        """Проверка загрузки страницы"""

        self.menu_cslst.should_be(Displayed,
                                  msg='Главная страница не загрузилась')
