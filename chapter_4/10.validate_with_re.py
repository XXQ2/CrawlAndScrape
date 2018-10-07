# 正規表現で価格として正しいかチェックする

import re

value = '3,000'

# 数値とカンマのみを含む正規表現にマッチするかチェックする。
if not re.search(r'^[0-9,]+$', value):
    raise ValueError('Invalid price')