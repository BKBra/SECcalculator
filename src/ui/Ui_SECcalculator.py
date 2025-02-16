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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLabel,
    QLayout, QListView, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(545, 528)
        self.verticalLayout_6 = QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_setting = QPushButton(Form)
        self.pushButton_setting.setObjectName(u"pushButton_setting")

        self.verticalLayout_6.addWidget(self.pushButton_setting)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_target = QLabel(Form)
        self.label_target.setObjectName(u"label_target")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_target.sizePolicy().hasHeightForWidth())
        self.label_target.setSizePolicy(sizePolicy)
        self.label_target.setMinimumSize(QSize(50, 0))

        self.horizontalLayout.addWidget(self.label_target)

        self.listWidget_target = QListWidget(Form)
        QListWidgetItem(self.listWidget_target)
        QListWidgetItem(self.listWidget_target)
        self.listWidget_target.setObjectName(u"listWidget_target")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget_target.sizePolicy().hasHeightForWidth())
        self.listWidget_target.setSizePolicy(sizePolicy1)
        self.listWidget_target.setMinimumSize(QSize(0, 40))
        self.listWidget_target.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.listWidget_target.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.listWidget_target.setViewMode(QListView.ViewMode.IconMode)

        self.horizontalLayout.addWidget(self.listWidget_target)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_fieldvalue = QLabel(Form)
        self.label_fieldvalue.setObjectName(u"label_fieldvalue")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_fieldvalue.sizePolicy().hasHeightForWidth())
        self.label_fieldvalue.setSizePolicy(sizePolicy3)
        self.label_fieldvalue.setMinimumSize(QSize(64, 0))

        self.horizontalLayout_2.addWidget(self.label_fieldvalue)

        self.listWidget_fieldvalue = QListWidget(Form)
        QListWidgetItem(self.listWidget_fieldvalue)
        QListWidgetItem(self.listWidget_fieldvalue)
        self.listWidget_fieldvalue.setObjectName(u"listWidget_fieldvalue")
        sizePolicy1.setHeightForWidth(self.listWidget_fieldvalue.sizePolicy().hasHeightForWidth())
        self.listWidget_fieldvalue.setSizePolicy(sizePolicy1)
        self.listWidget_fieldvalue.setMinimumSize(QSize(0, 80))
        self.listWidget_fieldvalue.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.listWidget_fieldvalue.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.listWidget_fieldvalue.setViewMode(QListView.ViewMode.IconMode)

        self.horizontalLayout_2.addWidget(self.listWidget_fieldvalue)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.label)

        self.listWidget_res_target = QListWidget(Form)
        self.listWidget_res_target.setObjectName(u"listWidget_res_target")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.listWidget_res_target.sizePolicy().hasHeightForWidth())
        self.listWidget_res_target.setSizePolicy(sizePolicy5)

        self.verticalLayout.addWidget(self.listWidget_res_target)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)

        self.verticalLayout_2.addWidget(self.label_2)

        self.listWidget_res_field = QListWidget(Form)
        self.listWidget_res_field.setObjectName(u"listWidget_res_field")
        sizePolicy5.setHeightForWidth(self.listWidget_res_field.sizePolicy().hasHeightForWidth())
        self.listWidget_res_field.setSizePolicy(sizePolicy5)

        self.verticalLayout_2.addWidget(self.listWidget_res_field)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)

        self.verticalLayout_3.addWidget(self.label_3)

        self.listWidget_res_xyz = QListWidget(Form)
        self.listWidget_res_xyz.setObjectName(u"listWidget_res_xyz")
        sizePolicy5.setHeightForWidth(self.listWidget_res_xyz.sizePolicy().hasHeightForWidth())
        self.listWidget_res_xyz.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.listWidget_res_xyz)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)

        self.verticalLayout_4.addWidget(self.label_4)

        self.listWidget_res_fusion = QListWidget(Form)
        self.listWidget_res_fusion.setObjectName(u"listWidget_res_fusion")
        sizePolicy5.setHeightForWidth(self.listWidget_res_fusion.sizePolicy().hasHeightForWidth())
        self.listWidget_res_fusion.setSizePolicy(sizePolicy5)

        self.verticalLayout_4.addWidget(self.listWidget_res_fusion)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 2)
        self.verticalLayout_6.setStretch(2, 100)
#if QT_CONFIG(shortcut)
        self.label_target.setBuddy(self.listWidget_target)
        self.label_fieldvalue.setBuddy(self.listWidget_fieldvalue)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.listWidget_target.clearSelection)
        self.pushButton_2.clicked.connect(self.listWidget_fieldvalue.clearSelection)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"SECcalculator", None))
        self.pushButton_setting.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.label_target.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u76ee\u6807\u503c\uff1a</span></p></body></html>", None))

        __sortingEnabled = self.listWidget_target.isSortingEnabled()
        self.listWidget_target.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_target.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"1", None));
        ___qlistwidgetitem1 = self.listWidget_target.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"2", None));
        self.listWidget_target.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
        self.label_fieldvalue.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u573a\u503c\uff1a</span></p></body></html>", None))

        __sortingEnabled1 = self.listWidget_fieldvalue.isSortingEnabled()
        self.listWidget_fieldvalue.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.listWidget_fieldvalue.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"1", None));
        ___qlistwidgetitem3 = self.listWidget_fieldvalue.item(1)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"2", None));
        self.listWidget_fieldvalue.setSortingEnabled(__sortingEnabled1)

        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">\u76ee\u6807</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">\u573a\u503c</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">XYZ</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Fusion</span></p></body></html>", None))
    # retranslateUi

