# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_settings.ui'
#
# Created: Thu May 05 12:29:28 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MetatoolsSettingsDialog(object):
    def setupUi(self, MetatoolsSettingsDialog):
        MetatoolsSettingsDialog.setObjectName(_fromUtf8("MetatoolsSettingsDialog"))
        MetatoolsSettingsDialog.resize(372, 300)
        self.verticalLayout = QtGui.QVBoxLayout(MetatoolsSettingsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(MetatoolsSettingsDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.generalTab = QtGui.QWidget()
        self.generalTab.setObjectName(_fromUtf8("generalTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.generalTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.generalTab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.leFilterFileName = QtGui.QLineEdit(self.groupBox)
        self.leFilterFileName.setObjectName(_fromUtf8("leFilterFileName"))
        self.horizontalLayout.addWidget(self.leFilterFileName)
        self.btnSelectFilter = QtGui.QPushButton(self.groupBox)
        self.btnSelectFilter.setObjectName(_fromUtf8("btnSelectFilter"))
        self.horizontalLayout.addWidget(self.btnSelectFilter)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.generalTab)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cmbImgFormat = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbImgFormat.sizePolicy().hasHeightForWidth())
        self.cmbImgFormat.setSizePolicy(sizePolicy)
        self.cmbImgFormat.setObjectName(_fromUtf8("cmbImgFormat"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.cmbImgFormat)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.generalTab)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.defaultProfileLabel = QtGui.QLabel(self.groupBox_3)
        self.defaultProfileLabel.setObjectName(_fromUtf8("defaultProfileLabel"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.defaultProfileLabel)
        self.defaultProfileComboBox = QtGui.QComboBox(self.groupBox_3)
        self.defaultProfileComboBox.setObjectName(_fromUtf8("defaultProfileComboBox"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.defaultProfileComboBox)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tabWidget.addTab(self.generalTab, _fromUtf8(""))
        self.isoTab = QtGui.QWidget()
        self.isoTab.setObjectName(_fromUtf8("isoTab"))
        self.formLayout = QtGui.QFormLayout(self.isoTab)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.isoTab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.cmbIsoViewStylesheet = QtGui.QComboBox(self.isoTab)
        self.cmbIsoViewStylesheet.setObjectName(_fromUtf8("cmbIsoViewStylesheet"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cmbIsoViewStylesheet)
        self.tabWidget.addTab(self.isoTab, _fromUtf8(""))
        self.fgdcTab = QtGui.QWidget()
        self.fgdcTab.setObjectName(_fromUtf8("fgdcTab"))
        self.formLayout_4 = QtGui.QFormLayout(self.fgdcTab)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_4 = QtGui.QLabel(self.fgdcTab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.cmbFgdcViewStylesheet = QtGui.QComboBox(self.fgdcTab)
        self.cmbFgdcViewStylesheet.setObjectName(_fromUtf8("cmbFgdcViewStylesheet"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.cmbFgdcViewStylesheet)
        self.tabWidget.addTab(self.fgdcTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(MetatoolsSettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MetatoolsSettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MetatoolsSettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MetatoolsSettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MetatoolsSettingsDialog)

    def retranslateUi(self, MetatoolsSettingsDialog):
        MetatoolsSettingsDialog.setWindowTitle(QtGui.QApplication.translate("MetatoolsSettingsDialog", "Metatools settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MetatoolsSettingsDialog", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MetatoolsSettingsDialog", "Filter file", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectFilter.setText(QtGui.QApplication.translate("MetatoolsSettingsDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MetatoolsSettingsDialog", "Preview image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MetatoolsSettingsDialog", "Image format", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MetatoolsSettingsDialog", "Default profile", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultProfileLabel.setText(QtGui.QApplication.translate("MetatoolsSettingsDialog", "Select profile", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generalTab), QtGui.QApplication.translate("MetatoolsSettingsDialog", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MetatoolsSettingsDialog", "View stylesheet", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.isoTab), QtGui.QApplication.translate("MetatoolsSettingsDialog", "ISO 19115", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MetatoolsSettingsDialog", "View stylesheet", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fgdcTab), QtGui.QApplication.translate("MetatoolsSettingsDialog", "FGDC", None, QtGui.QApplication.UnicodeUTF8))

