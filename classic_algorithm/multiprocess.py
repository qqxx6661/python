# -*- coding: utf-8 -*-
import multiprocessing
import time

def crawl_status_on(break_time):
    while(1):
        print('on')
        time.sleep(break_time)

def crawl_status_off(break_time):
    while(1):
        print('off')
        time.sleep(break_time)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=crawl_status_on, args=(1,))
    p1.start()
    p2 = multiprocessing.Process(target=crawl_status_off, args=(1,))
    p2.start()