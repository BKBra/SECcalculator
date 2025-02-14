# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SECcalculator.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QLabel, QListView,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(552, 257)
        self.listWidget_target = QListWidget(Form)
        QListWidgetItem(self.listWidget_target)
        QListWidgetItem(self.listWidget_target)
        self.listWidget_target.setObjectName(u"listWidget_target")
        self.listWidget_target.setGeometry(QRect(90, 30, 451, 41))
        self.listWidget_target.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.listWidget_target.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.listWidget_target.setViewMode(QListView.ViewMode.IconMode)
        self.listWidget_fieldvalue = QListWidget(Form)
        QListWidgetItem(self.listWidget_fieldvalue)
        QListWidgetItem(self.listWidget_fieldvalue)
        self.listWidget_fieldvalue.setObjectName(u"listWidget_fieldvalue")
        self.listWidget_fieldvalue.setGeometry(QRect(90, 70, 451, 41))
        self.listWidget_fieldvalue.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.listWidget_fieldvalue.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.listWidget_fieldvalue.setViewMode(QListView.ViewMode.IconMode)
        self.pushButton_setting = QPushButton(Form)
        self.pushButton_setting.setObjectName(u"pushButton_setting")
        self.pushButton_setting.setGeometry(QRect(460, 0, 82, 28))
        self.label_target = QLabel(Form)
        self.label_target.setObjectName(u"label_target")
        self.label_target.setGeometry(QRect(20, 30, 62, 20))
        self.label_fieldvalue = QLabel(Form)
        self.label_fieldvalue.setObjectName(u"label_fieldvalue")
        self.label_fieldvalue.setGeometry(QRect(20, 80, 62, 20))
        self.label_xyz = QLabel(Form)
        self.label_xyz.setObjectName(u"label_xyz")
        self.label_xyz.setGeometry(QRect(150, 130, 62, 20))
        self.label_fution = QLabel(Form)
        self.label_fution.setObjectName(u"label_fution")
        self.label_fution.setGeometry(QRect(360, 130, 62, 20))
        self.label_xyz_var = QLabel(Form)
        self.label_xyz_var.setObjectName(u"label_xyz_var")
        self.label_xyz_var.setGeometry(QRect(130, 170, 62, 20))
        self.label_fution_var = QLabel(Form)
        self.label_fution_var.setObjectName(u"label_fution_var")
        self.label_fution_var.setGeometry(QRect(350, 170, 71, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"SECcalculator", None))

        __sortingEnabled = self.listWidget_target.isSortingEnabled()
        self.listWidget_target.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_target.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"1", None));
        ___qlistwidgetitem1 = self.listWidget_target.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"2", None));
        self.listWidget_target.setSortingEnabled(__sortingEnabled)


        __sortingEnabled1 = self.listWidget_fieldvalue.isSortingEnabled()
        self.listWidget_fieldvalue.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.listWidget_fieldvalue.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"1", None));
        ___qlistwidgetitem3 = self.listWidget_fieldvalue.item(1)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"2", None));
        self.listWidget_fieldvalue.setSortingEnabled(__sortingEnabled1)

        self.pushButton_setting.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.label_target.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u503c\uff1a", None))
        self.label_fieldvalue.setText(QCoreApplication.translate("Form", u"\u573a\u503c\uff1a", None))
        self.label_xyz.setText(QCoreApplication.translate("Form", u"XYZ", None))
        self.label_fution.setText(QCoreApplication.translate("Form", u"\u878d\u5408", None))
        self.label_xyz_var.setText(QCoreApplication.translate("Form", u"Var_xyz", None))
        self.label_fution_var.setText(QCoreApplication.translate("Form", u"Var_fution", None))
    # retranslateUi

