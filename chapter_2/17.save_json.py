# ==Json形式の文字列に変換する==

import json

cities = [
    {'rank': 1, 'city': 'Shanghai', 'population': 24150000},
    {'rank': 2, 'city': 'Karachi', 'population': 23500000},
    {'rank': 3, 'city': 'Beijing', 'population': 21516000}

]

# json.dumps()で引数のobjをJSON形式のstrオブジェクトに直列化します。
# json.dump()だと引数のobjをJSON形式のfp(.write()がサポートされているfile-like object)へのストリームとして直列化されます。
print(json.dumps(cities))

# ↑上記の出力方法だと一行で出力されるため、整形して出力
print(json.dumps(cities, ensure_ascii=False, indent=2))

# 直接ファイルに保存
with open('top_cities.json', 'w') as f:
    json.dump(cities, f, ensure_ascii=False, indent=2)
