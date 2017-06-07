import logging
from queue import Queue
from download import get_links, setup_download_dir,\
                     DownloadWorker, CLIENT_ID


logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

THREADS = 4

if __name__ == '__main__':
    download_dir = setup_download_dir('images')
    queue = Queue()
    for link in get_links(CLIENT_ID):
        queue.put((download_dir, link))
    for i in range(THREADS):
        t = DownloadWorker(queue)
        t.daemon = True
        t.start()
    queue.join()
