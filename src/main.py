'''
Author: Allan
Date: 2025-02-14 13:36:52
LastEditors: Allan
LastEditTime: 2025-02-14 17:40:08
FilePath: \SECcalculator\src\main.py
Description: 

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''

# pip freeze > requirements.txt
# pip install -r requirements.txt

from PySide6 import QtWidgets, QtGui
from src.ui.Ui_SECcalculator import Ui_Form
from src.ui.Ui_setting import Ui_window_setting as Ui_setting
from json import load, dump
from enum import Enum
import random

# Fusion = 1
# XYZ = 2
# Other = 3

list_default: list[list[int]] = [
    [1, 1],  # 1
    [1, 2],  # 2
    [1, 3],  # 3
    [1, 4],  # 4
    [1, 5],  # 5
    [1, 6],  # 6
    [1, 7],  # 7
    [2, 3],  # 8
    [2, 3],  # 9
    [2, 4],  # 10
    [1, 4],  # 11
    [2, 5],  # 12
    [2, 5],  # 13
    [2, 6],  # 14
    [1, 6],  # 15
]


def generate_random_deck():
    return [[random.randint(1, 2), random.randint(0, 12)] for _ in range(15)]


list_default2 = generate_random_deck()

dict_Decks = {
    'default_deck1': list_default,
    'default_deck2': list_default2,
}
with open('Decks.json', 'w') as f:
    dump(dict_Decks, f)

with open('Decks.json', 'r') as f:
    dict_Decks = load(f)


class SECcalculator(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(SECcalculator, self).__init__()
        self.setupUi(self)
        self.setting_window = QtWidgets.QWidget()
        self.setting = Ui_setting()
        self.setting.setupUi(self.setting_window)

        self.pushButton_setting.clicked.connect(self.show_settings_window)
        self.setting.comboBox.currentIndexChanged.connect(self.display_setting)
        self.setting.pushButton_yes.clicked.connect(self.save_setting)
        self.setting.pushButton_no.clicked.connect(self.setting_window.close)
        self.connect_spinBox()
        self.listitem_selected()

        self.decks: dict[str, list[list[int]]] = {}

        self.load_setting()
        self.set_listwidget()

    def set_listwidget(self):
        self.listWidget_target.clear()
        self.listWidget_fieldvalue.clear()
        nice_green = QtGui.QColor(34, 139, 34)  # 深墨绿色 for dark mode

        for i in range(1, 12):
            item = QtWidgets.QListWidgetItem(f'{i + 1}')

            font = item.font()
            font.setPointSize(20)  # 设置字体大小为20
            item.setFont(font)
            item.setBackground(nice_green)
            self.listWidget_target.addItem(item)
            self.listWidget_target.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        for i in range(2, 20):
            item = QtWidgets.QListWidgetItem(f'{i + 1}')
            font = item.font()
            font.setPointSize(20)  # 设置字体大小为20
            item.setFont(font)
            self.listWidget_fieldvalue.addItem(item)
            self.listWidget_fieldvalue.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_target.setDragEnabled(False)
        self.listWidget_target.setAcceptDrops(False)
        self.listWidget_target.setDropIndicatorShown(False)

        self.listWidget_fieldvalue.setDragEnabled(False)
        self.listWidget_fieldvalue.setAcceptDrops(False)
        self.listWidget_fieldvalue.setDropIndicatorShown(False)

    def listitem_selected(self):
        self.listWidget_target.itemSelectionChanged.connect(self.target_listitem_selected)
        self.listWidget_fieldvalue.itemSelectionChanged.connect(self.field_listitem_selected)

    def target_listitem_selected(self):
        selected_items = self.listWidget_target.selectedItems()
        result = []
        for index in range(self.listWidget_target.count()):
            item = self.listWidget_target.item(index)
            if item in selected_items:
                item.setBackground(QtGui.QColor('blue'))
                solve = self.solve_target(int(item.text()))
                if solve:
                    result += [f'目标：{item.text()}', solve]
            else:
                item.setBackground(
                    QtGui.QColor('white') if not self.is_dark_mode() else QtGui.QColor(53, 53, 53)
                )

        print(result)

    def field_listitem_selected(self):
        selected_items = self.listWidget_fieldvalue.selectedItems()
        for index in range(self.listWidget_fieldvalue.count()):
            item = self.listWidget_fieldvalue.item(index)
            if item in selected_items:
                item.setBackground(QtGui.QColor('blue'))
            else:
                item.setBackground(
                    QtGui.QColor('white') if not self.is_dark_mode() else QtGui.QColor(53, 53, 53)
                )

    def is_dark_mode(self):
        return self.listWidget_target.palette().color(QtGui.QPalette.Window).lightness() < 128

    def show_settings_window(self):
        self.display_setting()
        self.setting_window.show()

    def load_setting(self):
        try:
            with open('Decks.json', 'r') as f:
                self.decks = load(f)
            for deck_name, deck in self.decks.items():
                if len(deck) != 15:
                    raise Exception(f"Deck {deck_name} has {len(deck)} cards, expected 15")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Warning", f"Failed to load settings: {e}")

        for deck_name, deck in self.decks.items():
            self.setting.comboBox.addItem(deck_name)
            self.quue_cards(deck)

    def save_setting(self):
        with open('Decks.json', 'w') as f:
            dump(self.decks, f)
        self.setting_window.close()
        QtWidgets.QMessageBox.information(self, "Information", "Settings saved")

    def quue_cards(self, deck: list[list[int]]):
        for i in range(len(deck)):
            for j in range(0, len(deck) - i - 1):
                if deck[j][0] > deck[j + 1][0]:
                    deck[j], deck[j + 1] = deck[j + 1], deck[j]

        for i in range(len(deck)):
            for j in range(0, len(deck) - i - 1):
                if deck[j][0] == deck[j + 1][0] and deck[j][1] > deck[j + 1][1]:
                    deck[j], deck[j + 1] = deck[j + 1], deck[j]

        # Move elements with 0 to the end
        non_zero_deck = [card for card in deck if card[1] != 0]
        zero_deck = [card for card in deck if card[1] == 0]
        deck[:] = non_zero_deck + zero_deck

    def display_setting(self):
        current_deck = self.setting.comboBox.currentText()
        deck = self.decks[current_deck]
        print(deck)
        for i in range(len(deck)):
            if deck[i][0] == 1:
                getattr(self.setting, f'radioButton_{i+1}_f').setChecked(True)
            elif deck[i][0] == 2:
                getattr(self.setting, f'radioButton_{i+1}_xyz').setChecked(True)
            else:
                getattr(self.setting, f'radioButton_{i+1}_f').setChecked(True)
            getattr(self.setting, f'spinBox_{i+1}').setValue(deck[i][1])
            if deck[i][1] == 0:
                getattr(self.setting, f'radioButton_{i+1}_f').setEnabled(False)
                getattr(self.setting, f'radioButton_{i+1}_xyz').setEnabled(False)

    def connect_spinBox(self):
        for i in range(15):
            getattr(self.setting, f'spinBox_{i+1}').valueChanged.connect(self.spinBoxChanged)

    def spinBoxChanged(self):
        for i in range(15):
            if getattr(self.setting, f'spinBox_{i+1}').value() == 0:
                getattr(self.setting, f'radioButton_{i+1}_f').setEnabled(False)
                getattr(self.setting, f'radioButton_{i+1}_xyz').setEnabled(False)
            else:
                getattr(self.setting, f'radioButton_{i+1}_f').setEnabled(True)
                getattr(self.setting, f'radioButton_{i+1}_xyz').setEnabled(True)

    def closeEvent(self, event):
        self.setting_window.close()
        event.accept()

    def solve_target(self, target):
        deck = self.decks[self.setting.comboBox.currentText()]
        xyz = [deck[i][1] for i in range(15) if deck[i][0] == 2]
        xyz = list(set(xyz))
        fusion = [deck[i][1] for i in range(15) if deck[i][0] == 1]
        fusion = list(set(fusion))
        result = []
        for x in xyz:
            for y in fusion:
                if target == 2 * x + y and (x + y) <= 20:
                    result.append((x, y, x + y))
        if len(result) == 0:
            return None
        else:
            return result


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = SECcalculator()
    widget.show()
    app.exec()
