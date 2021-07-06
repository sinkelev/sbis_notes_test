# -*- coding: utf-8 -*-
"""
Тестирование заметки
"""
from atf import run_tests, log
from atf.ui import TestCaseUI

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.notes_page import NotesPage, NoteEditor


class TestNotes(TestCaseUI):
    """Проверка создания и удаление заметок"""

    @classmethod
    def setup_class(cls):
        cls.browser.open('https://fix-sso.sbis.ru/auth-online/')
        AuthPage(cls.driver).auth('Демо_тензор', 'Демо123')

    def test_01_add_and_delete_note(self):
        """Создание заметки и удаление заметки"""

        note_text = 'Тестовый текст'

        log('Переход на страницу заметок и создание')
        main = MainPage(self.driver)
        main.go_to('Документы', 'Заметки')
        notes_page = NotesPage(self.driver)
        notes_page.add_note()
        note_editor = NoteEditor(self.driver)
        note_editor.create(note_text)
        notes_page.check_exist(note_text, msg='Не сохранилась')

        log('Удаление заметки')
        notes_page.open_note(note_text)
        note_editor.delete()
        notes_page.check_exist(note_text, False, msg='Не удалена')


if __name__ == '__main__':
    run_tests()
