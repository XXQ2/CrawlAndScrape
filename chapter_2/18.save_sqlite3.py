# ==SQLite3への保存==

import sqlite3
from contextlib import closing

# top_cities.dbファイルを開き、コネクションを取得。
# contextlib.closingを使うことでconnを明示的にcloseする必要は無く、
# 　エラーが発生した場合でも、withブロックを出るときにclose()が呼ばれる。
with closing(sqlite3.connect('top_cities.db')) as conn:

    # カーソルの取得。
    # SQLを実行するためにコネクションオブジェクトからカーソルを取得する必要がある。
    c = conn.cursor()

    # このスクリプトを何度実行しても同じ結果になるようにするためcitiesテーブルが存在する場合は削除する。
    c.execute('DROP TABLE IF EXISTS cities')

    # citiesテーブルの作成
    c.execute('''
        CREATE TABLE cities (
            rank integer,
            city text,
            population integer
        )
    ''')

    # ４つのインサート方法を紹介
    # 通常のインサート
    c.execute('INSERT INTO cities VALUES (1, "Shanghai", 24150000)')

    # パラメータで置き換える場所（プレースホルダ）は?で指定する
    sql = 'INSERT INTO cities VALUES (?,?,?)'
    city = (2, 'Karachi', 23500000)
    c.execute(sql, city)

    # パラメータが辞書の場合、プレースホルダは:キー名で指定する
    c.execute('INSERT INTO cities VALUES (:rank, :city, :population)',
              {'rank': 3, 'city': 'Beijing', 'population': 21516000})

    # executemany()メソッドで複数のパラメータをリストで指定できる
    c.executemany('INSERT INTO cities VALUES (:rank, :city, :population)',
                  (
                      {'rank': 4, 'city': 'Tianjin', 'population': 14722100},
                      {'rank': 5, 'city': 'Istanbul', 'population': 14160467}
                  ))

    # 変更をコミット(保存)する
    conn.commit()

    # 保存したデータを取得する
    c.execute('SELECT * FROM cities')

    # クエリの結果はfetchall()で取得できる
    for row in c.fetchall():
        print(row)


# sqlite3コマンドが使える場合はターミナルからでも保存したデータの確認が可能
# $ sqlite3 top_cities.db 'select * from cities'
# 1|Shanghai|24150000
# 2|Karachi|23500000
# 3|Beijing|21516000
# 4|Tianjin|14722100
# 5|Istanbul|14160467
