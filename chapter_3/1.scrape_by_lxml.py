# lxmlでスクレイピングを行う

import lxml.html

# htmlを読み込み、getroot()でHttpElementオブジェクトを得る
tree = lxml.html.parse('../index.html')
html = tree.getroot()

# cssselect()でa要素のリストを取得。
for a in html.cssselect('a'):

    # href属性とリンクのテキストを取得して表示。
    print(a.get('href'), a.text)
