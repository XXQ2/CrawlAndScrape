# エンコーディングを取得してデコードする

import sys
from urllib.request import urlopen

f = urlopen('http://sample.scraping-book.com/dp')

# HTTPヘッダーからエンコーディングを取得(明示されていない場合は’utf-8’とする)
encoding = f.info().get_content_charset(failobj="utf-8")

# エンコーディング情報を標準エラー出力へ出力する
# エラー情報や捕捉情報は標準エラー出力への出力がふさわしい。
print('encoding:', encoding, file=sys.stderr)

# 得られたエンコーディング情報を基に文字列にデコードする
text = f.read().decode(encoding)

# 標準出力へ出力
print(text)