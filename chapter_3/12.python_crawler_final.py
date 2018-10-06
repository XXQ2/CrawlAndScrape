# 最終的なクローラー

import time
import re
import requests
import lxml.html
from pymongo import MongoClient


def main():
    # localhostのmongoDBに接続
    client = MongoClient('localhost', 27017)
    # scrapingデータベースのebookコレクションを得る
    collection = client.scraping.ebook
    # データを一意に識別するキーを格納するフィールドにユニークなインデックスを作成する
    collection.create_index('key', unique=True)

    response = requests.get('https://gihyo.jp/dp')

    # 商品の詳細ページのURLを取得
    urls = scrape_list_page(response)

    for url in urls:
        key = extract_key(url)
        ebook = collection.find_one({'key': key})

        # mongoDBに存在しない場合だけ、詳細ページをクロールする
        if not ebook:
            time.sleep(1)
            response = requests.get(url)
            # 詳細ページのresponseからタイトルなどの情報を取得
            ebook = scrape_detail_page(response)
            # DBへ情報を登録する
            collection.insert_one(ebook)

        print(ebook)


def scrape_list_page(response):
    """
    一覧ページから詳細ページのURLを取得。
    """
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('#listBook a[itemprop="url"]'):
        url = a.get('href')
        yield url


def scrape_detail_page(response):
    """
    詳細ページのResponseから電子書籍の情報を取得。
    辞書形式でreturn
    """
    root = lxml.html.fromstring(response.content)
    ebook = {
        'url': response.url,
        'key': extract_key(response.url),
        'title': root.cssselect('#bookTitle')[0].text_content(),
        'price': root.cssselect('.buy')[0].text.strip(),
        'content': [normalize_space(h3.text_content()) for h3 in root.cssselect('#content > h3')],
    }
    return ebook


def extract_key(url):
    """
    URLからキー（URL末尾のISBN）を抜き出す
    """
    m = re.search(r'/([^/]+)$', url)
    return m.group(1)


def normalize_space(text):
    """
    連続する空白を1つのスペースに置き換え、前後の空白は削除した新しい文字列を取得する
    """
    return re.sub(r'\s+', ' ', text).strip()


if __name__ == "__main__":
    main()