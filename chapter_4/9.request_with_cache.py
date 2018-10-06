# CacheControlを使ってキャッシュを処理する

import requests
from cachecontrol import CacheControl

session = requests.Session()

# sessionをラップしたcached_sessionを作る
cached_session = CacheControl(session)

# １回目はキャッシュがないのでサーバーから取得しキャッシュする
response = cached_session.get('https://docs.python.org/3/')
print(response.from_cache)  # False

# ２回目はETagとLast-Modifiedの値を使って更新されているかを確認する。
# 更新されていない場合のコンテンツはキャッシュから取得するので高速に処理できる
response = cached_session.get('https://docs.python.org/3/')
print(response.from_cache)  # True
