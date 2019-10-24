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
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("/*\n"
" * This stylesheet contains almost all styles in this UI.\n"
" * Inspired by JetBrains IDEs.\n"
" */\n"
"\n"
"* {\n"
"    font-family: \'Microsoft YaHei UI\', sans-serif;\n"
"    background-color: #3c3f41;\n"
"    color: #bbbbbb;\n"
"}\n"
"\n"
"QPushButton {\n"
"    width: 109px;\n"
"    height: 36px;\n"
"    background-color: #4c5052;\n"
"    border-style: solid;\n"
"    border-color: #5e6060;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    height: 36px;\n"
"    background-color: #45494a;\n"
"    border-style: solid;\n"
"    border-color: #646464;\n"
"    border-width: 1px;\n"
"    border-radius: 1px;\n"
"}\n"
"\n"
"QPushButton:focus, QPushButton:pressed, QLineEdit:focus {\n"
"    border-color: #3d6185;\n"
"    border-width: 3px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #2b2b2b;\n"
"}\n"
"\n"
"QMenuBar, QMenuBar::item, QMenuBar::item:selected {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    padding-top: 8px;\n"
"    padding-bottom: 8px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QMenu {\n"
"    padding: 0px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #515151;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding-top: 8px;\n"
"    padding-bottom: 8px;\n"
"    padding-left: 37px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"/* FIXME: Ugly check signs in menus! */\n"
"\n"
"QListWidget, QTableWidget {\n"
"    background-color: #414547;\n"
"    alternate-background-color: #3c3f41;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #323232;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    color: #bbbbbb;\n"
"    padding-top: 4px;\n"
"    padding-bottom: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:pressed, QMenu::item:selected, QListWidget::item:selected {\n"
"    background-color: #4b6eaf;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 12px;\n"
"    padding-left: 0px;\n"
"    padding-right: 0px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 12px;\n"
"    padding-top: 0px;\n"
"    padding-bottom: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    border-style: none;\n"
"    background-color: #4d4d4d;\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    background-color: #5c5c5c;\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal, QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal, QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    height: 0px;\n"
"    width: 0px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border-top: 1px solid #323232;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-style: none;\n"
"    background-color: #3c3f41;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    padding-top: 7px;\n"
"    padding-bottom: 7px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: #27292a\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-bottom: 5px solid #747a80\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color:#3c3f41;\n"
"    border-style: solid;\n"
"}\n"
"")
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setStyleSheet("")
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_display_panel = QtWidgets.QWidget(self.central_widget)
        self.widget_display_panel.setStyleSheet("")
        self.widget_display_panel.setObjectName("widget_display_panel")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_display_panel)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_display_panel = QtWidgets.QLabel(self.widget_display_panel)
        self.label_display_panel.setObjectName("label_display_panel")
        self.verticalLayout_3.addWidget(self.label_display_panel)
        self.textedit_display_panel = QtWidgets.QTextEdit(self.widget_display_panel)
        self.textedit_display_panel.setStyleSheet("font-family: \'Fira Code\', Consolas, \'Courier New\', monospace")
        self.textedit_display_panel.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textedit_display_panel.setReadOnly(True)
        self.textedit_display_panel.setObjectName("textedit_display_panel")
        self.verticalLayout_3.addWidget(self.textedit_display_panel)
        self.verticalLayout_2.addWidget(self.widget_display_panel)
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setMinimumSize(QtCore.QSize(0, 10))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_file.sizePolicy().hasHeightForWidth())
        self.menu_file.setSizePolicy(sizePolicy)
        self.menu_file.setMinimumSize(QtCore.QSize(300, 0))
        self.menu_file.setMaximumSize(QtCore.QSize(300, 16777215))
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setMinimumSize(QtCore.QSize(300, 0))
        self.menu_help.setMaximumSize(QtCore.QSize(300, 16777215))
        self.menu_help.setObjectName("menu_help")
        self.menu_view = QtWidgets.QMenu(self.menubar)
        self.menu_view.setMinimumSize(QtCore.QSize(300, 0))
        self.menu_view.setMaximumSize(QtCore.QSize(300, 16777215))
        self.menu_view.setObjectName("menu_view")
        MainWindow.setMenuBar(self.menubar)
        self.sidebar = QtWidgets.QDockWidget(MainWindow)
        self.sidebar.setMinimumSize(QtCore.QSize(300, 200))
        self.sidebar.setObjectName("sidebar")
        self.sidebar_content = QtWidgets.QWidget()
        self.sidebar_content.setObjectName("sidebar_content")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sidebar_content)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_widget = QtWidgets.QTabWidget(self.sidebar_content)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_file = QtWidgets.QWidget()
        self.tab_file.setObjectName("tab_file")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_file)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.hortizontal_layout_open_file = QtWidgets.QHBoxLayout()
        self.hortizontal_layout_open_file.setObjectName("hortizontal_layout_open_file")
        self.label_path = QtWidgets.QLabel(self.tab_file)
        self.label_path.setObjectName("label_path")
        self.hortizontal_layout_open_file.addWidget(self.label_path)
        self.lineedit_path = QtWidgets.QLineEdit(self.tab_file)
        self.lineedit_path.setObjectName("lineedit_path")
        self.hortizontal_layout_open_file.addWidget(self.lineedit_path)
        self.pushbutton_browse = QtWidgets.QPushButton(self.tab_file)
        self.pushbutton_browse.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushbutton_browse.setObjectName("pushbutton_browse")
        self.hortizontal_layout_open_file.addWidget(self.pushbutton_browse)
        self.pushbutton_open = QtWidgets.QPushButton(self.tab_file)
        self.pushbutton_open.setObjectName("pushbutton_open")
        self.hortizontal_layout_open_file.addWidget(self.pushbutton_open)
        self.verticalLayout_4.addLayout(self.hortizontal_layout_open_file)
        self.vertical_layout_recent_files = QtWidgets.QVBoxLayout()
        self.vertical_layout_recent_files.setObjectName("vertical_layout_recent_files")
        self.label_recent = QtWidgets.QLabel(self.tab_file)
        self.label_recent.setObjectName("label_recent")
        self.vertical_layout_recent_files.addWidget(self.label_recent)
        self.list_widget_recent = QtWidgets.QListWidget(self.tab_file)
        self.list_widget_recent.setAlternatingRowColors(True)
        self.list_widget_recent.setObjectName("list_widget_recent")
        self.vertical_layout_recent_files.addWidget(self.list_widget_recent)
        self.verticalLayout_4.addLayout(self.vertical_layout_recent_files)
        self.tab_widget.addTab(self.tab_file, "")
        self.tab_download = QtWidgets.QWidget()
        self.tab_download.setObjectName("tab_download")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_download)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontal_layout_actions = QtWidgets.QHBoxLayout()
        self.horizontal_layout_actions.setObjectName("horizontal_layout_actions")
        self.pushbutton_add = QtWidgets.QPushButton(self.tab_download)
        self.pushbutton_add.setObjectName("pushbutton_add")
        self.horizontal_layout_actions.addWidget(self.pushbutton_add)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_actions.addItem(spacerItem)
        self.pushbutton_remove = QtWidgets.QPushButton(self.tab_download)
        self.pushbutton_remove.setObjectName("pushbutton_remove")
        self.horizontal_layout_actions.addWidget(self.pushbutton_remove)
        self.verticalLayout_6.addLayout(self.horizontal_layout_actions)
        self.vertical_layout_task_list = QtWidgets.QVBoxLayout()
        self.vertical_layout_task_list.setObjectName("vertical_layout_task_list")
        self.label_task_list = QtWidgets.QLabel(self.tab_download)
        self.label_task_list.setObjectName("label_task_list")
        self.vertical_layout_task_list.addWidget(self.label_task_list)
        self.tablewidget_task_list = QtWidgets.QTableWidget(self.tab_download)
        self.tablewidget_task_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidget_task_list.setAlternatingRowColors(True)
        self.tablewidget_task_list.setShowGrid(False)
        self.tablewidget_task_list.setObjectName("tablewidget_task_list")
        self.tablewidget_task_list.setColumnCount(0)
        self.tablewidget_task_list.setRowCount(0)
        self.vertical_layout_task_list.addWidget(self.tablewidget_task_list)
        self.verticalLayout_6.addLayout(self.vertical_layout_task_list)
        self.tab_widget.addTab(self.tab_download, "")
        self.verticalLayout.addWidget(self.tab_widget)
        self.sidebar.setWidget(self.sidebar_content)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.sidebar)
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_file_tab = QtWidgets.QAction(MainWindow)
        self.action_file_tab.setCheckable(True)
        self.action_file_tab.setChecked(True)
        self.action_file_tab.setObjectName("action_file_tab")
        self.action_download_tab = QtWidgets.QAction(MainWindow)
        self.action_download_tab.setCheckable(True)
        self.action_download_tab.setChecked(True)
        self.action_download_tab.setObjectName("action_download_tab")
        self.action_empty = QtWidgets.QAction(MainWindow)
        self.action_empty.setEnabled(False)
        self.action_empty.setObjectName("action_empty")
        self.menu_file.addAction(self.action_quit)
        self.menu_help.addAction(self.action_about)
        self.menu_view.addAction(self.action_file_tab)
        self.menu_view.addAction(self.action_download_tab)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.label_path.setBuddy(self.lineedit_path)
        self.label_recent.setBuddy(self.list_widget_recent)
        self.label_task_list.setBuddy(self.tablewidget_task_list)

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt Demo"))
        self.label_display_panel.setText(_translate("MainWindow", "N/A"))
        self.menu_file.setTitle(_translate("MainWindow", "&File"))
        self.menu_help.setTitle(_translate("MainWindow", "&Help"))
        self.menu_view.setTitle(_translate("MainWindow", "&View"))
        self.sidebar.setWindowTitle(_translate("MainWindow", "Tools"))
        self.label_path.setText(_translate("MainWindow", "&Path"))
        self.pushbutton_browse.setText(_translate("MainWindow", "..."))
        self.pushbutton_open.setText(_translate("MainWindow", "&Open"))
        self.label_recent.setText(_translate("MainWindow", "&Recent"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_file), _translate("MainWindow", "File"))
        self.pushbutton_add.setText(_translate("MainWindow", "&Add..."))
        self.pushbutton_remove.setText(_translate("MainWindow", "&Remove"))
        self.label_task_list.setText(_translate("MainWindow", "&Task List"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_download), _translate("MainWindow", "Download"))
        self.action_quit.setText(_translate("MainWindow", "&Quit"))
        self.action_about.setText(_translate("MainWindow", "&About..."))
        self.action_file_tab.setText(_translate("MainWindow", "&File Tab"))
        self.action_download_tab.setText(_translate("MainWindow", "&Download Tab"))
        self.action_empty.setText(_translate("MainWindow", "(Empty)"))
