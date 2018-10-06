# 詳細ページからスクレイピングする(1)

import requests
import lxml.html


def main():
    # 複数ページのクロールをするのでセッションを使用する
    session = requests.Session()
    response = session.get('https://gihyo.jp/dp')
    urls = scrape_list_page(response)
    for url in urls:
        response = session.get(url)
        ebook = scrape_detail_page(response)
        print(ebook)
        break  # 1ページだけ試すためここでbreak


def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)

    for a in root.cssselect('#listBook a[itemprop="url"]'):
        url = a.get('href')
        yield url


def scrape_detail_page(response):
    """
    詳細ページのResponseから電子書籍の情報をdictで取得する
    """
    root = lxml.html.fromstring(response.content)
    ebook = {
        'url': response.url,
        'title': root.cssselect('#bookTitle')[0].text_content(),
        'price': root.cssselect('.buy')[0].text,
        # リスト内包表記を使用し目次を取得
        'content': [h3.text_content() for h3 in root.cssselect('#content > h3')]
    }
    return ebook


if __name__ == '__main__':
    main()
