# YouTubeの動画を検索する

import os
from googleapiclient.discovery import build

# 環境変数からAPIキーを取得
YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']

# YouTubeのAPIクライアントを組み立てる。build()関数の第一引数にはAPI名を、
# 第二引数にはAPIのバージョンを指定し、キーワード引数developerKeyでAPIキーを指定する
# この関数は、内部的にhttps://www.googleapis.com/discovery/v1/apis/youtube/v3/rest という
# URLにアクセスし、APIのリソースやメソッドの情報を取得する。
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# キーワード引数で引数を指定し、search.listメソッドを呼び出す。
# list()メソッドでgoogleapiclient.http.HttpRequestオブジェクトが得られ、
# execute()メソッドを実行すると実際にHTTPリクエストが送られて、APIのレスポンスが得られる。
search_response = youtube.search().list(
    part='snippet',
    q='玉置浩二',
    type='video'
).execute()

# search_responseはAPIのレスポンスのJSONをパースしたdict。
for item in search_response['items']:
    print('\ntitle: ' + item['snippet']['title'] +
          '\ndiscription: ' + item['snippet']['description'])
