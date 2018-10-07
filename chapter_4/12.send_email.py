# メールを送信する

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# MINETextオブジェクトでメッセージを組み立てる
msg = MIMEText('メールの本文です')

msg['Subject'] = Header('メールの件名', 'utf-8')  # 件名に日本語を含める場合はHeaderオブジェクトを使う
msg['From'] = 'me@example.com'  # 差出人のメールアドレス
msg['To'] = 'you@example.com'  # 送信先のメールアドレス


# with smtplib.SMTP('localhost') as smtp:
#     smtp.send_message(msg)  # メールを送信する。


# GmailのSMTPサーバーからメールを送信する場合の例
# 以下でメールを送信する場合はGoogleアカウントの「安全性の低いアプリの許可」を有効にする必要がある
with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
    # Googleアカウントのユーザー名とパスワードを指定してログインする
    # ２段階認証を設定している場合はアプリパスワードを生成して使用する
    smtp.login('user_name', 'login_password')
    smtp.send_message(msg)
