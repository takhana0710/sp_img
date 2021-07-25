import requests
import random
import urllib.parse
import time
from datetime import datetime
from .models import PixivArt
session = requests.session()

pool = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.125",
]
header = {'user-agent': random.choice(pool),'referer':'https://www.pixiv.net/'}
cookie = {'PHPSESSID': ""}
img = ''
webhook_url = ''


def TokenStatus():  # 確定是否需要換token
    r = session.get("https://www.pixiv.net/touch/ajax/user/self/status?lang=zh_tw", headers=header, cookies=cookie)
    res = r.json()
    token_life = res['body']['user_status']['is_logged_in']
    print(token_life)


def TagSearch():  # 標籤搜尋
    url='https://i.pximg.net/img-original/img/2021/02/13/16/35/16/87734098_p0.jpg'
    url='https://www.pixiv.net/ajax/illust/89220807'
    r=requests.get(url,headers=header, cookies=cookie)
    print(r.json())
    # data = {'payload_json': '123'}
    # requests.post(webhook_url, json=data, headers=header, files={'8.jpg': r.content})

def Save():  # 蒐集圖片 # 研究結果:抓網路位址圖片最為穩定
    embed = {
        "description": "text in embed",
        "title": "embed title",
        "image": {'url': 'https://i.pximg.net/img-original/img/2021/04/09/20/21/49/89038959_p0.jpg'},
    }
    # data = {'content':'sdfsdfsdfs', "embeds": [embed]}
    # im=Image.open("8.jpg")
    with open('8.jpg', 'rb') as f:
        file_data = f.read()
    # file_data = base64.b64encode(file_data).decode()
    data = {'payload_json': '123'}
    r = requests.post(webhook_url, json=data, headers=header, files={'8.jpg': file_data})
    print(r.status_code)
    print(r.text)
    pass
def query():
    urlcode=urllib.parse.quote('Rice Shower',encoding=('utf-8'))
    search={'word':'Rice Shower','lang':'zh_tw'}
    r = session.get("https://www.pixiv.net/ajax/search/artworks/%s"%urlcode, headers=header, cookies=cookie,params=search)
    res = r.json()
    print(res)
    # token_life = res['body']['user_status']['is_logged_in']
    # print(token_life)
def sp_pixiv():
    taglist=['ウマ娘','ライスシャワー(ウマ娘)','ミホノブルボン(ウマ娘)','ナイスネイチャ(ウマ娘)','トウカイテイオー(ウマ娘)','エアグルーヴ(ウマ娘)','咲戀(公主連結)']
    # taglist=['トウカイテイオー(ウマ娘)']
    for i in taglist:
        url_code = urllib.parse.quote(i, encoding=('utf-8')) # 標籤轉code
        for page in range(2): #每天爬兩頁
            search_params={'word':i,'lang':'zh_tw','p':page+1}
            r = session.get("https://www.pixiv.net/ajax/search/artworks/%s" % url_code, headers=header, cookies=cookie,params=search_params).json()
            print(r['body']['illustManga'])
            for aid in range(len(r['body']['illustManga']['data'])):# 一頁的作品蝶帶
                time.sleep(2)
                # print(aid)
                # print(r['body']['illustManga']['data'][aid])
                artist_id=r['body']['illustManga']['data'][aid]['id'] # 創作者id
                title=r['body']['illustManga']['data'][aid]['title'] # 創作者id
                userName=r['body']['illustManga']['data'][aid]['userName'] # 創作者id
                artUrl='https://www.pixiv.net/ajax/illust/%s'%artist_id
                if PixivArt.objects.filter(artUrl=artUrl):
                    continue
                artwork= session.get(artUrl, headers=header,cookies=cookie).json() #  取得作品集
                time.sleep(2)
                imgUrl=artwork['body']['urls']['original']
                artUrl='https://www.pixiv.net/artworks/%s'%artist_id
                cdate=datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                PixivArt.objects.create(title=title,userName=userName,artUrl=artUrl,imgUrl=imgUrl,tag=i,cdate=cdate)

def sendDC(info):
    res = requests.get(info['img'], headers=header, cookies=cookie).content
    time.sleep(2)
    requests.post(webhook_url, json={'content':info['content']}, headers=header)  # 傳送DC
    data = {'payload_json': '123'}
    requests.post(webhook_url, json=data, headers=header, files={'img.jpg': res}) # 傳送DC


if __name__ == '__main__':
    # Save()
    # TagSearch()
    # query()
    sp_pixiv()