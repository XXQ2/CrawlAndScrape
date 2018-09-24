# ==正規表現によるスクレイピング==

import re
from html import unescape

# プロジェクト配下にダウンロードしたhtmlファイルを開き、レスポンスボディを変数に格納。
with open('../sample.scraping-book.com/dp.html') as f:
    html = f.read()

# findallを使って書籍一冊分のhtml情報を取得する
# re.DOTALL => 改行も含むすべての文字にマッチ
for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html, re.DOTALL):

    # 書籍のurlはa要素のhref属性から取得する
    # .group()に0を渡すと正規表現全体にマッチした値が得られ、
    # 1を渡すと正規表現の()で囲った部分にマッチした値を取得できる
    url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html).group(1)
    url = 'http://sample.scraping-book.com' + url

    title = re.search(r'<p itemprop="name".*?</p>', partial_html).group(0)

    # 値を置き換える
    # re.subでは正規表現でパターン指定できている点に注目。
    title = title.replace('<br/>', ' ')
    title = re.sub(r'<.*?>', '', title)

    title = unescape(title)

    print(url, title)
    print(1)