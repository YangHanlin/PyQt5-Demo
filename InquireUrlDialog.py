# InquireUrlDialog.py


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from InquireUrlDialog_form import Ui_Dialog


class InquireUrlDialog(QDialog, Ui_Dialog):
    url_ready = pyqtSignal()

    def __init__(self, parent=None):
        super(InquireUrlDialog, self).__init__(parent)
        self.setupUi(self)
        self.button_box.accepted.connect(self.on_ok_clicked)
        self.button_box.rejected.connect(self.on_cancel_clicked)
        self.closed.connect(self.url_ready)
        self.result_url = ''

    def on_ok_clicked(self):
        self.result_url = self.lineedit_url.text()
        self.close()

    def on_cancel_clicked(self):
        self.close()
