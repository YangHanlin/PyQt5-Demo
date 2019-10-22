from PyQt5.QtCore import QObject

class MainWindowService(QObject):
    def __init__(self, mainwindow, application):
        self.mainwindow = mainwindow
        self.application = application
