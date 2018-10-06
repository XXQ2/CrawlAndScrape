# ステータスコードに応じたエラー処理

import time
import requests

# 一時的なエラーを表すステータスコード
TEMPORARY_ERROR_CODES = (408, 500, 502, 503, 504)


def main():
    response = fetch('http://httpbin.org/status/200,404,503')
    if 200 <= response.status_code < 300:
        print("success!")
    else:
        print("Error!")


def fetch(url):
    """
    指定したURLを取得してResponseオブジェクトを返す。一時的なエラーが起きた場合は最大三回リトライする
    """
    max_retries = 3
    retries = 0
    while True:
        try:
            print('Retrieving {0}...'.format(url))
            response = requests.get(url)
            print('status: {0}'.format(response.status_code))

            # 一時的なエラーでない場合はレスポンスを返す
            if response.status_code not in TEMPORARY_ERROR_CODES:
                return response

        except requests.exceptions.RequestException as ex:
            print('Exception occured: {0}'.format(ex))

        retries += 1
        # リトライ回数の上限を超えた場合は例外を発生させる
        if retries >= max_retries:
            raise Exception('Too Many Retries.')

        wait = 2**(retries - 1)  # 指数関数的なリトライ間隔
        print('Waiting {0} seconds...'.format(wait))
        time.sleep(wait)


if __name__ == "__main__":
    main()