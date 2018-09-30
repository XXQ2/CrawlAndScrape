# MySQLへの保存

import MySQLdb

conn = MySQLdb.connect(db='scraping', user='USER_NAME', passwd='PASSWORD', charset='utf8mb4')

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS cities')


# MySQL Ver8.xからはrankは予約語に追加されたのでカラム名に使用するときはバッククォート(`)で囲んでエラーを回避。
# 全部バッククォート(`)で囲むようにした方が良いかも。
c.execute('''
    CREATE TABLE cities (
        `rank` INTEGER,
        city TEXT,
        population INTEGER
    )
''')

c.execute('INSERT INTO cities VALUES (%s, %s, %s)', (1, 'Shanghai', 24150000))

c.execute('INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)',
          {'rank': 2, 'city': 'Karachi', 'population': 23500000})

c.executemany('INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)',
              [
                  {'rank': 3, 'city': 'Beijing', 'population': 21516000},
                  {'rank': 4, 'city': 'Tianjin', 'population': 14722100},
                  {'rank': 5, 'city': 'Istanbul', 'population': 14160467}
              ])

conn.commit()

c.execute('SELECT * FROM cities')

for row in c.fetchall():
    print(row)

conn.close()
