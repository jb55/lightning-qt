# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/channelspage.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChannelsPage(object):
    def setupUi(self, ChannelsPage):
        ChannelsPage.setObjectName("ChannelsPage")
        ChannelsPage.resize(750, 350)
        self.verticalLayout = QtWidgets.QVBoxLayout(ChannelsPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalFrame_2 = QtWidgets.QFrame(ChannelsPage)
        self.verticalFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineNewChannelId = QtWidgets.QLineEdit(self.verticalFrame_2)
        self.lineNewChannelId.setMinimumSize(QtCore.QSize(100, 0))
        self.lineNewChannelId.setObjectName("lineNewChannelId")
        self.horizontalLayout_2.addWidget(self.lineNewChannelId)
        self.spinNewChannelAmount = QtWidgets.QSpinBox(self.verticalFrame_2)
        self.spinNewChannelAmount.setMinimum(100000)
        self.spinNewChannelAmount.setMaximum(1680000000)
        self.spinNewChannelAmount.setObjectName("spinNewChannelAmount")
        self.horizontalLayout_2.addWidget(self.spinNewChannelAmount)
        self.checkPrivateChannel = QtWidgets.QCheckBox(self.verticalFrame_2)
        self.checkPrivateChannel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkPrivateChannel.setObjectName("checkPrivateChannel")
        self.horizontalLayout_2.addWidget(self.checkPrivateChannel)
        self.buttonNewChannel = QtWidgets.QPushButton(self.verticalFrame_2)
        self.buttonNewChannel.setObjectName("buttonNewChannel")
        self.horizontalLayout_2.addWidget(self.buttonNewChannel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.labelNewChannelResult = QtWidgets.QLabel(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelNewChannelResult.setFont(font)
        self.labelNewChannelResult.setText("")
        self.labelNewChannelResult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNewChannelResult.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelNewChannelResult.setObjectName("labelNewChannelResult")
        self.verticalLayout_4.addWidget(self.labelNewChannelResult)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.line_5 = QtWidgets.QFrame(self.verticalFrame_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_3.addWidget(self.line_5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineCloseId = QtWidgets.QLineEdit(self.verticalFrame_2)
        self.lineCloseId.setMinimumSize(QtCore.QSize(100, 0))
        self.lineCloseId.setObjectName("lineCloseId")
        self.horizontalLayout_3.addWidget(self.lineCloseId)
        self.checkCloseForce = QtWidgets.QCheckBox(self.verticalFrame_2)
        self.checkCloseForce.setStyleSheet("color: rgb(204, 0, 0);")
        self.checkCloseForce.setObjectName("checkCloseForce")
        self.horizontalLayout_3.addWidget(self.checkCloseForce)
        self.spinCloseTimeout = QtWidgets.QSpinBox(self.verticalFrame_2)
        self.spinCloseTimeout.setMinimum(1)
        self.spinCloseTimeout.setMaximum(99999999)
        self.spinCloseTimeout.setProperty("value", 30)
        self.spinCloseTimeout.setObjectName("spinCloseTimeout")
        self.horizontalLayout_3.addWidget(self.spinCloseTimeout)
        self.buttonCloseChannel = QtWidgets.QPushButton(self.verticalFrame_2)
        self.buttonCloseChannel.setObjectName("buttonCloseChannel")
        self.horizontalLayout_3.addWidget(self.buttonCloseChannel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.labelCloseResult = QtWidgets.QLabel(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelCloseResult.setFont(font)
        self.labelCloseResult.setText("")
        self.labelCloseResult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCloseResult.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelCloseResult.setObjectName("labelCloseResult")
        self.verticalLayout_5.addWidget(self.labelCloseResult)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.line_4 = QtWidgets.QFrame(self.verticalFrame_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spinSetFeesBase = QtWidgets.QSpinBox(self.verticalFrame_2)
        self.spinSetFeesBase.setObjectName("spinSetFeesBase")
        self.horizontalLayout_4.addWidget(self.spinSetFeesBase)
        self.label_6 = QtWidgets.QLabel(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.spinSetFeesPpm = QtWidgets.QSpinBox(self.verticalFrame_2)
        self.spinSetFeesPpm.setObjectName("spinSetFeesPpm")
        self.horizontalLayout_4.addWidget(self.spinSetFeesPpm)
        self.label_9 = QtWidgets.QLabel(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.lineSetFeesId = QtWidgets.QLineEdit(self.verticalFrame_2)
        self.lineSetFeesId.setObjectName("lineSetFeesId")
        self.horizontalLayout_4.addWidget(self.lineSetFeesId)
        self.buttonSetFees = QtWidgets.QPushButton(self.verticalFrame_2)
        self.buttonSetFees.setObjectName("buttonSetFees")
        self.horizontalLayout_4.addWidget(self.buttonSetFees)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.labelSetFeesResult = QtWidgets.QLabel(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelSetFeesResult.setFont(font)
        self.labelSetFeesResult.setText("")
        self.labelSetFeesResult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSetFeesResult.setObjectName("labelSetFeesResult")
        self.verticalLayout_7.addWidget(self.labelSetFeesResult)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.verticalFrame_2)
        self.verticalFrame = QtWidgets.QFrame(ChannelsPage)
        self.verticalFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayoutnX = QtWidgets.QVBoxLayout()
        self.verticalLayoutnX.setObjectName("verticalLayoutnX")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.layoutChannelId = QtWidgets.QVBoxLayout()
        self.layoutChannelId.setObjectName("layoutChannelId")
        self.label_4 = QtWidgets.QLabel(self.verticalFrame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.layoutChannelId.addWidget(self.label_4)
        self.line = QtWidgets.QFrame(self.verticalFrame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutChannelId.addWidget(self.line)
        self.horizontalLayout_5.addLayout(self.layoutChannelId)
        self.layoutNodeId = QtWidgets.QVBoxLayout()
        self.layoutNodeId.setObjectName("layoutNodeId")
        self.label_7 = QtWidgets.QLabel(self.verticalFrame)
        self.label_7.setObjectName("label_7")
        self.layoutNodeId.addWidget(self.label_7)
        self.line_2 = QtWidgets.QFrame(self.verticalFrame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutNodeId.addWidget(self.line_2)
        self.horizontalLayout_5.addLayout(self.layoutNodeId)
        self.layoutAmount = QtWidgets.QVBoxLayout()
        self.layoutAmount.setObjectName("layoutAmount")
        self.label_8 = QtWidgets.QLabel(self.verticalFrame)
        self.label_8.setObjectName("label_8")
        self.layoutAmount.addWidget(self.label_8)
        self.line_3 = QtWidgets.QFrame(self.verticalFrame)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.layoutAmount.addWidget(self.line_3)
        self.horizontalLayout_5.addLayout(self.layoutAmount)
        self.verticalLayoutnX.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayoutnX)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.verticalFrame)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ChannelsPage)
        QtCore.QMetaObject.connectSlotsByName(ChannelsPage)

    def retranslateUi(self, ChannelsPage):
        _translate = QtCore.QCoreApplication.translate
        ChannelsPage.setWindowTitle(_translate("ChannelsPage", "Form"))
        self.label.setText(_translate("ChannelsPage", "Create a new channel"))
        self.lineNewChannelId.setToolTip(_translate("ChannelsPage", "The node to open a channel with"))
        self.lineNewChannelId.setPlaceholderText(_translate("ChannelsPage", "node_id@ip:port"))
        self.spinNewChannelAmount.setToolTip(_translate("ChannelsPage", "The amount of satoshi used to fund the channel"))
        self.checkPrivateChannel.setToolTip(_translate("ChannelsPage", "Check this if you don\'t want to announce this channel"))
        self.checkPrivateChannel.setText(_translate("ChannelsPage", "Private"))
        self.buttonNewChannel.setText(_translate("ChannelsPage", "Create channel"))
        self.label_3.setText(_translate("ChannelsPage", "Close a channel"))
        self.lineCloseId.setToolTip(_translate("ChannelsPage", "The Id of a node or a channel (or a short id of a channel)"))
        self.lineCloseId.setPlaceholderText(_translate("ChannelsPage", "channel/peer id"))
        self.checkCloseForce.setToolTip(_translate("ChannelsPage", "CAUTION : If check the channel will be unilateraly closed after timeout"))
        self.checkCloseForce.setText(_translate("ChannelsPage", "Force close"))
        self.spinCloseTimeout.setToolTip(_translate("ChannelsPage", "If close is forced, it is the timeout (default to 30s)"))
        self.buttonCloseChannel.setText(_translate("ChannelsPage", "Close channel"))
        self.label_5.setText(_translate("ChannelsPage", "Set routing fees"))
        self.spinSetFeesBase.setToolTip(_translate("ChannelsPage", "Base routing fees (fixed amount for each routing)"))
        self.label_6.setText(_translate("ChannelsPage", "MSAT"))
        self.spinSetFeesPpm.setToolTip(_translate("ChannelsPage", "Ppm (proportionaly per millionth) fees : amount in sat to charge for each million satoshi routed through"))
        self.label_9.setText(_translate("ChannelsPage", "SAT"))
        self.lineSetFeesId.setToolTip(_translate("ChannelsPage", "Channel, short channel, or peer id to apply this routing fees to. If not specified, set fees globally."))
        self.lineSetFeesId.setPlaceholderText(_translate("ChannelsPage", "Optional"))
        self.buttonSetFees.setText(_translate("ChannelsPage", "Set fees"))
        self.label_2.setText(_translate("ChannelsPage", "Your channels"))
        self.label_4.setText(_translate("ChannelsPage", "Channel id"))
        self.label_7.setText(_translate("ChannelsPage", "Node id"))
        self.label_8.setText(_translate("ChannelsPage", "Amount"))


