# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setFixedSize(375, 303)
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 10, 374, 297))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(14)
        self.verticalLayout_3.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radio_greater = QtGui.QRadioButton(self.groupBox)
        self.radio_greater.setEnabled(True)
        self.radio_greater.setGeometry(QtCore.QRect(10, 78, 100, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_greater.sizePolicy().hasHeightForWidth())
        self.radio_greater.setSizePolicy(sizePolicy)
        self.radio_greater.setObjectName(_fromUtf8("radio_greater"))
        self.radio_noteq = QtGui.QRadioButton(self.groupBox)
        self.radio_noteq.setGeometry(QtCore.QRect(10, 20, 100, 16))
        self.radio_noteq.setChecked(True)
        self.radio_noteq.setObjectName(_fromUtf8("radio_noteq"))
        self.radio_less = QtGui.QRadioButton(self.groupBox)
        self.radio_less.setGeometry(QtCore.QRect(10, 47, 100, 16))
        self.radio_less.setObjectName(_fromUtf8("radio_less"))
        self.verticalLayout_3.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.group_combo = QtGui.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_combo.sizePolicy().hasHeightForWidth())
        self.group_combo.setSizePolicy(sizePolicy)
        self.group_combo.setObjectName(_fromUtf8("group_combo"))
        self.horizontalLayout_7.addWidget(self.group_combo)
        spacerItem = QtGui.QSpacerItem(100, 67, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.feature_combo = QtGui.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feature_combo.sizePolicy().hasHeightForWidth())
        self.feature_combo.setSizePolicy(sizePolicy)
        self.feature_combo.setObjectName(_fromUtf8("feature_combo"))
        self.horizontalLayout_6.addWidget(self.feature_combo)
        spacerItem1 = QtGui.QSpacerItem(100, 67, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_6.addWidget(self.label_5)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_6.addWidget(self.label_7)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btnTemizle = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnTemizle.setObjectName(_fromUtf8("btnTemizle"))
        self.horizontalLayout_5.addWidget(self.btnTemizle)
        self.btnTamam = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnTamam.setObjectName(_fromUtf8("btnTamam"))
        self.horizontalLayout_5.addWidget(self.btnTamam)
        self.btnYardim = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnYardim.setObjectName(_fromUtf8("btnYardim"))
        self.horizontalLayout_5.addWidget(self.btnYardim)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.gridLayoutWidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.radioExact = QtGui.QRadioButton(self.groupBox_2)
        self.radioExact.setGeometry(QtCore.QRect(10, 44, 256, 17))
        self.radioExact.setObjectName(_fromUtf8("radioExact"))
        self.radioDefault = QtGui.QRadioButton(self.groupBox_2)
        self.radioDefault.setGeometry(QtCore.QRect(10, 21, 256, 17))
        self.radioDefault.setChecked(True)
        self.radioDefault.setObjectName(_fromUtf8("radioDefault"))
        self.radioNormalCorrection = QtGui.QRadioButton(self.groupBox_2)
        self.radioNormalCorrection.setGeometry(QtCore.QRect(10, 90, 256, 17))
        self.radioNormalCorrection.setObjectName(_fromUtf8("radioNormalCorrection"))
        self.radioNormal = QtGui.QRadioButton(self.groupBox_2)
        self.radioNormal.setGeometry(QtCore.QRect(10, 67, 256, 17))
        self.radioNormal.setObjectName(_fromUtf8("radioNormal"))
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Form", None))
        self.groupBox.setTitle(_translate("Dialog", "Alternatif Hipotez", None))
        self.radio_greater.setText(_translate("Dialog", "Fark > 0", None))
        self.radio_noteq.setText(_translate("Dialog", "İki taraflı", None))
        self.radio_less.setText(_translate("Dialog", "Fark < 0", None))
        self.label_5.setText(_translate("Dialog", "Grup Seçiniz", None))
        self.label_7.setText(_translate("Dialog", "Özellik Seçiniz", None))
        self.btnTemizle.setText(_translate("Dialog", "Temizle", None))
        self.btnTamam.setText(_translate("Dialog", "Tamam", None))
        self.btnYardim.setText(_translate("Dialog", "Yardım", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Test Tipi", None))
        self.radioExact.setText(_translate("Dialog", "Exact", None))
        self.radioDefault.setText(_translate("Dialog", "Default", None))
        self.radioNormalCorrection.setText(_translate("Dialog", "Normal Approximation with continuity correction", None))
        self.radioNormal.setText(_translate("Dialog", "Normal Approximation", None))

