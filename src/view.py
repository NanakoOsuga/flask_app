#coding: utf-8

from flask import Flask,render_template

# appという名前でFlaskオブジェクトをインスタンス化
app = Flask(__name__)

# --- View側の設定 ---
# ルートディレクトリにアクセスした場合の挙動
@app.route('/')
def index():
    # DBから以下の変数を読み込んできたと仮定
    title = 'ようこそ'
    message = 'MTVデザインパターンでWebアプリ作成'

    return render_template('index.html',title=title, message=message)

    # return render_template('index.html')

# エントリーポイント
if __name__ == '__main__':
    app.run()


