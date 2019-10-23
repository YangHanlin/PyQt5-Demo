default_url = 'https://hanlinyang.coding.me/academic-city/greetings.txt'

class DownloadTask:
    def __init__(self, url=None):
        self.url = url if url is not None else default_url

    def start(self):
        print('N/A for now')

    def stop(self):
        print('N/A for now')

    def progress(self):
        return 0.0
