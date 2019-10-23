import os

from PyQt5.QtCore import *

default_url = 'https://hanlinyang.coding.me/academy-city/greetings.txt'
target_prefix = ''


class DownloadTask(QObject):
    status_changed = pyqtSignal(str)

    def __init__(self, url=None, target=None):
        super().__init__()
        self.url = url if url is not None else default_url
        self.target = target_prefix + self._available_target_for(url)
        self.status = 'Waiting'

    def __str__(self):
        return 'Download task [URL = \'{}\', target = \'{}\', Status = \'{}\']'.format(self.url, self.target, self.status)

    def start(self):
        # TODO
        self._change_status('Completed')
        print('N/A for now')

    def stop(self):
        # TODO
        self._change_status('Aborted')
        print('N/A for now')

    def progress(self):
        return 0.0

    def _available_target_for(self, url):
        res = url[url.rfind('/') + len('/'):]
        separator_pos = res.rfind('.')
        if separator_pos != -1:
            filename, extension = res[:separator_pos], res[separator_pos + len('.'):]
        else:
            filename, extension = res, ''
        n = 0
        while os.path.exists(res):
            n += 1
            res = self._make_res(filename, extension, n)
        return res

    def _make_res(self, filename, extension, n):
        if n:
            return filename + ' (' + str(n) + ').' + extension
        return filename + '.' + extension

    def _change_status(self, status):
        self.status = status
        self.status_changed.emit(status)
