# pyqt_application.py


import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from pyqt_application_form import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.not_ready_buttons = [
            # empty
        ]
        self.not_ready_actions = [
            self.action_quit,
            self.action_about
        ]
        self.init_connections()
        self.init_chores()

    def init_connections(self):
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
    main_window = MainWindow()
    main_window.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
