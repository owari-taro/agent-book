# MCP (Model Context Protocol) の使い方

このリポジトリでは、MCP (Model Context Protocol) を使用してAIエージェントと外部ツールを統合できます。

## MCPとは？

Model Context Protocol (MCP) は、AIアプリケーションと外部データソースやツールを統合するためのオープンな標準プロトコルです。

## このリポジトリでのMCP使用例

### 1. VS Code設定での使用

`.vscode/settings.json` にMCPサーバーの設定があります：

```json
{
  "mcpServers": {
    "aws-knowledge": {
      "command": "npx",
      "args": ["mcp-remote", "https://knowledge-mcp.global.api.aws"]
    }
  }
}
```

### 2. Pythonコードでの使用

`chapter4/3_mcp_agent.py` で、LangGraphとMCPを組み合わせたエージェントの実装例があります。

主な特徴：
- FileSystem MCPサーバー：ローカルファイルシステムにアクセス
- AWS Knowledge MCPサーバー：AWSドキュメントを検索

### 3. MCPのデモンストレーション

簡単なMCP接続テストを実行するには：

```bash
# 必要なパッケージをインストール
pip install langchain-mcp-adapters

# MCPの設定とコンセプトを確認
python mcp_demo.py

# ローカルファイルシステムMCPサーバーのデモ
python mcp_local_demo.py
```

## 利用可能なMCPサーバー

このリポジトリで使用しているMCPサーバー：

1. **FileSystem MCP Server** (`@modelcontextprotocol/server-filesystem`)
   - ローカルファイルシステムへのアクセス
   - ファイルの読み書き機能

2. **AWS Knowledge MCP Server** (`https://knowledge-mcp.global.api.aws`)
   - AWSドキュメントの検索
   - AWS技術情報へのアクセス

## トラブルシューティング

### よくある質問

**Q: mcp使えますか？ (Can you use MCP?)**

A: はい、MCPは使用可能です！このリポジトリには以下が含まれています：

1. ✅ VS CodeでのMCP設定 (`.vscode/settings.json`)
2. ✅ PythonでのMCP使用例 (`chapter4/3_mcp_agent.py`)
3. ✅ MCPデモスクリプト (`mcp_demo.py` と `mcp_local_demo.py`)
4. ✅ 詳細なドキュメント (このファイル)

MCPが正常に設定されていることを確認するには：
```bash
python mcp_demo.py        # 設定とコンセプトを確認
python mcp_local_demo.py  # ローカル環境をテスト
```

### よくある問題

1. **インターネット接続エラー**
   - AWS Knowledge MCPサーバーはオンラインサービスのため、インターネット接続が必要です

2. **パッケージが見つからない**
   ```bash
   pip install langchain-mcp-adapters==0.1.9 uv==0.8.14
   ```

3. **Node.jsパッケージエラー**
   - FileSystem MCPサーバーを使用する場合は、Node.jsとnpxが必要です

## 参考リンク

- [MCP公式ドキュメント](https://modelcontextprotocol.io/)
- [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp)
- 書籍「AIエージェント開発/運用入門」第4章
