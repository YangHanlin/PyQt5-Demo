import os
import requests

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
        # FIXME: The download process will block any other action in the program.
        self._change_status('Progressing')
        try:
            with open(self.target, 'wb') as target_file:
                response = requests.get(self.url, stream=True)
                response.raise_for_status()
                total_size = int(response.headers['Content-Length'])
                chunk_size = 4 * 1024
                downloaded_size = 0
                # Response content is divided into chunks to avoid excessive use of memory
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        target_file.write(chunk)
                        downloaded_size += chunk_size
                        self._change_status('{}%'.format(downloaded_size / total_size * 100))
        except requests.exceptions.HTTPError as e:
            err_str = e.args[0]
            colon_index = err_str.find(':')
            if colon_index != -1:
                err_str = err_str[:colon_index]
            self._remove_target()
            self._change_status('Failed ({})'.format(err_str))
        except Exception as e:
            self._remove_target()
            print(type(e), e.args)
            self._change_status('Failed')
        else:
            self._change_status('Completed')

    def stop(self):
        # TODO Some improvement?
        self._change_status('Aborted')

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
        print('status = {}'.format(status))
        self.status_changed.emit(status)

    def _remove_target(self):
        if os.path.exists(self.target):
            os.remove(self.target)
