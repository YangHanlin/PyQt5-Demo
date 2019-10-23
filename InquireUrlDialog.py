# InquireUrlDialog.py


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from InquireUrlDialog_form import Ui_Dialog


class InquireUrlDialog(QDialog, Ui_Dialog):
    url_ready = pyqtSignal(str)

    def __init__(self, parent=None):
        super(InquireUrlDialog, self).__init__(parent)
        self.setupUi(self)
        self.button_box.accepted.connect(self.success)
        self.button_box.rejected.connect(self.failure)

    def success(self):
        self.url_ready.emit(self.lineedit_url.text())
        self.accept()

    def failure(self):
        self.url_ready.emit('')
