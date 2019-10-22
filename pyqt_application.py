# pyqt_application.py


import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from pyqt_application_form import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, application=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.application = application
        self.not_ready_buttons = [
            self.pushbutton_add,
            self.pushbutton_browse,
            self.pushbutton_open,
            self.pushbutton_remove
        ]
        self.not_ready_actions = [
            self.action_about,
            self.action_download_tab,
            self.action_file_tab
        ]
        self.init_connections()
        self.init_chores()

    def init_connections(self):
        self.action_quit.triggered.connect(self.application.quit)
        for button in self.not_ready_buttons:
            button.clicked.connect(self.work_in_progress)
        for action in self.not_ready_actions:
            action.triggered.connect(self.work_in_progress)

    def init_chores(self):
        pass

    def work_in_progress(self):
        print('This feature is not implemented yet; please wait.')


def main():
    application = QApplication(sys.argv)
    main_window = MainWindow(application=application)
    main_window.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
