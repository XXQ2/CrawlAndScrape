# ==Pythonによるスクレイピング==

import re
import sqlite3
from urllib.request import urlopen
from html import unescape
from contextlib import closing


def main():
    """
    メインの処理。fetch(),scrape(),save()の３つの関数を呼び出す
    """

    html = fetch('http://sample.scraping-book.com/dp')
    books = scrape(html)
    save('books.db', books)


def fetch(url):
    """
    引数urlで与えられたURLのWebページを取得する
    WebページのエンコーディングはContent-Typeから取得する
    :return: str型のHTML
    """

    f = urlopen(url)

    # HTTPヘッダーからエンコーディングを取得する(明示されていない場合はutf-8)
    encoding = f.info().get_content_charset(failobj="utf-8")

    html = f.read().decode(encoding)

    return html


def scrape(html):
    """
    引数htmlで与えられたHTMLから正規表現を使用し書籍の情報を抽出する
    :param html:
    :return: 書籍(dict)のリスト
    """
    books = []

    for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html, re.DOTALL):
        url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html).group(1)
        url = 'https://gihyo.jp' + url

        title = re.search(r'<p itemprop="name".*?</p>', partial_html).group(0)
        title = re.sub(r'<.*?>', '', title)
        title = unescape(title)

        books.append({'url': url, 'title': title})

    return books


def save(db_path, books):
    """
    引数booksで与えられた書籍のリストをDBに保存する
    """
    with closing(sqlite3.connect(db_path)) as conn:
        c = conn.cursor()

        c.execute('DROP TABLE IF EXISTS books')

        c.execute('''
            CREATE TABLE books(
                title text,
                url text
            )
        ''')

        c.executemany('INSERT INTO books VALUES (:title, :url)', books)

        conn.commit()


# Pythonコマンドで実行された時にmain()関数を呼び出す。
# これはモジュールとして他のファイルからインポートされた時に
#  main()関数が実行されないようにするための、Pythonにおける一般的なイディオム。
if __name__ == '__main__':
    main()


# 最後にターミナルで確認してみる
# $ sqlite3 books.db 'select * from books'
