# 一覧ページからURLの一覧を抜き出す(2)

import requests
import lxml.html

response = requests.get('https://gihyo.jp/dp')

root = lxml.html.fromstring(response.content)

# 全てのリンクを絶対URLに変換する
root.make_links_absolute(response.url)

for a in root.cssselect('a[itemprop="url"]'):
    url = a.get('href')
    print(url)
