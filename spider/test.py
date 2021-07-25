import concurrent
import os
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
def abc():
    while True:
        print('abc')
def cdf():
    while True:
        print('cdf')

def www():
    while True:
        print('qqq')
def aaa():
    while True:
        print('aaaaa')

def rrr():
    while True:
        print('rrrr')

def ab():
    print('66666')

def download_all_images():
    # 获取每一个详情妹纸
    # works = len(list_page_urls)
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as exector:
        exector.submit(abc)
        exector.submit(cdf)
        exector.submit(www)
        exector.submit(aaa)
        exector.submit(ab)

if __name__ == '__main__':
    download_all_images()

