# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_application_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setStyleSheet("* {\n"
"    font-family: \'Microsoft YaHei UI\', sans-serif\n"
"}\n"
"")
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.central_widget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 15))
        self.menubar.setMinimumSize(QtCore.QSize(0, 10))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_view = QtWidgets.QMenu(self.menubar)
        self.menu_view.setObjectName("menu_view")
        MainWindow.setMenuBar(self.menubar)
        self.dock_widget_2 = QtWidgets.QDockWidget(MainWindow)
        self.dock_widget_2.setMinimumSize(QtCore.QSize(400, 200))
        self.dock_widget_2.setObjectName("dock_widget_2")
        self.dock_widget_content = QtWidgets.QWidget()
        self.dock_widget_content.setObjectName("dock_widget_content")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dock_widget_content)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_widget = QtWidgets.QTabWidget(self.dock_widget_content)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tab_widget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_widget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tab_widget)
        self.dock_widget_2.setWidget(self.dock_widget_content)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_widget_2)
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.menu_file.addAction(self.action_quit)
        self.menu_help.addAction(self.action_about)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt Demo"))
        self.menu_file.setTitle(_translate("MainWindow", "&File"))
        self.menu_help.setTitle(_translate("MainWindow", "&Help"))
        self.menu_view.setTitle(_translate("MainWindow", "&View"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_1), _translate("MainWindow", "Tab 1"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.action_quit.setText(_translate("MainWindow", "&Quit"))
        self.action_about.setText(_translate("MainWindow", "&About..."))
