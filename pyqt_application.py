# pyqt_application.py


import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from pyqt_application_form import Ui_MainWindow
from CustomizedException import CustomizedException
from DownloadTask import DownloadTask
from InquireUrlDialog import InquireUrlDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, application=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.application = application
        self.file_patterns = [
            ('Text files', ['*.txt']),
            ('Images', ['*.jpg', '*.png', '*.gif', '*.bmp', '*.svg']),
            ('All files', ['*'])
        ]
        self.download_tasks = []
        self.download_task_items = []
        self.display_panel_mode = ''
        self.display_panel_img_path = ''
        self.init_connections()
        self.init_chores()
        self.installEventFilter(self)
        self.reset_display_panel()
        self.update_task_list()

    def init_connections(self):
        self.action_quit.triggered.connect(self.application.quit)
        self.action_about.triggered.connect(self.show_about)
        self.action_file_tab.triggered.connect(self.update_tab)
        self.action_download_tab.triggered.connect(self.update_tab)
        self.pushbutton_browse.clicked.connect(self.browse_file)
        self.pushbutton_open.clicked.connect(self.open_file)
        self.pushbutton_add.clicked.connect(self.add_task)
        self.pushbutton_remove.clicked.connect(self.remove_task)
        self.list_widget_recent.itemClicked.connect(self.fill_item)
        self.list_widget_recent.itemDoubleClicked.connect(self.reopen_item)

    def init_chores(self):
        pass

    def reset_display_panel(self):
        self.display_panel_mode = 'none'
        self.display_panel_img_path = ''
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
                    self.display_panel_mode = 'text'
                    self.label_display_panel.setText(path[path.rfind('/') + len('/'):])
                    self.textedit_display_panel.setText(file.read())
                    self.textedit_display_panel.show()
            except FileNotFoundError as e:
                raise CustomizedException(CustomizedException.describe_file_error(e, path))
        elif pattern == 'Images':
            if not os.path.exists(path):
                raise CustomizedException(
                    CustomizedException.describe_file_error(FileNotFoundError('No such file or directory'), path))
            self.reset_display_panel()
            self.display_panel_mode = 'img'
            self.display_panel_img_path = path
            self.label_display_panel.setAlignment(Qt.AlignCenter)
            self.label_display_panel.setPixmap(
                QPixmap(path).scaled(self.widget_display_panel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
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

    def add_task(self):
        dialog = InquireUrlDialog(self)
        dialog.url_ready.connect(self._add_task)
        dialog.show()

    def _add_task(self, url):
        if url:
            self.download_tasks.append(DownloadTask(url))
        self.update_task_list()

    def remove_task(self):
        task_to_remove = self.tablewidget_task_list.currentRow()
        del self.download_tasks[task_to_remove]
        self.update_task_list()

    def update_task_list(self):
        row_count = len(self.download_tasks)
        self.tablewidget_task_list.clear()
        self.download_task_items.clear()
        self.tablewidget_task_list.setColumnCount(2)
        self.tablewidget_task_list.setHorizontalHeaderLabels(('File', 'Status'))
        self.tablewidget_task_list.setRowCount(row_count)
        for i in range(row_count):
            download_task = self.download_tasks[i]
            self.download_task_items.append(download_task.target)
            self.download_task_items.append(download_task.status)
            self.tablewidget_task_list.setItem(i, 0, QTableWidgetItem(self.download_task_items[-2]))
            self.tablewidget_task_list.setItem(i, 1, QTableWidgetItem(self.download_task_items[-1]))

    def fill_item(self, item):
        self.lineedit_path.setText(item.text())

    def reopen_item(self, item):
        self.fill_item(item)
        self.open_file()

    def eventFilter(self, obj, event):
        # FIXME: The event filter cannot receive any event other than those in which obj == self (MainWindow)
        # print('OBJ = {}, EVENT.TYPE = {}'.format(obj, event.type()))
        if obj in (self.widget_display_panel, self.label_display_panel, self.textedit_display_panel) \
                and event.type() == QEvent.MouseButtonDblClick:
            print('Object confirmed!')
            if self.widget_display_panel.isFullScreen():
                print('Going back')
                self.widget_display_panel.setWindowFlags(Qt.SubWindow)
                self.widget_display_panel.setGeometry(self.rec0)
                self.widget_display_panel.showNormal()
            else:
                print('Going FullScreen!')
                self.widget_display_panel.setWindowFlags(Qt.Dialog)
                self.widget_display_panel.showFullScreen()
            return True
        # elif obj == self.widget_display_panel and event.type() == QEvent.Resize:
        elif event.type() == QEvent.Resize:
            print('Resize event captured!')
            if self.display_panel_mode == 'img':
                # original_pixmap = self.label_display_panel.pixmap()
                original_pixmap = QPixmap(self.display_panel_img_path)
                print('Got original!')
                new_size = self.widget_display_panel.size()
                print('Got size!')
                new_pixmap = original_pixmap.scaled(new_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                print('Got new!')
                self.label_display_panel.setPixmap(new_pixmap)
                print('Set new!')
                # self.label_display_panel.setPixmap(
                #     self.label_display_panel.pixmap().scaled(self.widget_display_panel.size()),
                #     Qt.KeepAspectRatio,
                #     Qt.SmoothTransformation
                # )
            return True
        return False


def main():
    application = QApplication(sys.argv)
    main_window = MainWindow(application=application)
    main_window.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
