# Pythonの公式イメージをベースとして使用
FROM python:3.12

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# `flaskr`ディレクトリ全体をコンテナにコピー
COPY flaskr /app/flaskr

# コンテナがリッスンするポートを公開
EXPOSE 5000

# 環境変数を設定（もしFlaskアプリケーションで必要であれば）
ENV FLASK_APP=flaskr

# アプリケーションを起動
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
