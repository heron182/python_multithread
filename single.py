import logging
from download import download_link, get_links, setup_download_dir,\
                     CLIENT_ID


logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    download_dir = setup_download_dir('images')
    for link in get_links(CLIENT_ID):
        download_link(download_dir, link)
