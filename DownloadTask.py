import os

from PyQt5.QtCore import *

from DownloadThread import DownloadThread

default_url = 'https://hanlinyang.coding.me/academy-city/greetings.txt'
target_prefix = ''


class DownloadTask(QObject):
    status_changed = pyqtSignal(str)
    aborted = pyqtSignal()

    def __init__(self, url=None, target=None):
        super().__init__()
        self.url = url if url is not None else default_url
        self.target = target_prefix + self._available_target_for(url)
        self.status = 'Waiting'
        self.thread_ = None
        self.stopping = False

    def __str__(self):
        return 'Download task [URL = \'{}\', target = \'{}\', Status = \'{}\']'.format(self.url, self.target, self.status)

    def start(self):
        if self.stopping:
            return
        self.thread_ = DownloadThread(self.url, self.target)
        self.thread_.completed.connect(self._on_completed)
        self.thread_.aborted.connect(self._on_aborted)
        self.thread_.failed.connect(self._on_failed)
        self.thread_.progressed.connect(self._on_progressed)
        self.thread_.start()

    def stop(self):
        print('Going to stop {}'.format(self.target))
        if self.stopping:
            return
        self.stopping = True
        if self.thread_.isRunning():
            print('Running...')
            self.thread_.to_abort = True
        else:
            print('Not Running...')
            self._on_aborted(False)

    def _on_completed(self):
        self._change_status('Completed')

    def _on_aborted(self, need_removal):
        if need_removal:
            self._remove_target()
        self._change_status('Aborted')
        self.stopping = False
        self.aborted.emit()

    def _on_failed(self, err_str):
        if err_str:
            self._change_status('Failed ({})'.format(err_str))
        else:
            self._change_status('Failed')
        self._remove_target()

    def _on_progressed(self, progress):
        self._change_status('{}%'.format(progress * 100))

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

    def _remove_target(self):
        if os.path.exists(self.target):
            os.remove(self.target)
