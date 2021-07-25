import re
import random
import requests
import time
from .models import PttTitle

def sp_ptt():
    pool = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.125",
    ]
    pre_total = []
    total = []
    header = {'user-agent': random.choice(pool), }
    r = requests.get('https://www.ptt.cc/bbs/C_Chat/index.html', headers=header).text
    pat_link = '<a href="(/bbs/C_Chat/M..*?.html)"'
    link = re.compile(pat_link, re.S).findall(r)  # 文章連結
    # print(len(link))
    pat_title = '(\[.*\]*?)</a>'
    # pat_title='<a href="/bbs/C_Chat/M.1615614370.A.284.html">(.*\[.*\].*?)</a>'
    title = re.compile(pat_title, re.M).findall(r)  # 文章標題 re.M 多行匹配 省略\n\t
    # for i in title:
    #     print(i + '\n')
    print(title)
    for i in range(len(link)):
        parse_link = 'https://www.ptt.cc/' + link[i] + '\n'
        # parse_title = title[i]+'\n'
        # total.append(parse_title)
        pre_total.append(parse_link)
    for _ in range(1):
        pat_oldpage = '<a class="btn wide" href="(/bbs/C_Chat/.*?\.html)">'
        oldpage = re.compile(pat_oldpage, re.S).findall(r)  # 上一頁
        # print(oldpage[1])
        r = requests.get('https://www.ptt.cc/' + oldpage[1], headers=header).text
        pat_link = '<a href="(/bbs/C_Chat/M..*?.html)"'
        link2 = re.compile(pat_link, re.S).findall(r)  # 文章連結
        # print(len(link))
        pat_title = '(\[.*\]*?)</a>'
        title2 = re.compile(pat_title, re.M).findall(r)  # 文章標題 re.M 多行匹配 省略\n\t
        for i in range(len(link2)):
            try:
                # print(link2[i])
                parse_link = 'https://www.ptt.cc/' + link2[i]
                parse_title = title2[i]
                print('====loop====')
                if not PttTitle.objects.filter(url=parse_link):
                    PttTitle.objects.create(url=parse_link, title=parse_title, type='c_chat')  # 寫入DB
                else:
                    continue
            except:
                total.append('error')
        pat_oldpage = '<a class="btn wide" href="(/bbs/C_Chat/.*?\.html)">'
        oldpage = re.compile(pat_oldpage, re.S).findall(r)  # 上一頁
        time.sleep(2)
