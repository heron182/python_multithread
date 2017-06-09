import json
import os
import logging
import threading
from pathlib import Path
from urllib.request import Request, urlopen

logger = logging.getLogger(__name__)

CLIENT_ID = open('secret').readline()[:-1]


class DownloadWorker(threading.Thread):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        logger.info('Starting worker %s ' %
                    threading.currentThread().getName())
        while True:
            download_dir, link = self.queue.get()
            download_link(download_dir, link)
            self.queue.task_done()


def get_links(client_id):
    headers = {'Authorization': 'Client-ID {}'.format(client_id)}
    req = Request('https://api.imgur.com/3/gallery/hot/1',
                  headers=headers, method='GET')
    with urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    return map(lambda item: item['link'],
               filter(lambda x: x['link'].endswith('.jpg'),
               data['data']))


def download_link(directory, link):
    logger.info('Downloading %s' % link)
    download_path = directory / os.path.basename(link)
    with urlopen(link) as img, download_path.open('wb') as f:
        f.write(img.read())


def setup_download_dir(dir_name):
    logger.info('Setting up directory %s' % dir_name)
    download_dir = Path(dir_name)
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir
