import re
import sys
from urllib.request import urlopen

f = urlopen('http://sample.scraping-book.com/dp')

# read()メソッド=>HTTPレスポンスのボディをbytes型で取得
# bytes型のレスポンスボディを変数に格納
bytes_content = f.read()

# レスポンスボディの先頭1024byteをASCII文字列としてデコードする
# ASCII範囲外の文字はU+FFFD(REPLACEMENT CHARACTER)に置き換え、例外を発生させない
scanned_text = bytes_content[:1024].decode('ascii', errors='replace')

# 'r' を前置した文字列リテラル内ではバックスラッシュを特別扱いしない。
# ["\']? => 指定されたエンコーディングが""や''で囲まれていた場合を考慮
# \w => “単語”を構成するキャラクタ、つまり文字と数字それにアンダースコア のいずれかにマッチ.
# ([\w-]+) => \wとハイフンが含まれる文字のグループ
match = re.search(r'charset=["\']?([\w-]+)', scanned_text)

if match:
    encoding = match.group(1)
else:
    encoding = 'utf-8'  # charsetが見つからなかった場合はutf-8とする

print('encoding:', encoding, file=sys.stderr)

text = bytes_content.decode(encoding)

print(text)