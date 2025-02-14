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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QLabel, QListView, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(848, 215)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_target = QLabel(Form)
        self.label_target.setObjectName(u"label_target")

        self.horizontalLayout.addWidget(self.label_target)

        self.listWidget_target = QListWidget(Form)
        QListWidgetItem(self.listWidget_target)
        QListWidgetItem(self.listWidget_target)
        self.listWidget_target.setObjectName(u"listWidget_target")
        self.listWidget_target.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.listWidget_target.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.listWidget_target.setViewMode(QListView.ViewMode.IconMode)

        self.horizontalLayout.addWidget(self.listWidget_target)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 3)

        self.pushButton_setting = QPushButton(Form)
        self.pushButton_setting.setObjectName(u"pushButton_setting")

        self.gridLayout.addWidget(self.pushButton_setting, 0, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_fieldvalue = QLabel(Form)
        self.label_fieldvalue.setObjectName(u"label_fieldvalue")

        self.horizontalLayout_2.addWidget(self.label_fieldvalue)

        self.listWidget_fieldvalue = QListWidget(Form)
        QListWidgetItem(self.listWidget_fieldvalue)
        QListWidgetItem(self.listWidget_fieldvalue)
        self.listWidget_fieldvalue.setObjectName(u"listWidget_fieldvalue")
        self.listWidget_fieldvalue.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.listWidget_fieldvalue.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.listWidget_fieldvalue.setViewMode(QListView.ViewMode.IconMode)

        self.horizontalLayout_2.addWidget(self.listWidget_fieldvalue)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 3)

        self.label_fution = QLabel(Form)
        self.label_fution.setObjectName(u"label_fution")

        self.gridLayout.addWidget(self.label_fution, 3, 2, 1, 1)

        self.label_fution_var = QLabel(Form)
        self.label_fution_var.setObjectName(u"label_fution_var")

        self.gridLayout.addWidget(self.label_fution_var, 5, 2, 1, 1)

        self.label_xyz = QLabel(Form)
        self.label_xyz.setObjectName(u"label_xyz")

        self.gridLayout.addWidget(self.label_xyz, 3, 1, 1, 1)

        self.label_xyz_var = QLabel(Form)
        self.label_xyz_var.setObjectName(u"label_xyz_var")

        self.gridLayout.addWidget(self.label_xyz_var, 5, 1, 1, 1)

#if QT_CONFIG(shortcut)
        self.label_target.setBuddy(self.listWidget_target)
        self.label_fieldvalue.setBuddy(self.listWidget_fieldvalue)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"SECcalculator", None))
        self.label_target.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u503c\uff1a", None))

        __sortingEnabled = self.listWidget_target.isSortingEnabled()
        self.listWidget_target.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_target.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"1", None));
        ___qlistwidgetitem1 = self.listWidget_target.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"2", None));
        self.listWidget_target.setSortingEnabled(__sortingEnabled)

        self.pushButton_setting.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.label_fieldvalue.setText(QCoreApplication.translate("Form", u"\u573a\u503c\uff1a", None))

        __sortingEnabled1 = self.listWidget_fieldvalue.isSortingEnabled()
        self.listWidget_fieldvalue.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.listWidget_fieldvalue.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"1", None));
        ___qlistwidgetitem3 = self.listWidget_fieldvalue.item(1)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"2", None));
        self.listWidget_fieldvalue.setSortingEnabled(__sortingEnabled1)

        self.label_fution.setText(QCoreApplication.translate("Form", u"\u878d\u5408", None))
        self.label_fution_var.setText(QCoreApplication.translate("Form", u"Var_fution", None))
        self.label_xyz.setText(QCoreApplication.translate("Form", u"XYZ", None))
        self.label_xyz_var.setText(QCoreApplication.translate("Form", u"Var_xyz", None))
    # retranslateUi

