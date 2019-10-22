from PyQt5.QtWidgets import QMessageBox

class CustomizedException(Exception):
    def __init__(self, description):
        self.description = description

    def pop_up(self, parent):
        QMessageBox.critical(
            parent,
            'Error',
            self.description
        )

    def describe_file_error(exception, path):
        return 'Error in opening file \'{}\':\n{}'.format(path, exception.args[1])
