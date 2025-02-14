# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QGridLayout,
    QHBoxLayout, QLayout, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_window_setting(object):
    def setupUi(self, window_setting):
        if not window_setting.objectName():
            window_setting.setObjectName(u"window_setting")
        window_setting.resize(658, 221)
        self.verticalLayout = QVBoxLayout(window_setting)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_1_xyz = QRadioButton(window_setting)
        self.buttonGroup = QButtonGroup(window_setting)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.setExclusive(True)
        self.buttonGroup.addButton(self.radioButton_1_xyz)
        self.radioButton_1_xyz.setObjectName(u"radioButton_1_xyz")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_1_xyz.sizePolicy().hasHeightForWidth())
        self.radioButton_1_xyz.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.radioButton_1_xyz)

        self.radioButton_1_f = QRadioButton(window_setting)
        self.buttonGroup.addButton(self.radioButton_1_f)
        self.radioButton_1_f.setObjectName(u"radioButton_1_f")
        sizePolicy.setHeightForWidth(self.radioButton_1_f.sizePolicy().hasHeightForWidth())
        self.radioButton_1_f.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.radioButton_1_f)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.spinBox_1 = QSpinBox(window_setting)
        self.spinBox_1.setObjectName(u"spinBox_1")
        self.spinBox_1.setMaximum(12)

        self.gridLayout.addWidget(self.spinBox_1, 0, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.radioButton_6_xyz = QRadioButton(window_setting)
        self.buttonGroup_6 = QButtonGroup(window_setting)
        self.buttonGroup_6.setObjectName(u"buttonGroup_6")
        self.buttonGroup_6.addButton(self.radioButton_6_xyz)
        self.radioButton_6_xyz.setObjectName(u"radioButton_6_xyz")
        sizePolicy.setHeightForWidth(self.radioButton_6_xyz.sizePolicy().hasHeightForWidth())
        self.radioButton_6_xyz.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.radioButton_6_xyz)

        self.radioButton_6_f = QRadioButton(window_setting)
        self.buttonGroup_6.addButton(self.radioButton_6_f)
        self.radioButton_6_f.setObjectName(u"radioButton_6_f")
        sizePolicy.setHeightForWidth(self.radioButton_6_f.sizePolicy().hasHeightForWidth())
        self.radioButton_6_f.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.radioButton_6_f)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 2, 1, 1)

        self.spinBox_6 = QSpinBox(window_setting)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMaximum(12)

        self.gridLayout.addWidget(self.spinBox_6, 0, 3, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.radioButton_11_xyz = QRadioButton(window_setting)
        self.buttonGroup_11 = QButtonGroup(window_setting)
        self.buttonGroup_11.setObjectName(u"buttonGroup_11")
        self.buttonGroup_11.addButton(self.radioButton_11_xyz)
        self.radioButton_11_xyz.setObjectName(u"radioButton_11_xyz")
        sizePolicy.setHeightForWidth(self.radioButton_11_xyz.sizePolicy().hasHeightForWidth())
        self.radioButton_11_xyz.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.radioButton_11_xyz)

        self.radioButton_11_f = QRadioButton(window_setting)
        self.buttonGroup_11.addButton(self.radioButton_11_f)
        self.radioButton_11_f.setObjectName(u"radioButton_11_f")
        sizePolicy.setHeightForWidth(self.radioButton_11_f.sizePolicy().hasHeightForWidth())
        self.radioButton_11_f.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.radioButton_11_f)


        self.gridLayout.addLayout(self.horizontalLayout_12, 0, 4, 1, 1)

        self.spinBox_11 = QSpinBox(window_setting)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setMaximum(12)

        self.gridLayout.addWidget(self.spinBox_11, 0, 5, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_2_xyz = QRadioButton(window_setting)
        self.buttonGroup_2 = QButtonGroup(window_setting)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_2_xyz)
        self.radioButton_2_xyz.setObjectName(u"radioButton_2_xyz")
        sizePolicy.setHeightForWidth(self.radioButton_2_xyz.sizePolicy().hasHeightForWidth())
        self.radioButton_2_xyz.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.radioButton_2_xyz)

        self.radioButton_2_f = QRadioButton(window_setting)
        self.buttonGroup_2.addButton(self.radioButton_2_f)
        self.radioButton_2_f.setObjectName(u"radioButton_2_f")
        sizePolicy.setHeightForWidth(self.radioButton_2_f.sizePolicy().hasHeightForWidth())
        self.radioButton_2_f.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.radioButton_2_f)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.spinBox_2 = QSpinBox(window_setting)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(12)

        self.gridLayout.addWidget(self.spinBox_2, 1, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.radioButton_7_xyz = QRadioButton(window_setting)
        self.buttonGroup_7 = QButtonGroup(window_setting)
        self.buttonGroup_7.setObjectName(u"buttonGroup_7")
        self.buttonGroup_7.addButton(self.radioButton_7_xyz)
        self.radioButton_7_xyz.setObjectName(u"radioButton_7_xyz")
        sizePolicy.setHeightForWidth(self.radioButton_7_xyz.sizePolicy().hasHeightForWidth())
        self.radioButton_7_xyz.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.radioButton_7_xyz)

        self.radioButton_7_f = QRadioButton(window_setting)
        self.buttonGroup_7.addButton(self.radioButton_7_f)
        self.radioButton_7_f.setObjectName(u"radioButton_7_f")
        sizePolicy.setHeightForWidth(self.radioButton_7_f.sizePolicy().hasHeightForWidth())
        self.radioButton_7_f.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.radioButton_7_f)


        self.gridLayout.addLayout(self.horizontalLayout_10, 1, 2, 1, 1)

        self.spinBox_7 = QSpinBox(window_setting)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setMaximum(12)

        self.gridLayout.addWidget(self.spinBox_7, 1, 3, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.radioButton_12_xyz = QRadioButton(window_setting)
        self.buttonGroup_12 = QButtonGroup(window_setting)
        self.buttonGroup_12.setObjectName(u"buttonGroup_12")
        self.buttonGroup_12.addButton(self.radioButton_12_xyz)
        self.radioButton_12_xyz.setObjectName(u"radioButton_12_xyz")
        sizePolicy.setHeightForWidth(self.radioButton_12_xyz.sizePolicy().hasHeightForWidth())
        self.radioButton_12_xyz.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.radioButton_12_xyz)

        self.radioButton_12_f = QRadioButton(window_setting)
        self.buttonGroup_12.addButton(self.radioButton_12_f)
        self.radioButton_12_f.setObjectName(u"radioButton_12_f")
        sizePolicy.setHeightForWidth(self.radioButton_12_f.sizePolicy().hasHeightForWidth())
        self.radioButton_12_f.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.radioButton_12_f)


        self.gridLayout.addLayout(self.horizontalLayout_15, 1, 4, 1, 1)

        self.spinBox_12 = QSpinBox(window_setting)
        self.spinBox_12.setObjectName(u"spinBox_12")
        self.spinBox_12.setMaximum(12)

        self.gridLayout.addWidget(self.spinBox_12, 1, 5, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_3_xyz = QRadioButton(window_setting)
        self.buttonGroup_3 = QButtonGroup(window_setting)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton_3_xyz)
        self.radioButton_3_xyz.setObjectName(u"radioButton_3_xyz")
        sizePolicy.setHeightForWidth(self.radioButton_3_xyz.sizePolicy().hasHeightForWidth())
        self.radioButton_3_xyz.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.radioButton_3_xyz)

        self.radioButton_3_f = QRadioButton(window_setting)
        self.buttonGroup_3.addButton(self.radioButton_3_f)
        self.radioButton_3_f.setObjectName(u"radioButton_3_f")
        sizePolicy.setHeightForWidth(self.radioButton_3_f.sizePolicy().hasHeightForWidth())
        self.radioButton_3_f.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.radioButton_3_f)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.spinBox_3 = QSpinBox(window_setting)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(12)

        self.gridLayout.addWidget(self.spinBox_3, 2, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.radioButton_8_xyz = QRadioButton(window_setting)
        self.buttonGroup_8 = QButtonGroup(window_setting)
        self.buttonGroup_8.setObjectName(u"buttonGroup_8")
        self.buttonGroup_8.addButton(self.radioButton_8_xyz)
        self.radioButton_8_xyz.setObjectName(u"radioButton_8_xyz")
        sizePolicy.setHeightForWidth(self.radioButton_8_xyz.sizePolicy().hasHeightForWidth())
        self.radioButton_8_xyz.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.radioButton_8_xyz)

        self.radioButton_8_f = QRadioButton(window_setting)
        self.buttonGroup_8.addButton(self.radioButton_8_f)
        self.radioButton_8_f.setObjectName(u"radioButton_8_f")
        sizePolicy.setHeightForWidth(self.radioButton_8_f.sizePolicy().hasHeightForWidth())
        self.radioButton_8_f.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.radioButton_8_f)


        self.gridLayout.addLayout(self.horizontalLayout_9, 2, 2, 1, 1)

        self.spinBox_8 = QSpinBox(window_setting)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setMaximum(12)

        self.gridLayout.addWidget(self.spinBox_8, 2, 3, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.radioButton_13_xyz = QRadioButton(window_setting)
        self.buttonGroup_13 = QButtonGroup(window_setting)
        self.buttonGroup_13.setObjectName(u"buttonGroup_13")
        self.buttonGroup_13.addButton(self.radioButton_13_xyz)
        self.radioButton_13_xyz.setObjectName(u"radioButton_13_xyz")
        sizePolicy.setHeightForWidth(self.radioButton_13_xyz.sizePolicy().hasHeightForWidth())
        self.radioButton_13_xyz.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.radioButton_13_xyz)

        self.radioButton_13_f = QRadioButton(window_setting)
        self.buttonGroup_13.addButton(self.radioButton_13_f)
        self.radioButton_13_f.setObjectName(u"radioButton_13_f")
        sizePolicy.setHeightForWidth(self.radioButton_13_f.sizePolicy().hasHeightForWidth())
        self.radioButton_13_f.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.radioButton_13_f)


        self.gridLayout.addLayout(self.horizontalLayout_14, 2, 4, 1, 1)

        self.spinBox_13 = QSpinBox(window_setting)
        self.spinBox_13.setObjectName(u"spinBox_13")
        self.spinBox_13.setMaximum(12)

        self.gridLayout.addWidget(self.spinBox_13, 2, 5, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton_4_xyz = QRadioButton(window_setting)
        self.buttonGroup_4 = QButtonGroup(window_setting)
        self.buttonGroup_4.setObjectName(u"buttonGroup_4")
        self.buttonGroup_4.addButton(self.radioButton_4_xyz)
        self.radioButton_4_xyz.setObjectName(u"radioButton_4_xyz")
        sizePolicy.setHeightForWidth(self.radioButton_4_xyz.sizePolicy().hasHeightForWidth())
        self.radioButton_4_xyz.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.radioButton_4_xyz)

        self.radioButton_4_f = QRadioButton(window_setting)
        self.buttonGroup_4.addButton(self.radioButton_4_f)
        self.radioButton_4_f.setObjectName(u"radioButton_4_f")
        sizePolicy.setHeightForWidth(self.radioButton_4_f.sizePolicy().hasHeightForWidth())
        self.radioButton_4_f.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.radioButton_4_f)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.spinBox_4 = QSpinBox(window_setting)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(12)

        self.gridLayout.addWidget(self.spinBox_4, 3, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton_9_xyz = QRadioButton(window_setting)
        self.buttonGroup_9 = QButtonGroup(window_setting)
        self.buttonGroup_9.setObjectName(u"buttonGroup_9")
        self.buttonGroup_9.addButton(self.radioButton_9_xyz)
        self.radioButton_9_xyz.setObjectName(u"radioButton_9_xyz")
        sizePolicy.setHeightForWidth(self.radioButton_9_xyz.sizePolicy().hasHeightForWidth())
        self.radioButton_9_xyz.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.radioButton_9_xyz)

        self.radioButton_9_f = QRadioButton(window_setting)
        self.buttonGroup_9.addButton(self.radioButton_9_f)
        self.radioButton_9_f.setObjectName(u"radioButton_9_f")
        sizePolicy.setHeightForWidth(self.radioButton_9_f.sizePolicy().hasHeightForWidth())
        self.radioButton_9_f.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.radioButton_9_f)


        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 2, 1, 1)

        self.spinBox_9 = QSpinBox(window_setting)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setMaximum(12)

        self.gridLayout.addWidget(self.spinBox_9, 3, 3, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.radioButton_14_xyz = QRadioButton(window_setting)
        self.buttonGroup_14 = QButtonGroup(window_setting)
        self.buttonGroup_14.setObjectName(u"buttonGroup_14")
        self.buttonGroup_14.addButton(self.radioButton_14_xyz)
        self.radioButton_14_xyz.setObjectName(u"radioButton_14_xyz")
        sizePolicy.setHeightForWidth(self.radioButton_14_xyz.sizePolicy().hasHeightForWidth())
        self.radioButton_14_xyz.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.radioButton_14_xyz)

        self.radioButton_14_f = QRadioButton(window_setting)
        self.buttonGroup_14.addButton(self.radioButton_14_f)
        self.radioButton_14_f.setObjectName(u"radioButton_14_f")
        sizePolicy.setHeightForWidth(self.radioButton_14_f.sizePolicy().hasHeightForWidth())
        self.radioButton_14_f.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.radioButton_14_f)


        self.gridLayout.addLayout(self.horizontalLayout_11, 3, 4, 1, 1)

        self.spinBox_14 = QSpinBox(window_setting)
        self.spinBox_14.setObjectName(u"spinBox_14")
        self.spinBox_14.setMaximum(12)

        self.gridLayout.addWidget(self.spinBox_14, 3, 5, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioButton_5_xyz = QRadioButton(window_setting)
        self.buttonGroup_5 = QButtonGroup(window_setting)
        self.buttonGroup_5.setObjectName(u"buttonGroup_5")
        self.buttonGroup_5.addButton(self.radioButton_5_xyz)
        self.radioButton_5_xyz.setObjectName(u"radioButton_5_xyz")
        sizePolicy.setHeightForWidth(self.radioButton_5_xyz.sizePolicy().hasHeightForWidth())
        self.radioButton_5_xyz.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.radioButton_5_xyz)

        self.radioButton_5_f = QRadioButton(window_setting)
        self.buttonGroup_5.addButton(self.radioButton_5_f)
        self.radioButton_5_f.setObjectName(u"radioButton_5_f")
        sizePolicy.setHeightForWidth(self.radioButton_5_f.sizePolicy().hasHeightForWidth())
        self.radioButton_5_f.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.radioButton_5_f)


        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)

        self.spinBox_5 = QSpinBox(window_setting)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMaximum(12)

        self.gridLayout.addWidget(self.spinBox_5, 4, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radioButton_10_xyz = QRadioButton(window_setting)
        self.buttonGroup_10 = QButtonGroup(window_setting)
        self.buttonGroup_10.setObjectName(u"buttonGroup_10")
        self.buttonGroup_10.addButton(self.radioButton_10_xyz)
        self.radioButton_10_xyz.setObjectName(u"radioButton_10_xyz")
        sizePolicy.setHeightForWidth(self.radioButton_10_xyz.sizePolicy().hasHeightForWidth())
        self.radioButton_10_xyz.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.radioButton_10_xyz)

        self.radioButton_10_f = QRadioButton(window_setting)
        self.buttonGroup_10.addButton(self.radioButton_10_f)
        self.radioButton_10_f.setObjectName(u"radioButton_10_f")
        sizePolicy.setHeightForWidth(self.radioButton_10_f.sizePolicy().hasHeightForWidth())
        self.radioButton_10_f.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.radioButton_10_f)


        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 2, 1, 1)

        self.spinBox_10 = QSpinBox(window_setting)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setMaximum(12)

        self.gridLayout.addWidget(self.spinBox_10, 4, 3, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.radioButton_15_xyz = QRadioButton(window_setting)
        self.buttonGroup_15 = QButtonGroup(window_setting)
        self.buttonGroup_15.setObjectName(u"buttonGroup_15")
        self.buttonGroup_15.addButton(self.radioButton_15_xyz)
        self.radioButton_15_xyz.setObjectName(u"radioButton_15_xyz")
        sizePolicy.setHeightForWidth(self.radioButton_15_xyz.sizePolicy().hasHeightForWidth())
        self.radioButton_15_xyz.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.radioButton_15_xyz)

        self.radioButton_15_f = QRadioButton(window_setting)
        self.buttonGroup_15.addButton(self.radioButton_15_f)
        self.radioButton_15_f.setObjectName(u"radioButton_15_f")
        sizePolicy.setHeightForWidth(self.radioButton_15_f.sizePolicy().hasHeightForWidth())
        self.radioButton_15_f.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.radioButton_15_f)


        self.gridLayout.addLayout(self.horizontalLayout_13, 4, 4, 1, 1)

        self.spinBox_15 = QSpinBox(window_setting)
        self.spinBox_15.setObjectName(u"spinBox_15")
        self.spinBox_15.setMaximum(12)

        self.gridLayout.addWidget(self.spinBox_15, 4, 5, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.comboBox = QComboBox(window_setting)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_16.addWidget(self.comboBox)

        self.pushButton_add = QPushButton(window_setting)
        self.pushButton_add.setObjectName(u"pushButton_add")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.pushButton_add)

        self.pushButton_delete = QPushButton(window_setting)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        sizePolicy2.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.pushButton_delete)

        self.pushButton_yes = QPushButton(window_setting)
        self.pushButton_yes.setObjectName(u"pushButton_yes")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_yes.sizePolicy().hasHeightForWidth())
        self.pushButton_yes.setSizePolicy(sizePolicy3)

        self.horizontalLayout_16.addWidget(self.pushButton_yes)

        self.pushButton_no = QPushButton(window_setting)
        self.pushButton_no.setObjectName(u"pushButton_no")
        sizePolicy3.setHeightForWidth(self.pushButton_no.sizePolicy().hasHeightForWidth())
        self.pushButton_no.setSizePolicy(sizePolicy3)

        self.horizontalLayout_16.addWidget(self.pushButton_no)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(window_setting)

        QMetaObject.connectSlotsByName(window_setting)
    # setupUi

    def retranslateUi(self, window_setting):
        window_setting.setWindowTitle(QCoreApplication.translate("window_setting", u"Form", None))
        self.radioButton_1_xyz.setText(QCoreApplication.translate("window_setting", u"XYZ", None))
        self.radioButton_1_f.setText(QCoreApplication.translate("window_setting", u"Fution", None))
        self.radioButton_6_xyz.setText(QCoreApplication.translate("window_setting", u"XYZ", None))
        self.radioButton_6_f.setText(QCoreApplication.translate("window_setting", u"Fution", None))
        self.radioButton_11_xyz.setText(QCoreApplication.translate("window_setting", u"XYZ", None))
        self.radioButton_11_f.setText(QCoreApplication.translate("window_setting", u"Fution", None))
        self.radioButton_2_xyz.setText(QCoreApplication.translate("window_setting", u"XYZ", None))
        self.radioButton_2_f.setText(QCoreApplication.translate("window_setting", u"Fution", None))
        self.radioButton_7_xyz.setText(QCoreApplication.translate("window_setting", u"XYZ", None))
        self.radioButton_7_f.setText(QCoreApplication.translate("window_setting", u"Fution", None))
        self.radioButton_12_xyz.setText(QCoreApplication.translate("window_setting", u"XYZ", None))
        self.radioButton_12_f.setText(QCoreApplication.translate("window_setting", u"Fution", None))
        self.radioButton_3_xyz.setText(QCoreApplication.translate("window_setting", u"XYZ", None))
        self.radioButton_3_f.setText(QCoreApplication.translate("window_setting", u"Fution", None))
        self.radioButton_8_xyz.setText(QCoreApplication.translate("window_setting", u"XYZ", None))
        self.radioButton_8_f.setText(QCoreApplication.translate("window_setting", u"Fution", None))
        self.radioButton_13_xyz.setText(QCoreApplication.translate("window_setting", u"XYZ", None))
        self.radioButton_13_f.setText(QCoreApplication.translate("window_setting", u"Fution", None))
        self.radioButton_4_xyz.setText(QCoreApplication.translate("window_setting", u"XYZ", None))
        self.radioButton_4_f.setText(QCoreApplication.translate("window_setting", u"Fution", None))
        self.radioButton_9_xyz.setText(QCoreApplication.translate("window_setting", u"XYZ", None))
        self.radioButton_9_f.setText(QCoreApplication.translate("window_setting", u"Fution", None))
        self.radioButton_14_xyz.setText(QCoreApplication.translate("window_setting", u"XYZ", None))
        self.radioButton_14_f.setText(QCoreApplication.translate("window_setting", u"Fution", None))
        self.radioButton_5_xyz.setText(QCoreApplication.translate("window_setting", u"XYZ", None))
        self.radioButton_5_f.setText(QCoreApplication.translate("window_setting", u"Fution", None))
        self.radioButton_10_xyz.setText(QCoreApplication.translate("window_setting", u"XYZ", None))
        self.radioButton_10_f.setText(QCoreApplication.translate("window_setting", u"Fution", None))
        self.radioButton_15_xyz.setText(QCoreApplication.translate("window_setting", u"XYZ", None))
        self.radioButton_15_f.setText(QCoreApplication.translate("window_setting", u"Fution", None))
#if QT_CONFIG(tooltip)
        self.pushButton_add.setToolTip(QCoreApplication.translate("window_setting", u"<html><head/><body><p>\u65b0\u5efa\u5206\u7ec4</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_add.setText(QCoreApplication.translate("window_setting", u"+", None))
#if QT_CONFIG(tooltip)
        self.pushButton_delete.setToolTip(QCoreApplication.translate("window_setting", u"<html><head/><body><p>\u5220\u9664\u5f53\u524d\u5206\u7ec4</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_delete.setText(QCoreApplication.translate("window_setting", u"-", None))
        self.pushButton_yes.setText(QCoreApplication.translate("window_setting", u"\u786e\u5b9a", None))
        self.pushButton_no.setText(QCoreApplication.translate("window_setting", u"\u53d6\u6d88", None))
    # retranslateUi

