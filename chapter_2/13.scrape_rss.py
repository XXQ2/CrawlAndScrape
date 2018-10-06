# ==ElementTreeでRSSをパースする==

from xml.etree import ElementTree

# parse()でファイルを読み込んで、ElementTreeオブジェクトを得る。
tree = ElementTree.parse('rss2.xml')

# getroot()でXMLのルート要素(この例ではRSS要素)に対応するElementオブジェクトを得る
root = tree.getroot()

# channel/item要素以下のtitle要素とlink要素の文字列を取得し、表示する。
for item in root.findall('channel/item'):
    title = item.find('title').text
    link = item.find('link').text
    print(link, title)