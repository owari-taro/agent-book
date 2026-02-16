# 必要なライブラリをインポート
import boto3
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
#load_dotenv()

# Bedrock呼び出し用のAPIクライアントを作成
client = boto3.client("bedrock-runtime",region_name="us-west-2") # Bedrockが利用可能なリージョンを指定ss

# Converse APIを実行
response = client.converse(
    modelId="global.anthropic.claude-sonnet-4-20250514-v1:0", # モデルID
    messages=[{
        "role": "user",
        "content": [{
            "text": "こんにちは" # 入力メッセージ
        }]
    }]
)

# 実行結果のテキストだけを画面に表示
print(response["output"]["message"]["content"][0]["text"])