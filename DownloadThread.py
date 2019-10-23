import requests
from PyQt5.QtCore import *

from CustomizedException import CustomizedException


class DownloadThread(QThread):
    completed = pyqtSignal()
    aborted = pyqtSignal(bool)
    failed = pyqtSignal(str)
    progressed = pyqtSignal(float)

    def __init__(self, url, target):
        super(DownloadThread, self).__init__()
        self.url = url
        self.target = target
        self.to_abort = False

    def run(self):
        try:
            with open(self.target, 'wb') as target_file:
                response = requests.get(self.url, stream=True)
                response.raise_for_status()
                total_size = int(response.headers['Content-Length'])
                chunk_size = 4 * 1024
                downloaded_size = 0
                # Response content is divided into chunks to avoid excessive use of memory
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if self.to_abort:
                        raise CustomizedException('abort')
                    if chunk:
                        target_file.write(chunk)
                        downloaded_size += chunk_size
                        self.progressed.emit(downloaded_size / total_size)
        except requests.exceptions.HTTPError as e:
            err_str = e.args[0]
            colon_index = err_str.find(':')
            if colon_index != -1:
                err_str = err_str[:colon_index]
            self.failed.emit(err_str)
        except CustomizedException as e:
            if e.description == 'abort':
                self.aborted.emit(True)
            else:
                raise
        except Exception as e:
            self._remove_target()
            print(type(e), e.args)
            self.failed.emit('')
        else:
            self.completed.emit()
