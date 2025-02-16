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

from PySide6 import QtWidgets, QtGui, QtCore
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
        self.setting.pushButton_add.clicked.connect(self.add_setting)
        self.setting.pushButton_delete.clicked.connect(self.delete_setting)
        self.connect_spinBox()
        self.listitem_selected()
        self.set_res_font()

        self.decks: dict[str, list[list[int]]] = {}

        self.create_setting_file()
        self.load_setting()
        self.set_listwidget()

    def set_listwidget(self):
        self.listWidget_target.clear()
        self.listWidget_fieldvalue.clear()

        for i in range(1, 12):
            item = QtWidgets.QListWidgetItem(f'{i + 1}')

            font = item.font()
            font.setPointSize(20)  # 设置字体大小为20
            item.setFont(font)
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
                item.setBackground(QtGui.QColor(34, 139, 34))
                solve = self.solve_target(int(item.text()))
                if solve:
                    result.append([f'{item.text()}', solve])
                else:
                    result.append([f'{item.text()}', '无解'])
            else:
                item.setBackground(
                    QtGui.QColor('white') if not self.is_dark_mode() else QtGui.QColor(53, 53, 53)
                )

        self.res_show(result)

    def field_listitem_selected(self):
        selected_items = self.listWidget_fieldvalue.selectedItems()
        for index in range(self.listWidget_fieldvalue.count()):
            item = self.listWidget_fieldvalue.item(index)
            if item in selected_items:
                item.setBackground(QtGui.QColor('34, 139, 34'))
            else:
                item.setBackground(
                    QtGui.QColor('white') if not self.is_dark_mode() else QtGui.QColor(53, 53, 53)
                )

    def is_dark_mode(self):
        return self.listWidget_target.palette().color(QtGui.QPalette.Window).lightness() < 128

    def show_settings_window(self):
        self.display_setting()
        self.setting_window.show()

    def is_setting_file_exist(self):
        try:
            with open('Decks.json', 'r') as f:
                return True
        except Exception as e:
            return False

    def create_setting_file(self):
        if not self.is_setting_file_exist():
            with open('Decks.json', 'w') as f:
                dump({'default': list_default}, f)
            return True

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
        current_deck = self.setting.comboBox.currentText()
        deck = []
        for i in range(15):
            if getattr(self.setting, f'radioButton_{i+1}_f').isChecked():
                deck.append([1, getattr(self.setting, f'spinBox_{i+1}').value()])
            elif getattr(self.setting, f'radioButton_{i+1}_xyz').isChecked():
                deck.append([2, getattr(self.setting, f'spinBox_{i+1}').value()])
            else:
                deck.append([3, getattr(self.setting, f'spinBox_{i+1}').value()])
        self.decks[current_deck] = deck
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
            if x == 0:
                continue
            for y in fusion:
                if y == 0:
                    continue
                if target == x + y and (x + y) <= 20:
                    result.append((x, y, 2 * x + y))
        if len(result) == 0:
            return None
        else:
            return result

    def set_res_font(self):
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Bold)
        self.listWidget_res_target.setFont(font)
        self.listWidget_res_field.setFont(font)
        self.listWidget_res_xyz.setFont(font)
        self.listWidget_res_fusion.setFont(font)

    def res_show(self, res: list[tuple[int, int, int]]):
        self.listWidget_res_target.clear()
        self.listWidget_res_field.clear()
        self.listWidget_res_xyz.clear()
        self.listWidget_res_fusion.clear()
        fieldvalues = []
        for index, r in enumerate(res):
            if self.is_dark_mode():
                color = QtGui.QColor('#1f1f1f') if index % 2 == 0 else QtGui.QColor('#181818')
            else:
                color = QtGui.QColor('#f0f0f0') if index % 2 == 0 else QtGui.QColor('#e0e0e0')
            if type(r[1]) == str:
                self.add_centered_item(self.listWidget_res_target, f'{r[0]}', color)
                self.add_centered_item(self.listWidget_res_field, f'无解', color)
                self.add_centered_item(self.listWidget_res_xyz, f'无解', color)
                self.add_centered_item(self.listWidget_res_fusion, f'无解', color)
            else:
                for t in r[1]:
                    self.add_centered_item(self.listWidget_res_target, f'{r[0]}', color)
                    self.add_centered_item(self.listWidget_res_field, f'{t[2]}', color)
                    if t[2] not in fieldvalues:
                        fieldvalues.append(t[2])
                    self.add_centered_item(self.listWidget_res_xyz, f'{t[0]}', color)
                    self.add_centered_item(self.listWidget_res_fusion, f'{t[1]}', color)
        for i in range(self.listWidget_fieldvalue.count()):
            if int(self.listWidget_fieldvalue.item(i).text()) in fieldvalues:
                self.listWidget_fieldvalue.item(i).setBackground(QtGui.QColor('#228b22'))
            else:
                self.listWidget_fieldvalue.item(i).setBackground(
                    QtGui.QColor('white') if not self.is_dark_mode() else QtGui.QColor('#2d2d2d')
                )

    def add_centered_item(self, list_widget, text, color):
        item = QtWidgets.QListWidgetItem(text)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(color)
        list_widget.addItem(item)

    def add_setting(self):
        deck_name, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter deck name:')
        if not ok:
            return
        if deck_name in self.decks:
            QtWidgets.QMessageBox.warning(self, "Warning", "Deck name already exists")
            self.setting_window.raise_()
            self.setting_window.activateWindow()
            return
        deck = [[1, 1] for _ in range(15)]
        self.decks[deck_name] = deck
        self.setting.comboBox.addItem(deck_name)
        self.setting_window.raise_()
        self.setting_window.activateWindow()

    def delete_setting(self):
        current_deck = self.setting.comboBox.currentText()
        if current_deck == 'default':
            QtWidgets.QMessageBox.warning(self, "Warning", "Cannot delete default deck")
            self.setting_window.raise_()
            self.setting_window.activateWindow()
            return
        del self.decks[current_deck]
        self.setting.comboBox.removeItem(self.setting.comboBox.currentIndex())
        self.setting_window.raise_()
        self.setting_window.activateWindow()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = SECcalculator()
    widget.show()
    app.exec()
