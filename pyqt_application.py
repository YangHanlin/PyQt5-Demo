# pyqt_application.py


import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from pyqt_application_form import Ui_MainWindow
from CustomizedException import CustomizedException


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, application=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.application = application
        self.not_ready_buttons = [
            self.pushbutton_add,
            self.pushbutton_remove
        ]
        self.not_ready_actions = [
            # self.action_download_tab,
            # self.action_file_tab
        ]
        self.file_patterns = [
            ('Text files', ['*.txt']),
            ('Images', ['*.jpg', '*.png', '*.gif', '*.bmp', '*.svg']),
            ('All files', ['*'])
        ]
        self.init_connections()
        self.init_chores()
        self.installEventFilter(self)
        self.reset_display_panel()

    def init_connections(self):
        self.action_quit.triggered.connect(self.application.quit)
        self.action_about.triggered.connect(self.show_about)
        self.action_file_tab.triggered.connect(self.update_tab)
        self.action_download_tab.triggered.connect(self.update_tab)
        self.pushbutton_browse.clicked.connect(self.browse_file)
        self.pushbutton_open.clicked.connect(self.open_file)
        for button in self.not_ready_buttons:
            button.clicked.connect(self.work_in_progress)
        for action in self.not_ready_actions:
            action.triggered.connect(self.work_in_progress)

    def init_chores(self):
        pass

    def reset_display_panel(self):
        self.label_display_panel.setText('')
        self.label_display_panel.setAlignment(Qt.AlignLeft)
        self.textedit_display_panel.clear()
        self.textedit_display_panel.hide()

    def work_in_progress(self):
        print('This feature is not implemented yet; please wait.')

    def browse_file(self):
        path = QFileDialog.getOpenFileName(
            self,
            'Browse and select a file',
            '',
            ';;'.join(['{} ({})'.format(pattern[0], ' '.join(pattern[1])) for pattern in self.file_patterns])
        )[0]
        if path:
            self.lineedit_path.setText(path)

    def open_file(self):
        path = self.lineedit_path.text()
        if path:
            try:
                self._open_file(path)
            except CustomizedException as e:
                e.pop_up(self)
            else:
                if not self.list_widget_recent.findItems(path, Qt.MatchExactly):
                    self.list_widget_recent.addItem(path)
                    # TODO: Click on list to re-open previously viewed files

    def _open_file(self, path):
        pattern = self.pattern_of(path)
        if pattern == 'Text files' or pattern == 'All files':
            try:
                with open(path) as file:
                    self.reset_display_panel()
                    self.label_display_panel.setText(path[path.rfind('/') + len('/'):])
                    self.textedit_display_panel.setText(file.read())
                    self.textedit_display_panel.show()
            except FileNotFoundError as e:
                raise CustomizedException(CustomizedException.describe_file_error(e, path))
        elif pattern == 'Images':
            if not os.path.exists(path):
                raise CustomizedException(CustomizedException.describe_file_error(FileNotFoundError('No such file or directory'), path))
            self.reset_display_panel()
            self.label_display_panel.setAlignment(Qt.AlignCenter)
            self.label_display_panel.setPixmap(QPixmap(path).scaled(self.widget_display_panel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            raise CustomizedException('Internal Error:\nInvalid file pattern \'{}\''.format(pattern))

    def pattern_of(self, path):
        for pattern in self.file_patterns:
            for suffix in pattern[1]:
                if path.endswith(suffix[suffix.rfind('*.') + len('*.'):]):
                    return pattern[0]

    def show_about(self):
        QMessageBox.about(
            self,
            'About',
            'Copyright (C) 2019 Yang Hanlin.\n'
            'Grade 2018, School of Software, Hefei University of Technology'
        )

    def update_tab(self):
        # TODO: Restore current tab
        self.tab_widget.clear()
        if self.action_file_tab.isChecked():
            self.tab_widget.addTab(self.tab_file, 'File')
        if self.action_download_tab.isChecked():
            self.tab_widget.addTab(self.tab_download, 'Download')

    def eventFilter(self, obj, event):
        # print('OBJ = {}, EVENT.TYPE = {}'.format(obj, event.type()))
        if event.type() == QEvent.MouseButtonDblClick:
            print('Captured doubleclick: obj = {}'.format(obj))
            if obj in (self.widget_display_panel, self.label_display_panel, self.textedit_display_panel):
                print('Object confirmed!')
                if self.widget_display_panel.isFullScreen():
                    print('Going back')
                    self.widget_display_panel.setWindowFlags(Qt.SubWindow)
                    self.widget_display_panel.setGeometry(self.rec0)
                    self.widget_display_panel.showNormal()
                else:
                    print('Going FullScreen!')
                    self.widget_display_panel.setWindowFlags(Qt.Window)
                    self.widget_display_panel.showFullScreen()
                return True
        return False


def main():
    application = QApplication(sys.argv)
    main_window = MainWindow(application=application)
    main_window.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
