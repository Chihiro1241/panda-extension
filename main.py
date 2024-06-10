import requests

# ログイン情報
url = "https://panda.ecs.kyoto-u.ac.jp/portal/"
login_info = {
    'username': 'a0222077',
    'password': 'Toko81481226'
}

# セッションを開始
session = requests.Session()

# ログイン
response = session.post(url, data=login_info)

# ログイン後のページの内容を確認
print(response.text)