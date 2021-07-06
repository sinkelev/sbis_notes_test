# -*- coding: utf-8 -*-
"""
Модуль для страницы заметок
"""
from atf.ui import *
from atf.helper import delay

from selenium.webdriver.common.by import By


class SubmitPopup(Region):
    """Диалоговое окно"""

    positive_btn = Button(By.CSS_SELECTOR, '[sbisname="positiveButton"]', 'Подтверждение удаления')
    negative_btn = Button(By.CSS_SELECTOR, '[sbisname="negativeButton"]', 'Отменить удаление')

    def confirm_delete(self, confirm=True):
        """Подтвердить удаление
        :param confirm: (True/False) Подтвердить/Отказаться
        """

        self.check_open()
        delay(0.5, message='Анимация диалогового окна')
        if confirm:
            self.positive_btn.click()
        else:
            self.negative_btn.click()
        self.check_close()

    def check_open(self):
        """Проверка открытия окна"""

        self.positive_btn.should_be(Displayed,
                                    msg='Диалоговое окно не открылось')

    def check_close(self):
        """Проверка закрытия окна"""

        self.positive_btn.should_be(Hidden,
                                    msg='Диалоговое окно не закрылось')


class NoteEditor(Region):
    """Редактор заметок"""

    note_input_elm  = Element(  By.CSS_SELECTOR, '[sbisname="noteContent"]', 'Ввод заметки')
    ok_btn          = Button(   By.CSS_SELECTOR, '[sbisname="okButton"]', 'Ок')
    remove_elm      = Element(  By.CSS_SELECTOR, '[sbisname="Remove"]', 'Удалить')

    submit_popup    = SubmitPopup()

    def save(self):
        """Сохранение заметки"""

        self.check_open_editor()
        self.ok_btn.click()
        self.check_close_editor()

    def delete(self):
        """Удаление заметки"""

        self.check_open_editor()
        self.remove_elm.click()
        delay(0.5, message='Анимация диалогового окна')
        self.submit_popup.confirm_delete()
        self.check_close_editor()

    def check_open_editor(self):
        """Проверка открытия"""

        self.ok_btn.should_be(Displayed,
                              msg='Редактор заметок не открылся')

    def check_close_editor(self):
        """Проверка, что закрылась"""

        self.ok_btn.should_be(Hidden, msg='Редактор заметки не закрылся')


class NotesPage(Region):
    """Страница заметок"""

    add_note_btn    = Button(       By.CSS_SELECTOR, '[sbisname="addNote"]', 'Создать заметку')
    notes_cslst     = CustomList(   By.CSS_SELECTOR, '[sbisname="notes"] .ws-note', 'Список заметок')

    note_editor     = NoteEditor()

    def create_note(self, note_text):
        """Создание заметки
        :param note_text: (string) текст заметки
        """

        self.check_load()
        self.add_note_btn.click()
        self.note_editor.check_open_editor()
        self.note_editor.note_input_elm.type_in(note_text)
        delay(0.5, message='Ввод текста')
        self.note_editor.save()
        self.notes_cslst.item(contains_text=note_text)\
            .should_be(Displayed, msg='Заметка не сохранилась')

    def open_note(self, note_text):
        """Открытие заметки
        :param note_text: (string) текст заметки, которую необходимо удалить
        """

        self.check_load()
        self.notes_cslst.item(contains_text=note_text).click()

    def delete_note(self, note_text):
        """Удаление заметки
        :param note_text: (string) текст заметки, которую необходимо удалить
        """

        self.note_editor.delete()
        self.check_exist(note_text)

    def check_exist(self, note_text):
        """Проверка отображения элемента"""

        self.notes_cslst.item(contains_text=note_text)\
            .should_be(Hidden, msg='Заметка не удалена')

    def check_load(self):
        """Проверка загрузки страницы"""

        self.notes_cslst.should_be(Displayed,
                                   msg='Страница заметок не загрузилась')
