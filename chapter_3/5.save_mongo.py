# MongoDBに保存する

import lxml.html
from pymongo import MongoClient

# HTMLファイルを読み込み、getroot()でHtmlElementオブジェクトを取得する
tree = lxml.html.parse('../index.html')
html = tree.getroot()

client = MongoClient('localhost', 27017)
db = client.scraping  # scrapingデータベースを取得
collection = db.links  # linksコレクションを取得する

# このスクリプトを何度実行しても同じ結果になるようにするため、コレクションのドキュメントを全て削除する
collection.delete_many({})

# cssselect()でaタグの要素を取得し、それぞれの要素に対して処理を行う
for a in html.cssselect('a'):
    collection.insert_one({
        'url': a.get('href'),
        'title': a.text,
    })

# collectionの全てのドキュメントを_idの順にソートして取得する。
for link in collection.find().sort('_id'):
    print(link['_id'], link['url'], link['title'])