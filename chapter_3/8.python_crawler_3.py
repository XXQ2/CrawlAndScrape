# 一覧ページからURLの一覧を抜き出す(3)

import requests
import lxml.html


def main():
    """
    クローラーのメインの処理。
    """
    response = requests.get('https://gihyo.jp/dp')
    urls = scrape_list_page(response)

    # ジェネレーターイテレーターはlistなどと同様に繰り返し可能。
    for url in urls:
        print(url)


def scrape_list_page(response):
    """
    一覧ページのResponseから詳細ぺーじのURLを抜き出すジェネレータ関数。
    """
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)

    for a in root.cssselect('#listBook a[itemprop="url"]'):
        url = a.get('href')

        # yield文でジェネレーターイテレーターの要素を返す。
        yield url


if __name__ == '__main__':
    main()