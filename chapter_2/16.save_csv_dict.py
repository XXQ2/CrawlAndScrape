# ==辞書のリストをCSV形式で保存する==

import csv

with open('top_cities.csv', 'w', newline='') as f:

    # DictWriter => 通常の writer のように動作しますが、辞書を出力行にマップするオブジェクトを生成します
    # 第一引数にファイルオブジェクト、第二引数にフィールド名のリストを指定する。
    writer = csv.DictWriter(f, ['rank', 'city', 'population'])

    # 1行目のヘッダーを出力(書き込み)する
    writer.writeheader()

    # フィールド名を指定するため、writerオブジェクト作成時のフィールド順でなくても書き込み可能（通常するべきでない）
    writer.writerows([
        {'rank': 1,              'city': 'Shanghai',     'population': 24150000},
        {'city': 'Karachi',      'population': 23500000, 'rank': 2},
        {'population': 21516000, 'rank': 3,              'city': 'Beijing'}
    ])
