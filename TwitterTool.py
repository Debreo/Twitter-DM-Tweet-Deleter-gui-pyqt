# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TwitterTool.ui'
#
# Created: Thu Dec 18 16:10:40 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtWebKit
import sys, time
import tweepy

from random import randint
import os
from keys import keys1, keys2, keys3, keys4
import twitter_api



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

class Ui_Form(QtGui.QWidget):


    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)


    def setupUi(self, Form):

        #Form Setup and Size Policy

        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1389, 805)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("twitter images/twitter-big.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.Accounts_btn = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)


        #Account Choice Button

        sizePolicy.setHeightForWidth(self.Accounts_btn.sizePolicy().hasHeightForWidth())
        self.Accounts_btn.setSizePolicy(sizePolicy)
        self.Accounts_btn.setObjectName(_fromUtf8("Accounts_btn"))
        self.Accounts_btn.addItem(_fromUtf8(""))
        self.Accounts_btn.addItem(_fromUtf8(""))
        self.Accounts_btn.addItem(_fromUtf8(""))
        self.Accounts_btn.addItem(_fromUtf8(""))
        self.Accounts_btn.addItem(_fromUtf8(""))
        self.Accounts_btn.addItem(_fromUtf8(""))
        self.Accounts_btn.addItem(_fromUtf8(""))
        self.Accounts_btn.addItem(_fromUtf8(""))
        self.Accounts_btn.addItem(_fromUtf8(""))
        self.Accounts_btn.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.Accounts_btn)


        #Tab Widget


        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Twitter_tab = QtGui.QWidget()
        self.Twitter_tab.setObjectName(_fromUtf8("Twitter_tab"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.Twitter_tab)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)




        #Back Button

        self.back_btn_2 = QtGui.QPushButton(self.Twitter_tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("twitter images/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn_2.setIcon(icon1)
        self.back_btn_2.setObjectName(_fromUtf8("back_btn_2"))
        self.horizontalLayout.addWidget(self.back_btn_2)
        self.refresh_btn_2 = QtGui.QPushButton(self.Twitter_tab)


        #Refresh Button

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("twitter images/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_btn_2.setIcon(icon2)
        self.refresh_btn_2.setObjectName(_fromUtf8("refresh_btn_2"))
        self.horizontalLayout.addWidget(self.refresh_btn_2)


        #Url Label
        
        self.url_line = QtGui.QLineEdit(self.Twitter_tab)
        self.url_line.setObjectName(_fromUtf8("url_line"))
        self.horizontalLayout.addWidget(self.url_line)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)



        #Go Button

        self.go_btn = QtGui.QPushButton(self.Twitter_tab)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("twitter images/twitter_standing.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.go_btn.setIcon(icon3)
        self.go_btn.setObjectName(_fromUtf8("go_btn"))
        self.horizontalLayout.addWidget(self.go_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)



        #Twitter Tab

        self.tabWidget_2 = QtGui.QTabWidget(self.Twitter_tab)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))


        #Account 1 Webview

        self.Account_1 = QtGui.QWidget()
        self.Account_1.setObjectName(_fromUtf8("Account_1"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.Account_1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.webView = QtWebKit.QWebView(self.Account_1)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("https://twitter.com/")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.horizontalLayout_16.addWidget(self.webView)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_16)
        self.tabWidget_2.addTab(self.Account_1, _fromUtf8(""))



        #Account 2 Webview

        self.Account_2 = QtGui.QWidget()
        self.Account_2.setObjectName(_fromUtf8("Account_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.Account_2)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.webView_2 = QtWebKit.QWebView(self.Account_2)
        self.webView_2.setUrl(QtCore.QUrl(_fromUtf8("https://twitter.com/")))
        self.webView_2.setObjectName(_fromUtf8("webView_2"))
        self.horizontalLayout_5.addWidget(self.webView_2)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.tabWidget_2.addTab(self.Account_2, _fromUtf8(""))



        #Account 3 Webview
        
        self.Account_3 = QtGui.QWidget()
        self.Account_3.setObjectName(_fromUtf8("Account_3"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.Account_3)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.webView_3 = QtWebKit.QWebView(self.Account_3)
        self.webView_3.setUrl(QtCore.QUrl(_fromUtf8("https://twitter.com/")))
        self.webView_3.setObjectName(_fromUtf8("webView_3"))
        self.horizontalLayout_7.addWidget(self.webView_3)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_7)
        self.tabWidget_2.addTab(self.Account_3, _fromUtf8(""))


        #Account 4 Webview

        self.Account_4 = QtGui.QWidget()
        self.Account_4.setObjectName(_fromUtf8("Account_4"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.Account_4)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.webView_4 = QtWebKit.QWebView(self.Account_4)
        self.webView_4.setUrl(QtCore.QUrl(_fromUtf8("https://twitter.com/")))
        self.webView_4.setObjectName(_fromUtf8("webView_4"))
        self.horizontalLayout_14.addWidget(self.webView_4)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_14)
        self.tabWidget_2.addTab(self.Account_4, _fromUtf8(""))


        #Account 5 Webview

        self.Account_5 = QtGui.QWidget()
        self.Account_5.setObjectName(_fromUtf8("Account_5"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.Account_5)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.webView_5 = QtWebKit.QWebView(self.Account_5)
        self.webView_5.setUrl(QtCore.QUrl(_fromUtf8("https://twitter.com/")))
        self.webView_5.setObjectName(_fromUtf8("webView_5"))
        self.horizontalLayout_3.addWidget(self.webView_5)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_3)
        self.tabWidget_2.addTab(self.Account_5, _fromUtf8(""))


        #Account 6 Webview

        self.Account_6 = QtGui.QWidget()
        self.Account_6.setObjectName(_fromUtf8("Account_6"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.Account_6)
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.webView_6 = QtWebKit.QWebView(self.Account_6)
        self.webView_6.setUrl(QtCore.QUrl(_fromUtf8("https://twitter.com/")))
        self.webView_6.setObjectName(_fromUtf8("webView_6"))
        self.horizontalLayout_18.addWidget(self.webView_6)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_18)
        self.tabWidget_2.addTab(self.Account_6, _fromUtf8(""))



        #Account 7 Webview

        self.Account_7 = QtGui.QWidget()
        self.Account_7.setObjectName(_fromUtf8("Account_7"))
        self.horizontalLayout_21 = QtGui.QHBoxLayout(self.Account_7)
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.webView_7 = QtWebKit.QWebView(self.Account_7)
        self.webView_7.setUrl(QtCore.QUrl(_fromUtf8("https://twitter.com/")))
        self.webView_7.setObjectName(_fromUtf8("webView_7"))
        self.horizontalLayout_20.addWidget(self.webView_7)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_20)
        self.tabWidget_2.addTab(self.Account_7, _fromUtf8(""))


        #Account 8 Webview

        self.Account_8 = QtGui.QWidget()
        self.Account_8.setObjectName(_fromUtf8("Account_8"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout(self.Account_8)
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.webView_8 = QtWebKit.QWebView(self.Account_8)
        self.webView_8.setUrl(QtCore.QUrl(_fromUtf8("https://twitter.com/")))
        self.webView_8.setObjectName(_fromUtf8("webView_8"))
        self.horizontalLayout_22.addWidget(self.webView_8)
        self.horizontalLayout_23.addLayout(self.horizontalLayout_22)
        self.tabWidget_2.addTab(self.Account_8, _fromUtf8(""))


        #Account 9 Webview

        self.Account_9 = QtGui.QWidget()
        self.Account_9.setObjectName(_fromUtf8("Account_9"))
        self.horizontalLayout_25 = QtGui.QHBoxLayout(self.Account_9)
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.webView_9 = QtWebKit.QWebView(self.Account_9)
        self.webView_9.setUrl(QtCore.QUrl(_fromUtf8("https://twitter.com/")))
        self.webView_9.setObjectName(_fromUtf8("webView_9"))
        self.horizontalLayout_24.addWidget(self.webView_9)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_24)
        self.tabWidget_2.addTab(self.Account_9, _fromUtf8(""))


        #Account 10 Webview

        self.Account_10 = QtGui.QWidget()
        self.Account_10.setObjectName(_fromUtf8("Account_10"))
        self.horizontalLayout_27 = QtGui.QHBoxLayout(self.Account_10)
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.webView_10 = QtWebKit.QWebView(self.Account_10)
        self.webView_10.setUrl(QtCore.QUrl(_fromUtf8("https://twitter.com/")))
        self.webView_10.setObjectName(_fromUtf8("webView_10"))
        self.horizontalLayout_26.addWidget(self.webView_10)
        self.horizontalLayout_27.addLayout(self.horizontalLayout_26)
        self.tabWidget_2.addTab(self.Account_10, _fromUtf8(""))


        #Spacer and Layout

        self.verticalLayout_10.addWidget(self.tabWidget_2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(400, 0, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)


        #Delete Button

        self.Delete_btn = QtGui.QPushButton(self.Twitter_tab)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("twitter images/red-delete-button.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Delete_btn.setIcon(icon4)
        self.Delete_btn.setObjectName(_fromUtf8("Delete_btn"))
        self.horizontalLayout_2.addWidget(self.Delete_btn)
        spacerItem3 = QtGui.QSpacerItem(400, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)


        #Twitter Icon

        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("twitter images/twitter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Twitter_tab, icon5, _fromUtf8(""))


        #Message Tab

        self.Message_tab = QtGui.QWidget()
        self.Message_tab.setObjectName(_fromUtf8("Message_tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.Message_tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.twitter_label = QtGui.QLabel(self.Message_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twitter_label.sizePolicy().hasHeightForWidth())


        #Twitter Banner


        self.twitter_label.setSizePolicy(sizePolicy)
        self.twitter_label.setText(_fromUtf8(""))
        self.twitter_label.setTextFormat(QtCore.Qt.AutoText)
        self.twitter_label.setPixmap(QtGui.QPixmap(_fromUtf8("twitter images/twitter_new_banner_620px.jpg")))
        self.twitter_label.setObjectName(_fromUtf8("twitter_label"))
        self.horizontalLayout_10.addWidget(self.twitter_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))

        #User Handles Button Text File Input


        self.handles_btn = QtGui.QToolButton(self.Message_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.handles_btn.sizePolicy().hasHeightForWidth())
        self.handles_btn.setSizePolicy(sizePolicy)
        self.handles_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("twitter images/msn.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.handles_btn.setIcon(icon6)
        self.handles_btn.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.handles_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.handles_btn.setObjectName(_fromUtf8("handles_btn"))
        self.horizontalLayout_11.addWidget(self.handles_btn)
        self.line_2 = QtGui.QFrame(self.Message_tab)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_11.addWidget(self.line_2)


        #Messages Button for Text File Input



        self.message_btn = QtGui.QToolButton(self.Message_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_btn.sizePolicy().hasHeightForWidth())
        self.message_btn.setSizePolicy(sizePolicy)
        self.message_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("twitter images/notepad.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.message_btn.setIcon(icon7)
        self.message_btn.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.message_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.message_btn.setObjectName(_fromUtf8("message_btn"))
        self.horizontalLayout_11.addWidget(self.message_btn)
        self.line = QtGui.QFrame(self.Message_tab)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_11.addWidget(self.line)



        #Direct Message Button

        self.dm_btn = QtGui.QPushButton(self.Message_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dm_btn.sizePolicy().hasHeightForWidth())
        self.dm_btn.setSizePolicy(sizePolicy)
        self.dm_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("twitter images/rss.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dm_btn.setIcon(icon8)
        self.dm_btn.setObjectName(_fromUtf8("dm_btn"))
        self.horizontalLayout_11.addWidget(self.dm_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))

        #Remove Button

        self.pushButton_2 = QtGui.QPushButton(self.Message_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("twitter images/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon9)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_11.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.treeWidget = QtGui.QTreeWidget(self.Message_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())


        #Tree Widget File Viewer


        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(300)
        self.treeWidget.header().setMinimumSectionSize(33)
        self.horizontalLayout_12.addWidget(self.treeWidget)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("twitter images/email2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Message_tab, icon10, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)


        #Translate UI Form and Tab order


        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        



        #Gui Connections 

        self.connect(self.back_btn_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.webView.back)
        self.connect(self.refresh_btn_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.webView.reload)
        self.connect(self.refresh_btn_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.webView_2.reload)
        self.connect(self.refresh_btn_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.webView_3.reload)
        self.connect(self.refresh_btn_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.webView_4.reload)
        self.connect(self.webView, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.feeds)
        self.connect(self.go_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.feeds)
        self.connect(self.webView, QtCore.SIGNAL(_fromUtf8("urlChanged(const QUrl)")), self.url_changed)
        self.connect(self.webView_2, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.feeds)
        self.connect(self.webView_3, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.feeds)
        self.connect(self.webView_4, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.feeds)
        self.connect(self.Delete_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.user_accounts)
        self.connect(self.Accounts_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.user_accounts)
        self.connect(self.Delete_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.webView.reload)
        self.connect(self.Delete_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.webView_2.reload)
        self.connect(self.Delete_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.webView_3.reload)
        self.connect(self.Delete_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.webView_4.reload)
        self.connect(self.handles_btn,QtCore.SIGNAL(_fromUtf8("clicked()")), self.slot1)
        self.connect(self.message_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.slot2)
        self.connect(self.dm_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.user_acnt_dm)
        self.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked")), self.abort)



    #User Accounts Chosen Calls Function For Deleting Tweets


    def user_accounts(self):
        if self.Accounts_btn.currentIndex() == 0:
            print("Entries Being Removed From Account 1")
            twitter_api.delete_tweets(CONSUMER_KEY = keys1["consumer_key"], CONSUMER_SECRET = keys1['consumer_secret'], ACCESS_TOKEN = keys1['access_token'], ACCESS_SECRET = keys1['access_token_secret'])
        elif self.Accounts_btn.currentIndex() == 1:
            print("Entries Being Removed From Account 2")
            twitter_api.delete_tweets(CONSUMER_KEY = keys2["consumer_key"], CONSUMER_SECRET = keys2['consumer_secret'], ACCESS_TOKEN = keys2['access_token'], ACCESS_SECRET = keys2['access_token_secret'])
        elif self.Accounts_btn.currentIndex() == 2:
            print("Entries Being Removed From Account 3")
            twitter_api.delete_tweets(CONSUMER_KEY = keys3["consumer_key"], CONSUMER_SECRET = keys3['consumer_secret'], ACCESS_TOKEN = keys3['access_token'], ACCESS_SECRET = keys3['access_token_secret'])
        elif self.Accounts_btn.currentIndex() == 3:
            print("Entries Being Removed From Account 4")
            twitter_api.delete_tweets(CONSUMER_KEY = keys4["consumer_key"], CONSUMER_SECRET = keys4['consumer_secret'], ACCESS_TOKEN = keys4['access_token'], ACCESS_SECRET = keys4['access_token_secret'])

        else:
            pass


    #User Accounts Chosen Calls Function For User DM


    def user_acnt_dm(self):
        if self.Accounts_btn.currentIndex() == 0:
            twitter_api.dm(self.users, self.messages, CONSUMER_KEY = keys1["consumer_key"], CONSUMER_SECRET = keys1['consumer_secret'], ACCESS_TOKEN = keys1['access_token'], ACCESS_SECRET = keys1['access_token_secret'])
        elif self.Accounts_btn.currentIndex() == 1:
            twitter_api.dm(self.users, self.messages, CONSUMER_KEY = keys2["consumer_key"], CONSUMER_SECRET = keys2['consumer_secret'], ACCESS_TOKEN = keys2['access_token'], ACCESS_SECRET = keys2['access_token_secret'])
        elif self.Accounts_btn.currentIndex() == 2:
            twitter_api.dm(self.users, self.messages, CONSUMER_KEY = keys3["consumer_key"], CONSUMER_SECRET = keys3['consumer_secret'], ACCESS_TOKEN = keys3['access_token'], ACCESS_SECRET = keys3['access_token_secret'])
        elif self.Accounts_btn.currentIndex() == 3:
            twitter_api.dm(self.users, self.messages, CONSUMER_KEY = keys4["consumer_key"], CONSUMER_SECRET = keys4['consumer_secret'], ACCESS_TOKEN = keys4['access_token'], ACCESS_SECRET = keys4['access_token_secret'])
        else:
            pass




    def retranslateUi(self, Form):

        #Window Title

        Form.setWindowTitle(_translate("Form", "TwitterTool ", None))


        #Accounts


        self.Accounts_btn.setItemText(0, _translate("Form", "Account 1", None))
        self.Accounts_btn.setItemText(1, _translate("Form", "Account 2", None))
        self.Accounts_btn.setItemText(2, _translate("Form", "Account 3", None))
        self.Accounts_btn.setItemText(3, _translate("Form", "Account 4", None))
        self.Accounts_btn.setItemText(4, _translate("Form", "Account 5", None))
        self.Accounts_btn.setItemText(5, _translate("Form", "Account 6", None))
        self.Accounts_btn.setItemText(6, _translate("Form", "Account 7", None))
        self.Accounts_btn.setItemText(7, _translate("Form", "Account 8", None))
        self.Accounts_btn.setItemText(8, _translate("Form", "Account 9", None))
        self.Accounts_btn.setItemText(9, _translate("Form", "Account 10", None))

        #Back/Refresh/Go Button

        self.back_btn_2.setText(_translate("Form", "Back", None))
        self.refresh_btn_2.setText(_translate("Form", "Refresh", None))
        self.go_btn.setText(_translate("Form", "Go", None))

        #User Accounts Tabs

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Account_1), _translate("Form", "Account 1", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Account_2), _translate("Form", "Account 2", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Account_3), _translate("Form", "Account 3", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Account_4), _translate("Form", "Account 4", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Account_5), _translate("Form", "Account 5", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Account_6), _translate("Form", "Account 6", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Account_7), _translate("Form", "Account 7", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Account_8), _translate("Form", "Account 8", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Account_9), _translate("Form", "Account 9", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Account_10), _translate("Form", "Account 10", None))

        #Function Buttons

        self.Delete_btn.setText(_translate("Form", "Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Twitter_tab), _translate("Form", "Twitter", None))
        self.handles_btn.setText(_translate("Form", "Handles", None))
        self.message_btn.setText(_translate("Form", "Message", None))
        self.dm_btn.setText(_translate("Form", "Direct Message", None))
        self.pushButton_2.setText(_translate("Form", "Remove", None))
        self.treeWidget.headerItem().setText(0, _translate("Form", "Uploaded Files", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Message_tab), _translate("Form", "Message", None))


        #Default Url Twitter

        self.default_url = "https://www.twitter.com/"
        self.url_line.setText(self.default_url)
        self.feeds()

    def feeds(self):

        url = self.url_line.text() if self.url_line.text() else self.set_Url
        self.webView.load(QtCore.QUrl(url))


    def url_changed(self, url):

        """Triggered when the url is changed"""

        self.url_line.setText(url.toString())


    def slot1(self):

        """Opens Text File and Reads User Handles"""
        
        handles = QtGui.QFileDialog.getOpenFileName(self, 'Open File', 'handles')

        f = open(handles, "r")
        users = f.readlines()
        f.close()
        self.users = users
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", handles, None))



    def slot2(self):
        """Opens Text File and Reads Message To Send"""

        
        texts = QtGui.QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()")
        words = open(texts, "r")
        messages = words.readlines()
        words.close()
        self.messages = messages
        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", texts, None))



    def abort(self):
        quit(self)






if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())
