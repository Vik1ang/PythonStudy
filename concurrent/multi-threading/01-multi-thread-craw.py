import threading

import blog_spider
import time


def single_thread():
    print('single thread begin')
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print('single thread end')


def multi_thread():
    print('multi thread begin')
    threads = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.craw, args=(url,))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print('multi thread end')


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()

    print('single cost: ', end - start, ' seconds')

    start = time.time()
    multi_thread()
    end = time.time()

    print('multi cost: ', end - start, ' seconds')
