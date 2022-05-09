import queue
import random
import threading
import time

import blog_spider


def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = blog_spider.craw(url)
        html_queue.put(html)
        print(threading.currentThread().name, f' craw {url} url_queue_size = {url_queue.qsize()}')
        time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue, fout):
    while True:
        html = html_queue.get()
        results = blog_spider.parse(html)
        for result in results:
            fout.write(str(result) + '\n')
        print(threading.currentThread().name, f' results_size = {len(results)} html_queue_size = {html_queue.qsize()}')
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in blog_spider.urls:
        url_queue.put(url)

    for idx in range(3):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue), name=f'craw{idx}')
        t.start()

    fout = open('02.data.txt', 'w')
    for idx in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue, fout), name=f'craw{idx}')
        t.start()
