# ==リストのリストをCSV形式で保存する==

import csv

# ファイル書き込み用に開く。
# newline=''は改行コードの自動変換を抑制する
with open('top_cities.csv', 'w', newline='') as f:

    # csv.writer => 与えられたファイルオブジェクトに書き込むためのwriterオブジェクトを返します。
    # 引数のファイルオブジェクトはwrite()メソッドを持つ任意のオブジェクトです。
    writer = csv.writer(f)

    # 1行を出力
    writer.writerow(['rank', 'city', 'population'])

    # 複数行を一度に出力
    writer.writerows([
        [1, 'Shanghai', 24150000],
        [2, 'Karachi', 23500000],
        [3, 'Beijing', 21516000]
    ])