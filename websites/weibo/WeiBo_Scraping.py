import requests
import pandas as pd


class WeiBo:
    def __init__(self):
        self.count = 0

    def write_file(self, item):
        df = pd.DataFrame(item).T
        df.to_excel("weibo.xlsx")

    def get_info(self):
        comment = {}
        for i in range(15):
            url = 'https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp=0&page={}'.format(i)
            headers = {
                'Cookie':'_T_WM=6f0ac6371517e3784eaff9a86b687a6b; MLOGIN=0; WEIBOCN_FROM=1110006030;\
                 M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803%26uicode%3D20000174',
                'Host': 'm.weibo.cn',
                'referer': 'https://m.weibo.cn/',
                'iphone': 'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; \
                 MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko)\
                 Version/4.0 Mobile Safari/533.1',
                'MWeibo-Pwa': '1',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                 Chrome/68.0.3440.106 Safari/537.36'
            }
            res = requests.get(url, headers=headers).json()
            post = res['data']['cards']
            for index in range(len(post)):
                if 'mblog' in post[index].keys():
                    comment[post[index]['mblog']['user']['screen_name']] = post[index]['mblog']
                    self.count += 1
                print('已爬取：', self.count, '条。')
        self.write_file(comment)


if __name__ == '__main__':
    wb = WeiBo()
    wb.get_info()

