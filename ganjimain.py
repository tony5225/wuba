from multiprocessing import Pool
from channel_extract import linkurl
from get_parsing import get_links_from
def get_alllinks(channel):
    for i in range(1,50):
        get_links_from(channel,i)

if __name__ == '__main__':
    pool = Pool()
    # pool = Pool(processes=6)
    pool.map(get_alllinks,linkurl)
