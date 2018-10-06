# retryingを使ってリトライ処理を簡潔に書く

import requests
from retrying import retry

# 一時的なエラーを表すステータスコード
TEMPORARY_ERROR_CODES = (408, 500, 502, 503, 504)


def main():
    response = fetch('http://httpbin.org/status/200,404,503')
    if 200 <= response.status_code < 300:
        print("success!")
    else:
        print("Error!")


# stop_max_attempt_numberは最大リトライ回数を指定する
# wait_exponential_multiplierは指数関数的なウェイトをとる場合の初回のウェイトをミリ秒単位で指定する
@retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000)
def fetch(url):
    """
    指定したURLを取得してResponseを返す。一時的なエラーが起きた場合は最大3回リトライする
    """

    print('Retrieving {0}...'.format(url))
    response = requests.get(url)
    print('status: {0}'.format(response.status_code))
    if response.status_code not in TEMPORARY_ERROR_CODES:
        return response

    raise Exception('Temporary Error: {0}'.format(response.status_code))


if __name__ == "__main__":
    main()
