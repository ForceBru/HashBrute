# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'brute.ui'
#
# Created: Thu Jan 16 19:40:05 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

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

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName(_fromUtf8("GroupBox"))
        GroupBox.resize(340, 250)
        GroupBox.setMinimumSize(QtCore.QSize(270, 175))
        GroupBox.setMaximumSize(QtCore.QSize(340, 250))
        GroupBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        GroupBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        GroupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gridLayout = QtGui.QGridLayout(GroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.start = QtGui.QToolButton(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy)
        self.start.setStyleSheet(_fromUtf8("background-color: rgb(7, 255, 44);"))
        self.start.setObjectName(_fromUtf8("start"))
        self.horizontalLayout.addWidget(self.start)
        self.stop = QtGui.QToolButton(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop.sizePolicy().hasHeightForWidth())
        self.stop.setSizePolicy(sizePolicy)
        self.stop.setStyleSheet(_fromUtf8("background-color: rgb(255, 58, 23);"))
        self.stop.setObjectName(_fromUtf8("stop"))
        self.horizontalLayout.addWidget(self.stop)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 2)
        self.label = QtGui.QLabel(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bookman Old Style"))
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.results = QtGui.QLabel(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.results.sizePolicy().hasHeightForWidth())
        self.results.setSizePolicy(sizePolicy)
        self.results.setScaledContents(True)
        self.results.setAlignment(QtCore.Qt.AlignCenter)
        self.results.setObjectName(_fromUtf8("results"))
        self.gridLayout.addWidget(self.results, 3, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.settings_hashType = QtGui.QToolButton(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_hashType.sizePolicy().hasHeightForWidth())
        self.settings_hashType.setSizePolicy(sizePolicy)
        self.settings_hashType.setShortcut(_fromUtf8(""))
        self.settings_hashType.setCheckable(False)
        self.settings_hashType.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.settings_hashType.setAutoRaise(True)
        self.settings_hashType.setArrowType(QtCore.Qt.NoArrow)
        self.settings_hashType.setObjectName(_fromUtf8("settings_hashType"))
        self.horizontalLayout_2.addWidget(self.settings_hashType)
        self.word_len_min_spin = QtGui.QSpinBox(GroupBox)
        self.word_len_min_spin.setMinimum(1)
        self.word_len_min_spin.setObjectName(_fromUtf8("word_len_min_spin"))
        self.horizontalLayout_2.addWidget(self.word_len_min_spin)
        self.word_len_spin = QtGui.QSpinBox(GroupBox)
        self.word_len_spin.setStyleSheet(_fromUtf8(""))
        self.word_len_spin.setWrapping(False)
        self.word_len_spin.setFrame(False)
        self.word_len_spin.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.word_len_spin.setSpecialValueText(_fromUtf8(""))
        self.word_len_spin.setAccelerated(True)
        self.word_len_spin.setSuffix(_fromUtf8(""))
        self.word_len_spin.setPrefix(_fromUtf8(""))
        self.word_len_spin.setMinimum(2)
        self.word_len_spin.setProperty("value", 10)
        self.word_len_spin.setObjectName(_fromUtf8("word_len_spin"))
        self.horizontalLayout_2.addWidget(self.word_len_spin)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.Hash = QtGui.QLineEdit(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Hash.sizePolicy().hasHeightForWidth())
        self.Hash.setSizePolicy(sizePolicy)
        self.Hash.setStyleSheet(_fromUtf8("selection-background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(120, 216, 127, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.852273 rgba(83, 216, 132, 250));\n"
"font: italic 8pt \"Courier New\";"))
        self.Hash.setMaxLength(96)
        self.Hash.setObjectName(_fromUtf8("Hash"))
        self.gridLayout.addWidget(self.Hash, 2, 0, 1, 2)

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(_translate("GroupBox", "Bruteforce", None))
        GroupBox.setTitle(_translate("GroupBox", "Bruteforce", None))
        self.start.setText(_translate("GroupBox", "Start bruteforce!", None))
        self.stop.setText(_translate("GroupBox", "Stop bruteforce!", None))
        self.label.setText(_translate("GroupBox", "Input your hash ", None))
        self.results.setText(_translate("GroupBox", "Here will be the results", None))
        self.settings_hashType.setToolTip(_translate("GroupBox", "<html><head/><body><p>Type of your hash. Hashes of this type will be generated.</p></body></html>", None))
        self.settings_hashType.setText(_translate("GroupBox", "Hash type", None))
        self.word_len_min_spin.setToolTip(_translate("GroupBox", "<html><head/><body><p>Minimum word length</p></body></html>", None))
        self.word_len_spin.setToolTip(_translate("GroupBox", "<html><head/><body><p>Maximum word length</p></body></html>", None))
        self.Hash.setPlaceholderText(_translate("GroupBox", "Hash", None))

