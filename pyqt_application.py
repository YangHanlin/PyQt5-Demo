# pyqt_application.py


import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

from pyqt_application_form import Ui_MainWindow


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
            self.action_about,
            self.action_download_tab,
            self.action_file_tab
        ]
        self.file_patterns = [
            ('Text files', ['*.txt']),
            ('Images', ['*.jpg', '*.png', '*.gif', '*.bmp', '*.svg']),
            ('All files', ['*'])
        ]
        self.init_connections()
        self.init_chores()

    def init_connections(self):
        self.action_quit.triggered.connect(self.application.quit)
        self.pushbutton_browse.clicked.connect(self.browse_file)
        self.pushbutton_open.clicked.connect(self.open_file)
        for button in self.not_ready_buttons:
            button.clicked.connect(self.work_in_progress)
        for action in self.not_ready_actions:
            action.triggered.connect(self.work_in_progress)

    def init_chores(self):
        pass

    def work_in_progress(self):
        print('This feature is not implemented yet; please wait.')

    def browse_file(self):
        self.lineedit_path.setText(QFileDialog.getOpenFileName(
            self,
            'Browse and select a file',
            '',
            ';;'.join(['{} ({})'.format(pattern[0], ' '.join(pattern[1])) for pattern in self.file_patterns])
        )[0])

    def open_file(self):
        path = self.lineedit_path.text()
        if path:
            try:
                
                with open(path) as file:
                    pass
            except FileNotFoundError as e:
                QMessageBox.critical(
                    self,
                    'Error',
                    'Error in opening file \'{}\':\n{}'.format(path, e.args[1])
                )


def main():
    application = QApplication(sys.argv)
    main_window = MainWindow(application=application)
    main_window.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
