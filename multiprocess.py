import logging
from functools import partial
from multiprocessing import Pool
from download import get_links, setup_download_dir,\
                     download_link, CLIENT_ID

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

PROCESSES = 4

if __name__ == '__main__':
    download_dir = setup_download_dir('images')
    download = partial(download_link, download_dir)
    links = get_links(CLIENT_ID)
    with Pool(PROCESSES) as p:
        p.map(download, links)
